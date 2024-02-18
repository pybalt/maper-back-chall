from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
from django.db.models import Avg
from django.db.models.functions import TruncSecond
from django.db.utils import IntegrityError
class Command(BaseCommand):
    help = """Calculate the runtime of the machines of the latest 24-hours measurements and write the results to the database."""

    def write_to_db(self, runtimes, current_date):
        from metrics.models import MachineRuntime
        with transaction.atomic():
            for machine, runtime in runtimes.items():
                machine_runtime = MachineRuntime.objects.create(
                    machine=machine,
                    runtime=(runtime.total_seconds()/3600),
                    date=current_date
                )
                machine_runtime.save()

    def handle(self, *args, **kwargs):
        self.stdout.write('Updating machine runtimes...')
        from metrics.models import Measurement
        from metrics.utils import calculate_runtimes

        now = timezone.now()

        start_of_last_24_hours = now - timedelta(hours=24)
        """I am taking the average of measurements, considering that we have different sensors, as a way to reduce noisy data."""

        average_measurements = (
            Measurement.objects
            .filter(date__gte=start_of_last_24_hours)
            .annotate(trunc_date=TruncSecond('date'))
            .values('machine', 'trunc_date')
            .annotate(vibration=Avg('vibration'))
            .order_by('machine', 'trunc_date')
        )
        try:
            calculate_runtimes(average_measurements)
        except TypeError:
            self.stdout.write('No measurements in the last 24 hours.')
        except IntegrityError:
            self.stdout.write('Data already calculated.')
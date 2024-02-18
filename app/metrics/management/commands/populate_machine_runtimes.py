from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Avg
from django.db.models.functions import TruncSecond
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = """
    This command is useful due to the fact that the measurements were not being taken recently.
    We need to populate the database with the measurements from the .csv file and then calculate the runtimes.
    """

    def write_to_db(self, runtimes, current_date):
        from metrics.models import MachineRuntime
        from machine.models import Machine
        with transaction.atomic():
            for machine, runtime in runtimes.items():
                machine_runtime = MachineRuntime.objects.create(
                    machine=Machine.objects.get(id=machine),
                    runtime=(runtime.total_seconds()/3600),
                    date=current_date
                )
                machine_runtime.save()

    def handle(self, *args, **kwargs):
        from metrics.models import Measurement
        from metrics.utils import calculate_runtimes
        self.stdout.write('Updating machine runtimes...')
        """I am taking the average of measurements, considering that we have different sensors, as a way to reduce noisy data."""
        
        average_measurements = (
            Measurement.objects
            .annotate(trunc_date=TruncSecond('date'))
            .values('machine', 'trunc_date')
            .annotate(vibration=Avg('vibration'))
            .order_by('machine', 'trunc_date')
        )
        try:
            calculate_runtimes(average_measurements)
        except TypeError:
            self.stdout.write('There isn\'t any data to calculate. You must populate the database with measurements first.')
        except IntegrityError:
            self.stdout.write('Data already calculated.')
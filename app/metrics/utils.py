from django.db import transaction
from datetime import timedelta
from django.db.models import QuerySet
from django.db.utils import IntegrityError
import math


def __write_runtimes_to_db(runtimes, current_date):
    from metrics.models import MachineRuntime
    from machine.models import Machine
    with transaction.atomic():
        try:
            for machine, runtime in runtimes.items():
                machine_runtime = MachineRuntime.objects.create(
                    machine=Machine.objects.get(id=machine),
                    runtime=(runtime.total_seconds()/3600),
                    date=current_date
                )
                machine_runtime.save()
        except IntegrityError as e:
            """Data is already loaded."""
            return
        except Exception as e:
            raise e

def calculate_runtimes(average_measurements: QuerySet):
    
    earliest_date = average_measurements.first()['trunc_date']
    latest_date = average_measurements.last()['trunc_date']

    def is_vibrating(measurement):
        if measurement is None:
            return False
        return math.trunc(measurement['vibration']) > 0

    runtimes = {}
    start_up_times = {}
    turn_off_times = {}
    current_date = earliest_date
    while current_date <= latest_date:
        print(f'Current date {current_date}...')

        measurements = average_measurements.filter(date__date=current_date).order_by('machine', 'date')
        list_measurements = list(measurements)
        
        previous_measurement = None

        for index_measurement in range(len(list_measurements)):
            measurement = list_measurements[index_measurement]
            previous_measurement = list_measurements[index_measurement - 1] if index_measurement > 0 else None

            machine = measurement['machine']

            if machine not in runtimes:
                runtimes[machine] = timedelta(0)

            if is_vibrating(measurement) and not is_vibrating(previous_measurement):
                start_up_times[machine] = measurement['trunc_date']
            elif not is_vibrating(measurement) and is_vibrating(previous_measurement) and machine in start_up_times:
                turn_off_times[machine] = measurement['trunc_date']
                runtime = turn_off_times[machine] - start_up_times[machine]
                runtimes[machine] += runtime
                del start_up_times[machine]
                del turn_off_times[machine]
        
        for machine, runtime in runtimes.items():
            if(runtime.total_seconds()/3600 > 24):
                raise Exception(f'Runtime for machine {machine} is greater than 24 hours.')

        __write_runtimes_to_db(runtimes, current_date)

        current_date += timedelta(days=1)
        
        runtimes = {}
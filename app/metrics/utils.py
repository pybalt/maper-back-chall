from django.db import transaction
from datetime import timedelta
from django.db.models import QuerySet
from django.db.utils import IntegrityError
import math

def __write_runtimes_to_db(array_of_runtimes):
    from metrics.models import MachineRuntime
    from machine.models import Machine

    machine_runtimes = []
    with transaction.atomic():
        for runtimes in array_of_runtimes:
            date = runtimes['date']
            runtimes = runtimes['runtimes']
            for machine, runtime in runtimes.items():
                machine_instance = Machine.objects.get(id=machine)
                runtime_hours = runtime.total_seconds() / 3600
                machine_runtime = MachineRuntime(machine=machine_instance, runtime=runtime_hours, date=date)
                machine_runtimes.append(machine_runtime)
        try:
            inserted_objects = MachineRuntime.objects.bulk_create(machine_runtimes)
            print(f'{len(inserted_objects.count())} runtimes were successfully written to the database.')
        except IntegrityError:
            print('Data already calculated.')

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
    array_of_runtimes = []
    while current_date <= latest_date:

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

        current_date += timedelta(days=1)
        
        array_of_runtimes.append({'date': current_date, 'runtimes': runtimes})
        runtimes = {}

    __write_runtimes_to_db(array_of_runtimes)
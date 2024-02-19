import csv
import os
from typing import Any
from datetime import datetime
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from machine.models import Machine
from sensors.models import Sensor
from metrics.models import Measurement

def is_populated(_id) -> bool:
    return Measurement.objects.filter(id=_id).exists()

class Command(BaseCommand):
    help = 'Load data from challenge_backend.csv'
    def handle(self, *args: Any, **options: Any) -> str | None:
        print('Loading data from challenge_backend.csv')
        with open('challenge_backend.csv') as file:
            reader = csv.DictReader(file)
            measurements = []
            checked = False
            for row in reader:
                if not checked and is_populated(row['id']):
                    print(f'DB already populated')
                    break
                else:
                    checked = True
                machine, created = Machine.objects.get_or_create(id=row['machine'])
                sensor, created = Sensor.objects.get_or_create(id=row['sensor'], machine=machine)
                measurement = Measurement(
                    id=row['id'],
                    vibration=row['vibration'],
                    date=datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S.%f %z'),
                    sensor=sensor,
                    machine=machine
                )
                measurements.append(measurement)

                Measurement.objects.bulk_create(measurements)

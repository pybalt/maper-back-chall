import csv
from typing import Any
from datetime import datetime
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from machine.models import Machine
from sensors.models import Sensor
from metrics.models import Measurement

class Command(BaseCommand):
    help = 'Load data from challenge_backend.csv'
    def handle(self, *args: Any, **options: Any) -> str | None:
        print('Loading data from challenge_backend.csv')
        with open('challenge_backend.csv') as file:
            reader = csv.DictReader(file)
            try:
                for row in reader:
                    machine, created = Machine.objects.get_or_create(id=row['machine'])
                    sensor, created = Sensor.objects.get_or_create(id=row['sensor'], machine=machine)
                    Measurement.objects.create(
                        id=row['id'],
                        vibration=row['vibration'],
                        date=datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S.%f %z'),
                        sensor=sensor,
                        machine=machine
                    )
            except IntegrityError as e:
                """Data is already loaded."""
                return
            except Exception as e:
                raise e
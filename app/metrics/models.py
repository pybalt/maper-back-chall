from django.db import models
from machine.models import Machine
from sensors.models import Sensor

class Measurement(models.Model):
    id = models.IntegerField(primary_key=True)
    vibration = models.FloatField()
    date = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, models.DO_NOTHING)
    machine = models.ForeignKey(Machine, models.DO_NOTHING)

    class Meta:
        ordering = ['date']
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'
        indexes = [
            models.Index(fields=['date'], name='measurement_date_idx')
        ]

class MachineRuntime(models.Model):
    machine = models.ForeignKey(Machine, models.DO_NOTHING)
    date = models.DateField()
    runtime = models.FloatField()

    class Meta:
        unique_together = ('machine', 'date')
        ordering = ['date']
        indexes = [
            models.Index(fields=['date'], name='machine_runtime_date_idx'),
            models.Index(fields=['machine'], name='machine_idx')
        ]
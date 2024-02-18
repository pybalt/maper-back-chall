from django.db import models
from machine.models import Machine


class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    machine = models.ForeignKey(Machine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensors'
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'], name='sensor_id_idx')
        ]
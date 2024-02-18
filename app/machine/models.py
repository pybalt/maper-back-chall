from django.db import models

class Machine(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'], name='machine_id_idx')
        ]
# Generated by Django 5.0.2 on 2024-02-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Machine',
                'verbose_name_plural': 'Machines',
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='machine_id_idx')],
            },
        ),
    ]

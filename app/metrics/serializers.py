from rest_framework import serializers
from .models import MachineRuntime, Measurement
from sensors.models import Sensor
from machine.models import Machine

class MachineRuntimeSerializer(serializers.ModelSerializer):
    machine = serializers.IntegerField(help_text='Machine ID')
    runtime = serializers.IntegerField(help_text='Runtime in hours')

    class Meta:
        model = MachineRuntime
        fields = ('machine', 'runtime', 'date')

class MeasurementSerializer(serializers.ModelSerializer):
    vibration = serializers.FloatField(help_text='Vibration level')
    date = serializers.DateTimeField(help_text='Date and time of measurement')
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), help_text='Sensor ID')
    machine = serializers.PrimaryKeyRelatedField(queryset=Machine.objects.all(), help_text='Machine ID')

    class Meta:
        model = Measurement
        fields = ('vibration', 'date', 'sensor', 'machine')
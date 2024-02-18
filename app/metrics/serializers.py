from rest_framework import serializers
from .models import MachineRuntime

class MachineRuntimeSerializer(serializers.ModelSerializer):
    machine = serializers.IntegerField(help_text='Machine ID')
    runtime = serializers.IntegerField(help_text='Runtime in hours')

    class Meta:
        model = MachineRuntime
        fields = ('machine', 'runtime', 'date')
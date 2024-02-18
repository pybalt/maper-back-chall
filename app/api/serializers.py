from rest_framework import serializers
from datetime import date

class MachineRuntimeRequestSerializer(serializers.Serializer):
    machine_id = serializers.IntegerField(default=2341)
    date = serializers.DateField(default=date(year=2024, month=1, day=20))

    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError('Date cannot be in the future')
        return value

    def validate(self, data):
        if not data.get('machine_id') or not data.get('date'):
            raise serializers.ValidationError('Machine ID and Date are required')
        return data

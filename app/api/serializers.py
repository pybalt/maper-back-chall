from rest_framework import serializers
from datetime import date

class DateBasedSerializer(serializers.Serializer):
    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError('Date cannot be in the future')
        return value

class MachineRuntimeRequestSerializer(DateBasedSerializer):
    machine_id = serializers.IntegerField(default=2341)
    date = serializers.DateField(default=date(year=2024, month=1, day=20))

    def validate(self, data):
        if not data.get('machine_id') or not data.get('date'):
            raise serializers.ValidationError('Machine ID and Date are required')
        return data

class SensorDataRequestSerializer(DateBasedSerializer):
    sensors = serializers.ListField(child=serializers.IntegerField(), help_text='List of sensor IDs', default=[3348, 2363, 2371, 3356, 3346])
    start_date = serializers.DateField(help_text='Start date', default=date(year=2023, month=1, day=30))
    end_date = serializers.DateField(help_text='End date', default=date(year=2024, month=1, day=30))

    def validate_sensors_min_max_length(self, value):
        if not 1 <= len(value) <= 16:
            raise serializers.ValidationError('Number of sensors must be between 1 and 16')
        return value
    
    def validate_max_time_range(self, value):
        if (value - self.start_date).days > 365:
            raise serializers.ValidationError('Time range cannot exceed 1 year')
        return value

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if not data.get('sensors') or not start_date or not end_date:
            raise serializers.ValidationError('Sensors, Start Date and End Date are required')
        if start_date > end_date:
            raise serializers.ValidationError('Start date cannot be greater than end date')
        if (end_date - start_date).days > 365:
            raise serializers.ValidationError('Time range cannot exceed 1 year')

        return data
    
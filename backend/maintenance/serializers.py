from rest_framework import serializers

from .models import Maintenance


class MaintenanceSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.IntegerField(write_only=True)
    vehicle = serializers.PrimaryKeyRelatedField(read_only=True)
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Maintenance
        fields = ['id', 'schedule_date', 'completion_date', 'vehicle', 'vehicle_id', 'description', 'schedule_type']
        read_only_fields = ['id', 'vehicle']

    def validate(self, data):
        vehicle = data.get('vehicle')
        if vehicle and vehicle.status != 'Inactive':
            raise serializers.ValidationError('Only vehicles with status "Inactive" can create maintenance records.')

        return data

    def validate_description(self, value):
        if value:
            return value
        return 'Normal Maintenance'

    def create(self, validated_data):
        maintenance = Maintenance.objects.create(
            vehicle_id=self.context.get("vehicle_id"),
            schedule_date=validated_data['schedule_date'],
            description=validated_data['description'],
            schedule_type="manual",
            completion_date=None,
        )
        return maintenance
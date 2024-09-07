from rest_framework import serializers

from vehicles.models import Vehicle
from .models import Maintenance


class MaintenanceSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.IntegerField(write_only=True)
    vehicle = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Maintenance
        fields = ['id', 'schedule_date', 'completion_date', 'vehicle', 'vehicle_id', 'description', 'schedule_type']
        read_only_fields = ['id', 'vehicle']

    def validate(self, data):
        vehicle = data.get('vehicle')

        # Ensure vehicle status is "Inactive" before allowing creation
        if vehicle and vehicle.status != 'Inactive':
            raise serializers.ValidationError('Only vehicles with status "Inactive" can create maintenance records.')

        return data

    def create(self, validated_data):
        vehicle = Maintenance.objects.create(
            vehicle_id=validated_data['vehicle_id'],
            schedule_date=validated_data['schedule_date'],
            description=validated_data['description'],
            schedule_type="manual",
            completion_date=None,
        )
        return vehicle
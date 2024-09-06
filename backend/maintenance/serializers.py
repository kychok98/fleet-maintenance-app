from rest_framework import serializers

from vehicles.models import Vehicle
from .models import Maintenance


class MaintenanceSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Maintenance
        fields = ['id', 'schedule_date', 'completion_date', 'vehicle_id', 'description', 'schedule_type']
        read_only_fields = ['id']

    def validate(self, data):
        vehicle = data.get('vehicle')

        # Ensure vehicle status is "Pending" before allowing creation
        if vehicle and vehicle.status != 'Pending':
            raise serializers.ValidationError('Only vehicles with status "Pending" can create maintenance records.')

        return data
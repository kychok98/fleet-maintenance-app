from rest_framework import serializers

from vehicles.models import Vehicle
from .models import Maintenance


class MaintenanceSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())

    class Meta:
        model = Maintenance
        fields = ['id', 'vehicle', 'description', 'schedule_type', 'schedule_date', 'completion_date']
        read_only_fields = ['id']

    def validate(self, data):
        vehicle = data.get('vehicle')

        # Ensure vehicle status is "Pending" before allowing creation
        if vehicle and vehicle.status != 'Pending':
            raise serializers.ValidationError('Only vehicles with status "Pending" can create maintenance records.')

        return data
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
            raise serializers.ValidationError({'status':'Only vehicles with status "Inactive" can create maintenance records.'})

        schedule_date = data.get('schedule_date') if data.get('schedule_date') else getattr(self.instance, 'schedule_date')
        completion_date = data.get('completion_date')

        # Check if completion_date is earlier than schedule_date
        if completion_date and schedule_date and completion_date < schedule_date:
            raise serializers.ValidationError(
                {'completion_date': 'Completion date cannot be earlier than the schedule date.'})

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

class MaintenanceCompleteSerializer(serializers.Serializer):
    maintenance_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )

    def validate_maintenance_ids(self, value):
        pending_maintenances = Maintenance.objects.filter(id__in=value)
        if pending_maintenances.count() != len(value):
            raise serializers.ValidationError("One or more maintenance records do not exist.")

        return value
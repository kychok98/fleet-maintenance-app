from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from maintenance.serializers import MaintenanceSerializer
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    maintenances = SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'model', 'year', 'vin', 'mileage', 'last_service_date', 'status', 'maintenances']
        read_only_fields = ['id', 'vin', 'last_service_date', 'status']

    # noinspection PyMethodMayBeStatic
    def get_maintenances(self, instance):
        maintenances = instance.maintenances.order_by('-schedule_date' , 'completion_date')
        return MaintenanceSerializer(maintenances, many=True).data

    def create(self, validated_data):
        vehicle = Vehicle.objects.create(
            make=validated_data['make'],
            model=validated_data['model'],
            year=validated_data['year']
        )
        return vehicle

    def validate(self, data):
        if self.instance and getattr(self.instance, 'mileage') > data['mileage']:
            raise serializers.ValidationError({"mileage":"cannot be decrement."})

        return data
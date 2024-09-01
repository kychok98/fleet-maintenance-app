from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'model', 'year', 'vin', 'mileage', 'last_service_date', 'status']
        read_only_fields = ['id', 'vin', 'status']

    def validate(self, data):
        # todo: Validate mileage cannot decrease.
        # todo: Validate mileage proceed to maintenance to prevent vehicle from inactive status
        return data
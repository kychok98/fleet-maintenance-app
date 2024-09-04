from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'model', 'year', 'vin', 'mileage', 'last_service_date', 'status']
        read_only_fields = ['id', 'vin', 'last_service_date', 'status']

    def create(self, validated_data):
        vehicle = Vehicle.objects.create(
            make=validated_data['make'],
            model=validated_data['model'],
            year=validated_data['year']
        )
        return vehicle

    def validate(self, data):
        if data['mileage'] < getattr(self.instance, 'mileage'):
            raise serializers.ValidationError({"mileage":"cannot be decrement."})

        return data
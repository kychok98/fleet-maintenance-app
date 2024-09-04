from datetime import date
from enum import Enum

from django.db import models


class VehicleStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'

class Vehicle(models.Model):
    MILEAGE_THRESHOLD = 5000

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)

    mileage = models.IntegerField(default=0)
    last_service_date = models.DateField(default=date.today)

    @property
    def status(self):
        if self.maintenances.filter(completion_date__isnull=True).exists():
            return VehicleStatus.PENDING.value

        next_mileage = self.MILEAGE_THRESHOLD * (self.maintenances.count() + 1)
        if self.mileage < next_mileage:
            return VehicleStatus.ACTIVE.value

        return VehicleStatus.INACTIVE.value

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.vin}) - {self.status}"

    def save(self, *args, **kwargs):
        if not self.vin:  # If the VIN is not set, generate a new one
            last_vehicle = Vehicle.objects.all().order_by('id').last()
            if last_vehicle:
                last_vin_num = int(last_vehicle.vin[3:])  # Extract the numeric part of the VIN
                new_vin_num = last_vin_num + 1
            else:
                new_vin_num = 1
            self.vin = f'VIN{new_vin_num:03d}'  # Format the VIN as VIN001, VIN002, etc.

        super().save(*args, **kwargs)
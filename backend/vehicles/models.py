from datetime import timedelta, date
from enum import Enum

from django.db import models
from django.utils import timezone


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
        if self.mileage < self.MILEAGE_THRESHOLD:
            return VehicleStatus.ACTIVE.value
        if self.maintenances.count() < self.mileage // self.MILEAGE_THRESHOLD:
            return VehicleStatus.INACTIVE.value
        if self.maintenances.filter(completion_date__isnull=True).exists():
            return VehicleStatus.PENDING.value
        return VehicleStatus.ACTIVE.value

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.vin}) - {self.status}"

    def schedule_predictive_maintenance(self):
        # Check if mileage is a multiple of 5000 and no maintenance record exists
        if self.mileage and self.mileage % 5000 == 0 and not self.maintenances.filter(
                schedule_date__gte=self.last_service_date).exists():
            self.maintenances.create(
                vehicle=self,
                description="Predictive maintenance required",
                schedule_type="auto",
                schedule_date=timezone.now() + timedelta(days=7),
            )

    def save(self, *args, **kwargs):
        if not self.vin:  # If the VIN is not set, generate a new one
            last_vehicle = Vehicle.objects.all().order_by('id').last()
            if last_vehicle:
                last_vin_num = int(last_vehicle.vin[3:])  # Extract the numeric part of the VIN
                new_vin_num = last_vin_num + 1
            else:
                new_vin_num = 1
            self.vin = f'VIN{new_vin_num:03d}'  # Format the VIN as VIN001, VIN002, etc.

        self.schedule_predictive_maintenance()
        super().save(*args, **kwargs)
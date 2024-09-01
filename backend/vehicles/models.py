from datetime import timedelta
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

    mileage = models.IntegerField()
    last_service_date = models.DateField(default=timezone.now)

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
        if self.mileage % 5000 == 0 and not self.maintenances.filter(
                schedule_date__gte=self.last_service_date).exists():
            self.maintenances.create(
                vehicle=self,
                description="Predictive maintenance required",
                schedule_type="auto",
                schedule_date=timezone.now() + timedelta(days=7),
            )

    def save(self, *args, **kwargs):
        self.schedule_predictive_maintenance()
        super().save(*args, **kwargs)
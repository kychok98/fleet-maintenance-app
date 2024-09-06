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
        return f"{self.id} {self.year} {self.make} {self.model} {self.mileage} - {self.last_service_date} {self.status}"
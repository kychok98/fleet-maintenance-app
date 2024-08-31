from datetime import timedelta

from django.db import models
from django.utils import timezone


class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)

    mileage = models.IntegerField()
    last_service_date = models.DateField(null=True, blank=True)

    def calculate_expected_maintenance_count(self):
        """Calculate the number of expected maintenance records based on mileage."""
        mileage_threshold = 5000
        return self.mileage // mileage_threshold

    @property
    def status(self):
        if self.maintenances.filter(completion_date__isnull=True).exists():
            return 'Upcoming'
        if self.maintenances.count() < self.calculate_expected_maintenance_count():
            return 'Pending'
        return 'Healthy'

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
                schedule_date=timezone.now() + timedelta(days=60),
            )

    def save(self, *args, **kwargs):
        self.schedule_predictive_maintenance()
        super().save(*args, **kwargs)
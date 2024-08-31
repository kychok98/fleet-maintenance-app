from django.db import models
from django.utils import timezone

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)
    mileage = models.IntegerField()
    last_service_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.vin})"

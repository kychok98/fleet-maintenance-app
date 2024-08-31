from django.db import models
from django.utils import timezone

from vehicles.models import Vehicle


class Maintenance(models.Model):
    SCHEDULE_TYPE_CHOICES = [
        ('manual', 'Manual'),
        ('auto', 'Auto'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenances')
    description = models.TextField()
    schedule_type = models.CharField(max_length=10, choices=SCHEDULE_TYPE_CHOICES, default='manual')
    schedule_date = models.DateField(default=timezone.now)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.description} on {self.schedule_date} for {self.vehicle}"
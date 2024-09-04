from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from vehicles.models import Vehicle, VehicleStatus


@receiver(post_save, sender=Vehicle)
def schedule_predictive_maintenance(sender, instance, **kwargs):
    print("schedule_predictive_maintenance: ", instance.mileage, instance.status)
    if not instance.mileage:
        return

    if instance.status == VehicleStatus.INACTIVE.value:
        if not instance.maintenances.filter(schedule_date__gte=instance.last_service_date).exists():
            instance.maintenances.create(
                vehicle=instance,
                description="Predictive maintenance required",
                schedule_type="auto",
                schedule_date=timezone.now() + timedelta(days=7),
            )
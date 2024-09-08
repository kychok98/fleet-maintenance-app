from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from vehicles.models import Vehicle, VehicleStatus


@receiver(post_save, sender=Vehicle)
def schedule_predictive_maintenance(sender, instance, **kwargs):
    print("schedule_predictive_maintenance: ", instance)
    if not instance.mileage:
        return

    if instance.status == VehicleStatus.INACTIVE.value:
        has_pending = instance.maintenances.filter(
                schedule_date__gte=instance.last_service_date,
                completion_date__isnull=True).exists()
        if not has_pending:
            instance.maintenances.create(
                vehicle=instance,
                description="Predictive Mileage Maintenance",
                schedule_type="auto",
                schedule_date=timezone.now() + timedelta(days=7),
            )
from django.db.models.signals import post_save
from django.dispatch import receiver

from maintenance.models import Maintenance


@receiver(post_save, sender=Maintenance)
def update_vehicle_last_service_date(sender, instance, created, **kwargs):
    print("update_vehicle_last_service_date: ", instance.completion_date, created)
    if instance.completion_date:
        instance.vehicle.last_service_date = instance.completion_date
        instance.vehicle.save()

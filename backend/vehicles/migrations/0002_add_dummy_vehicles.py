# Generated by Django 4.2.15 on 2024-08-31 12:24

import datetime
import random

from django.db import migrations
from django.utils import timezone


def create_dummy_vehicles_and_maintenance(apps, schema_editor):
    Vehicle = apps.get_model('vehicles', 'Vehicle')
    Maintenance = apps.get_model('maintenance', 'Maintenance')

    makes_and_models = [
        ("Toyota", "Camry"),
        ("Honda", "Civic"),
        ("Ford", "Mustang"),
        ("Chevrolet", "Malibu"),
        ("Nissan", "Altima"),
        ("BMW", "3 Series"),
        ("Audi", "A4"),
        ("Mercedes-Benz", "C-Class"),
        ("Tesla", "Model 3"),
        ("Hyundai", "Elantra")
    ]

    vehicles = []
    maintenances = []

    for i in range(50):
        make, model = random.choice(makes_and_models)
        year = random.randint(2015, 2022)
        vin = f"VIN{str(i + 1).zfill(3)}"
        mileage = random.randint(1000, 20000)
        last_service_date = datetime.date(2024, random.randint(1, 8), random.randint(1, 28))

        vehicle = Vehicle(
            make=make,
            model=model,
            year=year,
            vin=vin,
            mileage=mileage,
            last_service_date=timezone.now() if mileage < 5000  else last_service_date
        )
        vehicles.append(vehicle)

        # Randomly determine if this vehicle should have maintenance records
        if random.choice([True, False]):
            # Generate maintenance records based on mileage
            maintenance_mileage = 5000
            while maintenance_mileage <= mileage:
                maintenance_mileage += 5000
                maintenance=Maintenance(
                    vehicle=vehicle,
                    schedule_type='auto',
                    schedule_date=last_service_date,
                    completion_date=None if maintenance_mileage > mileage else last_service_date,
                    description='Backdate Routine maintenance'
                )
                maintenances.append(maintenance)

    Vehicle.objects.bulk_create(vehicles)
    Maintenance.objects.bulk_create(maintenances)

class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_dummy_vehicles_and_maintenance),
    ]
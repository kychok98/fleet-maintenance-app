from datetime import date

from django.test import TestCase

from vehicles.models import Vehicle
from .models import Maintenance


class MaintenanceModelTest(TestCase):

    def setUp(self):
        self.vehicle = Vehicle.objects.create(make='Toyota', model='Camry', year=2020, vin='VIN123', mileage=12000)
        self.maintenance_manual = Maintenance.objects.create(
            vehicle=self.vehicle,
            description='Oil Change',
            schedule_date=date(2024, 8, 1),
            schedule_type='manual'
        )
        self.maintenance_auto = Maintenance.objects.create(
            vehicle=self.vehicle,
            description='Tire Rotation',
            schedule_date=date(2024, 8, 1),
            schedule_type='auto'
        )

    def test_manual_schedule_does_not_set_next_schedule_date(self):
        self.assertIsNone(self.maintenance_manual.next_schedule_date)

    def test_auto_schedule_sets_next_schedule_date(self):
        self.assertEqual(self.maintenance_auto.next_schedule_date, date(2025, 1, 28))  # 6 months later

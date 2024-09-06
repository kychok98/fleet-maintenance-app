from django.test import TestCase
from .models import Vehicle

class VehicleModelTest(TestCase):
    def setUp(self):
        Vehicle.objects.create(make="Toyota", model="Corolla", year=2020, id="1", mileage=15000, last_service_date="2024-01-01")

    def test_vehicle_creation(self):
        vehicle = Vehicle.objects.get(vin="1")
        self.assertEqual(vehicle.make, "Toyota")
        self.assertEqual(vehicle.model, "Corolla")

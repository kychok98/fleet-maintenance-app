from vehicles.models import Vehicle, VehicleStatus


class VehicleService:
    @staticmethod
    def get_vehicles(sort_by='-last_service_date', status_filter=None):
        vehicles = Vehicle.objects.all().order_by(sort_by)

        if status_filter:
            if status_filter not in {status.value for status in VehicleStatus}:
                raise ValueError(f"{status_filter} is not a valid status.")

            # Filter in-memory
            vehicles = [vehicle for vehicle in vehicles if vehicle.status == status_filter]

        return vehicles

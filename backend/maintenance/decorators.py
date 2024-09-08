from functools import wraps

from rest_framework.response import Response

from .models import Maintenance


def maintenance_exists(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        vehicle_id = kwargs.get('vehicle_id')
        try:
            pending_maintenance = Maintenance.objects.filter(vehicle_id=vehicle_id, completion_date__isnull=True)
            if pending_maintenance.exists():
                return Response({'error': 'Pending maintenance exists'}, status=400)
        except Maintenance.DoesNotExist:
            return Response({'error': 'Vehicle does not exist'}, status=404)
        return func(request, *args, **kwargs)
    return wrapper

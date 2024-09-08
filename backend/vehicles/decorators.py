from functools import wraps

from rest_framework.response import Response

from .models import Vehicle


def vehicle_exists(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            vehicle = Vehicle.objects.get(id=pk)
        except Vehicle.DoesNotExist:
            return Response({'error': 'Vehicle not found'}, status=404)
        return func(request, vehicle, *args, **kwargs)
    return wrapper

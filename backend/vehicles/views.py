from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Vehicle
from .serializers import VehicleSerializer


@api_view(['GET'])
def get_vehicles(request):
    data = Vehicle.objects.all()
    serializer = VehicleSerializer(data, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
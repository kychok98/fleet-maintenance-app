from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .decorators import vehicle_exists
from .models import Vehicle
from .serializers import VehicleSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List all vehicles': 'GET /vehicles/',
        'Add vehicle': 'POST /vehicles/create',
        'Get vehicle by ID': 'GET /vehicles/<int:pk>',
        'Update vehicle by ID': 'PUT /vehicles/<int:pk>',
        'Delete vehicle by ID': 'DELETE /vehicles/<int:pk>',
    }
    return Response(data=api_urls, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_vehicles(request):
    sort_by = request.query_params.get('sort_by', 'id')
    data = Vehicle.objects.all().order_by(sort_by)
    serializer = VehicleSerializer(data, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_vehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@vehicle_exists
def vehicle_detail(request, vehicle, pk):
    if request.method == 'GET':
        serializer = VehicleSerializer(instance=vehicle)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = VehicleSerializer(instance=vehicle, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
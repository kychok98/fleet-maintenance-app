from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Maintenance
from .serializers import MaintenanceSerializer


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
def list_maintenance(request):
    sort_by = request.query_params.get('sort_by', 'service_date')

    maintenances = Maintenance.objects.all().order_by(sort_by)
    serializer = MaintenanceSerializer(maintenances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_maintenance(request):
    serializer = MaintenanceSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def maintenance_detail(request, pk):
    try:
        maintenance = Maintenance.objects.get(id=pk)
    except Maintenance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MaintenanceSerializer(maintenance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MaintenanceSerializer(maintenance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        maintenance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

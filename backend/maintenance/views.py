from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .decorators import maintenance_exists
from .models import Maintenance
from .serializers import MaintenanceSerializer, MaintenanceCompleteSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List all maintenances': 'GET /maintenance/',
        'Add maintenance by vehicle': 'POST /maintenance/add/<int:vehicle_id>/',
        'Get maintenance by ID': 'GET /maintenance/<int:pk>/',
        'Update maintenance by ID': 'PUT /maintenance/<int:pk>/',
        'Delete maintenance by ID': 'DELETE /maintenance/<int:pk>/',
        'Complete maintenance by vehicle ids': 'POST /maintenance/complete/'
    }
    return Response(data=api_urls, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_maintenance(request):
    sort_by = request.query_params.get('sort_by', '-schedule_date')

    maintenances = Maintenance.objects.all().order_by(sort_by)
    serializer = MaintenanceSerializer(maintenances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@maintenance_exists
def add_maintenance(request, vehicle_id):
    serializer = MaintenanceSerializer(data=request.data, partial=True, context={'vehicle_id': vehicle_id})
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

@api_view(['POST'])
def maintenance_complete(request):
    serializer = MaintenanceCompleteSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    maintenance_ids = serializer.validated_data['maintenance_ids']
    Maintenance.objects.filter(id__in=maintenance_ids).update(
        completion_date=timezone.now()
    )

    return Response({'message': 'Maintenance records marked as complete.'}, status=status.HTTP_200_OK)
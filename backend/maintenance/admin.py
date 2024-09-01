from django.contrib import admin

from .models import Maintenance


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle__last_service_date', 'vehicle__mileage', 'vehicle','description', 'schedule_type', 'schedule_date', 'completion_date')
    search_fields = ('description', 'vehicle__vin')
    list_filter = ('schedule_type', 'schedule_date', 'completion_date')
    date_hierarchy = 'schedule_date'

    @admin.display(description='Last service date')
    def vehicle__last_service_date(self, obj):
        return obj.vehicle.last_service_date

    @admin.display(description='Mileage')
    def vehicle__mileage(self, obj):
        return obj.vehicle.mileage

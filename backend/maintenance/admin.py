from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Maintenance


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle__last_service_date', 'vehicle','description', 'schedule_type', 'schedule_date', 'completion_date')
    search_fields = ('description', 'vehicle__vin')
    list_filter = ('schedule_type', 'schedule_date', 'completion_date')
    date_hierarchy = 'schedule_date'

    @admin.display(description='Last service date')
    def vehicle__last_service_date(self, obj):
        return obj.vehicle.last_service_date

    def save_model(self, request, obj, form, change):
        if not change:  # Only check for new records
            if obj.vehicle.status != 'Pending':
                raise ValidationError('Only vehicles with status "Pending" can have maintenance records.')
        super().save_model(request, obj, form, change)

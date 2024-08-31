from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'vin', 'mileage', 'status', 'last_service_date')
    search_fields = ('make', 'model', 'vin')
    list_filter = ('make', 'year')

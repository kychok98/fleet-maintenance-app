from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', 'mileage', 'status', 'last_service_date')
    search_fields = ('id', 'make', 'model')
    list_filter = ('make', 'year')
    ordering = ('-last_service_date',)

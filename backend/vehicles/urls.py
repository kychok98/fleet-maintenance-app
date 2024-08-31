from django.urls import path

from . import views

urlpatterns = [
    path('overview/', views.api_overview, name='vehicle-api-overview'),

    path('', views.list_vehicles, name='vehicle-list'),
    path('add/', views.add_vehicle, name='vehicle-add'),
    path('<int:pk>/', views.vehicle_detail, name='vehicle-detail'),
]
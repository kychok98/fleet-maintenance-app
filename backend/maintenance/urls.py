from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.api_overview, name='maintenance-api-overview'),

    path('', views.list_maintenance, name='maintenance-list'),
    path('add/<int:vehicle_id>/', views.add_maintenance, name='maintenance-add'),
    path('<int:pk>/', views.maintenance_detail, name='maintenance-detail'),
    path('complete/', views.maintenance_complete, name='maintenance-complete'),
]

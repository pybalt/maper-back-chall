from django.urls import path
from .api_views import machine_runtime, sensor_data

urlpatterns = [
    path('machine_runtime/', machine_runtime, name='machine_runtime'),
    path('sensor_data', sensor_data, name='sensor_data')
]
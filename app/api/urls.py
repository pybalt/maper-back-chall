from django.urls import path
from .api_views import ok, machine_runtime

urlpatterns = [
    path('machine_runtime/', machine_runtime, name='machine_runtime')
]
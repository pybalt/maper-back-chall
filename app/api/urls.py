from django.urls import path
from .api_views import ok

urlpatterns = [
    path('ok/', ok, name='ok'),
]
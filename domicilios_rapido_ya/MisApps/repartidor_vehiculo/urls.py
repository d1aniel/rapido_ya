from django.urls import path
from MisApps.repartidor_vehiculo.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
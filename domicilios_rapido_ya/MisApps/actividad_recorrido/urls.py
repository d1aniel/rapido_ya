from django.urls import path
from MisApps.actividad_recorrido.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
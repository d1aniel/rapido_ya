from django.urls import path
from MisApps.clientes.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
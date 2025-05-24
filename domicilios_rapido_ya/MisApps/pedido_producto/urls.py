from django.urls import path
from MisApps.pedido_producto.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('MisApps.clientes.urls')),
    path('actividad_recorrido/', include('MisApps.actividad_recorrido.urls')),
    path('pedido_producto/', include('MisApps.pedido_producto.urls')),
    path('repartidor_vehiculo/', include('MisApps.repartidor_vehiculo.urls')),
]

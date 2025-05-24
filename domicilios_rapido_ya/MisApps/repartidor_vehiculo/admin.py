from django.contrib import admin
from MisApps.repartidor_vehiculo.models import Vehiculo, Repartidor

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'marca', 'modelo', 'placa')
    search_fields = ('placa', 'marca', 'modelo')

@admin.register(Repartidor)
class RepartidorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'vehiculo')
    search_fields = ('nombre', 'telefono')
    list_filter = ('vehiculo__marca',)

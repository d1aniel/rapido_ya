from django.contrib import admin
from MisApps.repartidor_vehiculo.models import Vehiculo, Repartidor

class RepartidorInline(admin.StackedInline):
    model = Repartidor
    can_delete = False
    # Como es OneToOne, solo 1 objeto
    max_num = 1
    fk_name = 'vehiculo'  # Esto indica la FK en Repartidor que apunta a Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    inlines = [RepartidorInline]
    list_display = ('marca', 'modelo', 'placa', 'tipo')

@admin.register(Repartidor)
class RepartidorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'vehiculo')
    search_fields = ('nombre', 'telefono', 'vehiculo__placa')
from django.contrib import admin
from MisApps.repartidor_vehiculo.models import Vehiculo, Repartidor

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'placa', 'tipo')
    search_fields = ('marca', 'modelo', 'placa')

@admin.register(Repartidor)
class RepartidorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'vehiculo')
    search_fields = ('nombre', 'telefono', 'vehiculo__placa')

class VehiculoInline(admin.StackedInline):
    model = Vehiculo
    extra = 1

class RepartidorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'vehiculo')
    search_fields = ('nombre', 'telefono', 'vehiculo__placa')
    inlines = [VehiculoInline]

    def get_form(self, request, obj=None, **kwargs):
        # Si ya tiene un vehículo, no mostrar el inline para crear otro
        if obj and Vehiculo.objects.filter(repartidor=obj).exists():
            self.inlines = []
        else:
            self.inlines = [VehiculoInline]
        return super().get_form(request, obj, **kwargs)

admin.site.register(Repartidor, RepartidorAdmin)
admin.site.register(Vehiculo)

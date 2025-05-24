from django.contrib import admin
from MyApps.repartidor_vehiculo.models import Vehiculo, Repartidor

class VehiculoInline(admin.StackedInline):
    model = Vehiculo
    extra = 1  # número de formularios adicionales vacíos
    max_num = 1  # solo permitir un vehículo por repartidor
    can_delete = False

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

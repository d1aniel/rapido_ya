# actividad_recorrido/admin.py
#ya tengo sueño
from django.contrib import admin
from MisApps.actividad_recorrido.models import Recorrido, Actividad
from MisApps.repartidor_vehiculo.models import Repartidor 

class ActividadInline(admin.TabularInline):
    model = Actividad
    extra = 1  

@admin.register(Recorrido)
class RecorridoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'fecha', 'hora_inicio', 'hora_fin']
    search_fields = ['pedido__id']
    list_filter = ['fecha']
    inlines = [ActividadInline]
    filter_horizontal = ['repartidores'] 

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['id', 'recorrido', 'descripcion', 'hora_inicio', 'duracion']
    search_fields = ['descripcion']
    list_filter = ['recorrido']

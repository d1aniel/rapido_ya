from django.contrib import admin
from MyApps.clientes.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'direccion')
    search_fields = ('nombre', 'telefono', 'direccion')
    list_filter = ('nombre',)
    ordering = ('id',)
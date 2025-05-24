from django.contrib import admin
from MisApps.clientes.models import Cliente
from MisApps.pedido_producto.models import Pedido

class PedidoInline(admin.TabularInline):  # o admin.StackedInline si lo prefieres vertical
    model = Pedido
    extra = 1  # cuántos formularios vacíos mostrar por defecto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'direccion')
    search_fields = ('nombre', 'telefono', 'direccion')
    list_filter = ('nombre',)
    ordering = ('id',)
    inlines = [PedidoInline]  # aquí se añade el inline
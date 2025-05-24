from django.contrib import admin
from MisApps.pedido_producto.models import Pedido, Producto_Servicio, Pedido_Producto_Servicio

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_hora', 'direccion_entrega', 'estado', 'cliente_nombre', 'repartidor_nombre')
    list_filter = ('estado', 'fecha_hora')
    search_fields = ('direccion_entrega', 'cliente__nombre', 'repartidor__nombre')
    date_hierarchy = 'fecha_hora'


    def cliente_nombre(self, obj):
        return obj.cliente.nombre
    cliente_nombre.short_description = 'Cliente'

   
    def repartidor_nombre(self, obj):
        return obj.repartidor.nombre if obj.repartidor else 'Sin asignar'
    repartidor_nombre.short_description = 'Repartidor'

@admin.register(Producto_Servicio)
class ProductoServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion_corta', 'precio')
    search_fields = ('nombre',)

    def descripcion_corta(self, obj):
        return obj.descripcion[:50] + '...' if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

@admin.register(Pedido_Producto_Servicio)
class PedidoProductoServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido_id', 'producto_nombre', 'cantidad', 'precio_unitario')
    list_filter = ('pedido',)
    search_fields = ('producto_servicio__nombre',)

  
    def producto_nombre(self, obj):
        return obj.producto_servicio.nombre
    producto_nombre.short_description = 'Producto'

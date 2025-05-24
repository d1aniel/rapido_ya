from django.db import models
from MisApps.clientes.models import Cliente
from MisApps.repartidor_vehiculo.models import Repartidor

class Producto_Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'producto_servicio'
        verbose_name = 'Producto o Servicio'
        verbose_name_plural = 'Productos y Servicios'


class Pedido(models.Model):
    fecha_hora = models.DateTimeField()
    direccion_entrega = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    repartidor = models.ForeignKey(Repartidor, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_repartidor')

    class Meta:
        db_table = 'pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class Pedido_Producto_Servicio(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='id_pedido')
    producto_servicio = models.ForeignKey(Producto_Servicio, on_delete=models.CASCADE, db_column='id_producto_servicio')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'pedido_producto_servicio'
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedidos'
        unique_together = ('pedido', 'producto_servicio')
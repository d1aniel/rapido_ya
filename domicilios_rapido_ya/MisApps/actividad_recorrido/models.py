from django.db import models

class Recorrido(models.Model):
    pedido = models.ForeignKey('pedido_producto.Pedido', on_delete=models.CASCADE)
    repartidores = models.ManyToManyField('repartidor_vehiculo.Repartidor', related_name='recorridos') 
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Recorrido #{self.id} - Pedido #{self.pedido.id}"

class Actividad(models.Model):
    recorrido = models.ForeignKey(Recorrido, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=130)
    hora_inicio = models.TimeField()
    duracion = models.DurationField()

    def __str__(self):
        return f"Actividad #{self.id} - Recorrido #{self.recorrido.id}"

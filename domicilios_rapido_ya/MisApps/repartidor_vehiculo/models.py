from django.db import models

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=50, null=True, blank=True)
    placa = models.CharField(max_length=20, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    marca = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Vehiculo'
        managed = True
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'


class Repartidor(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, db_column='id_vehiculo')

    class Meta:
        db_table = 'Repartidor'
        managed = True
        verbose_name = 'Repartidor'
        verbose_name_plural = 'Repartidores'

    def __str__(self):
        return self.nombre or f"Repartidor #{self.id}"
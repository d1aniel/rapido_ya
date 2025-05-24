from django.db import models

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=20)
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"


class Repartidor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'Cliente'
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre or f"Cliente #{self.id}"

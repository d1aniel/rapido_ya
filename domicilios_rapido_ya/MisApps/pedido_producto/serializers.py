from rest_framework import serializers
from .models import Producto_Servicio, Pedido, Pedido_Producto_Servicio

class ProductoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_Servicio
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoProductoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Producto_Servicio
        fields = '__all__'

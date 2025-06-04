from rest_framework import viewsets
from .models import Producto_Servicio, Pedido, Pedido_Producto_Servicio
from .serializers import (
    ProductoServicioSerializer,
    PedidoSerializer,
    PedidoProductoServicioSerializer
)

class ProductoServicioViewSet(viewsets.ModelViewSet):
    queryset = Producto_Servicio.objects.all()
    serializer_class = ProductoServicioSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoProductoServicioViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Producto_Servicio.objects.all()
    serializer_class = PedidoProductoServicioSerializer

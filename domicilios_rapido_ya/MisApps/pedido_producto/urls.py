from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductoServicioViewSet,
    PedidoViewSet,
    PedidoProductoServicioViewSet
)

router = DefaultRouter()
router.register(r'productos-servicios', ProductoServicioViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles-pedido', PedidoProductoServicioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, RepartidorViewSet

router = DefaultRouter()
router.register(r"vehiculos", VehiculoViewSet)
router.register(r"repartidores", RepartidorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecorridoViewSet, ActividadViewSet

router = DefaultRouter()
router.register(r'recorridos', RecorridoViewSet)
router.register(r'actividades', ActividadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

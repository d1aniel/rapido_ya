from rest_framework import viewsets
from .models import Recorrido, Actividad
from .serializers import RecorridoSerializer, ActividadSerializer

class RecorridoViewSet(viewsets.ModelViewSet):
    queryset = Recorrido.objects.all()
    serializer_class = RecorridoSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

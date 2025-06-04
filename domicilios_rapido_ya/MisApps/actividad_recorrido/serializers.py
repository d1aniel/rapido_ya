from rest_framework import serializers
from .models import Recorrido, Actividad

class RecorridoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recorrido
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

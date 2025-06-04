from rest_framework import serializers
from .models import Vehiculo, Repartidor

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class RepartidorSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()

    class Meta:
        model = Repartidor
        fields = ['id', 'nombre', 'telefono', 'vehiculo']

    def create(self, validated_data):
        vehiculo_data = validated_data.pop('vehiculo')
        vehiculo = Vehiculo.objects.create(**vehiculo_data)
        repartidor = Repartidor.objects.create(vehiculo=vehiculo, **validated_data)
        return repartidor

    def update(self, instance, validated_data):
        vehiculo_data = validated_data.pop('vehiculo', None)
        if vehiculo_data:
            # Actualizar campos del vehículo existente
            for attr, value in vehiculo_data.items():
                setattr(instance.vehiculo, attr, value)
            instance.vehiculo.save()

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance

from django.core.management.base import BaseCommand
from MisApps.clientes.models import Cliente
from MisApps.pedido_producto.models import Producto_Servicio, Pedido, Pedido_Producto_Servicio
from MisApps.repartidor_vehiculo.models import Repartidor, Vehiculo
from MisApps.actividad_recorrido.models import Recorrido, Actividad
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = 'Carga datos falsos en la base de datos Rapido_Ya'

    def handle(self, *args, **kwargs):
        fake = Faker('es_CO')

        # Crear Clientes
        clientes = []
        for _ in range(20):
            cliente = Cliente.objects.create(
                nombre=fake.name(),
                telefono=fake.numerify(text='##########')[:15],
                direccion=fake.address()
            )
            clientes.append(cliente)

        # Crear Vehículos
        vehiculos = []
        for _ in range(10):
            vehiculo = Vehiculo.objects.create(
                tipo=random.choice(['Moto', 'Bicicleta', 'Carro']),
                placa=fake.unique.license_plate(),
                modelo=fake.word(),
                marca=fake.company()[:20]
            )
            vehiculos.append(vehiculo)

        # Crear Repartidores: asignar vehículos únicos para evitar errores OneToOne
        repartidores = []
        vehiculos_disponibles = vehiculos.copy()
        for _ in range(10):
            vehiculo_asignado = vehiculos_disponibles.pop(0)  # Asignar un vehículo único
            repartidor = Repartidor.objects.create(
                nombre=fake.name(),
                telefono=fake.phone_number()[:15],
                vehiculo=vehiculo_asignado
            )
            repartidores.append(repartidor)

        # Crear Productos o Servicios
        productos = []
        for _ in range(30):
            producto = Producto_Servicio.objects.create(
                nombre=fake.word().capitalize(),
                descripcion=fake.sentence(),
                precio=random.randint(5000, 500000)
            )
            productos.append(producto)

        # Crear Pedidos
        pedidos = []
        for _ in range(20):
            pedido = Pedido.objects.create(
                fecha_Hora=fake.date_time_this_year(),
                direccion_Entrega=fake.address(),
                estado=random.choice(['Entregado', 'En camino', 'Pendiente']),
                cliente=random.choice(clientes),
                repartidor=random.choice(repartidores)
            )
            pedidos.append(pedido)

            # Crear relación con productos/servicios
            productos_pedido = random.sample(productos, k=random.randint(1, 5))
            for producto in productos_pedido:
                cantidad = random.randint(1, 3)
                Pedido_Producto_Servicio.objects.create(
                    pedido=pedido,
                    producto_servicio=producto,
                    cantidad=cantidad,
                    precio=producto.precio  # corregido: atributo en minúscula
                )

        # Crear Recorridos
        recorridos = []
        for pedido in pedidos:
            recorrido = Recorrido.objects.create(
                fecha=pedido.fecha_Hora.date(),
                hora_inicio=pedido.fecha_Hora.time(),
                hora_fin=(pedido.fecha_Hora + timedelta(minutes=random.randint(20, 120))).time(),
                pedido=pedido
            )
            recorridos.append(recorrido)

        # Crear Actividades
        for recorrido in recorridos:
            for _ in range(random.randint(1, 3)):
                hora_inicio = timezone.now().time()
                duracion_minutos = random.randint(10, 60)
                # Para duracion, es mejor guardar un timedelta en lugar de un time
                # Pero si el modelo espera time, aquí simplemente asignamos la hora de fin:
                duracion = (timezone.now() + timedelta(minutes=duracion_minutos)).time()
                Actividad.objects.create(
                    descripcion=fake.sentence(),
                    hora_inicio=hora_inicio,
                    duracion=duracion,
                    id_recorrido=recorrido
                )

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada con datos falsos exitosamente!'))
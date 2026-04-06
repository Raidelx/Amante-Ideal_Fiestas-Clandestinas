"""
Capa de Repositorio — acceso a datos para Fiestas e Invitados.
Abstrae las queries de Django ORM del resto de la aplicación.
"""
from django.utils import timezone
from apps.fiestas.models import Fiesta, Invitado


class FiestaRepository:
    @staticmethod
    def get_all():
        return Fiesta.objects.all()

    @staticmethod
    def get_disponibles():
        """Fiestas abiertas con fecha futura."""
        return Fiesta.objects.filter(
            estado='abierta',
            fecha_hora__gte=timezone.now()
        )

    @staticmethod
    def get_by_id(fiesta_id):
        try:
            return Fiesta.objects.get(pk=fiesta_id)
        except Fiesta.DoesNotExist:
            return None

    @staticmethod
    def get_by_codigo(codigo):
        try:
            return Fiesta.objects.get(codigo_acceso=codigo)
        except Fiesta.DoesNotExist:
            return None

    @staticmethod
    def crear(nombre, descripcion, direccion, capacidad, fecha_hora,
              codigo_acceso, latitud=None, longitud=None):
        return Fiesta.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            direccion=direccion,
            capacidad=capacidad,
            fecha_hora=fecha_hora,
            codigo_acceso=codigo_acceso,
            latitud=latitud,
            longitud=longitud,
        )

    @staticmethod
    def actualizar_estado(fiesta, nuevo_estado):
        fiesta.estado = nuevo_estado
        fiesta.save(update_fields=['estado'])
        return fiesta


class InvitadoRepository:
    @staticmethod
    def get_by_fiesta(fiesta):
        return Invitado.objects.filter(fiesta=fiesta)

    @staticmethod
    def get_confirmados(fiesta):
        return Invitado.objects.filter(fiesta=fiesta, estado='confirmado')

    @staticmethod
    def get_by_alias_y_fiesta(alias, fiesta):
        try:
            return Invitado.objects.get(alias=alias, fiesta=fiesta)
        except Invitado.DoesNotExist:
            return None

    @staticmethod
    def crear(fiesta, nombre, alias, telefono, codigo_acceso):
        return Invitado.objects.create(
            fiesta=fiesta,
            nombre=nombre,
            alias=alias,
            telefono=telefono,
            codigo_acceso=codigo_acceso,
            estado='pendiente',
        )

    @staticmethod
    def confirmar(invitado):
        invitado.estado = 'confirmado'
        invitado.save(update_fields=['estado'])
        return invitado

    @staticmethod
    def rechazar(invitado):
        invitado.estado = 'rechazado'
        invitado.save(update_fields=['estado'])
        return invitado

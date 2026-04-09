"""
Capa de Lógica de Negocio — reglas y operaciones de dominio.
No conoce Django HTTP, solo trabaja con repositorios y modelos.
"""
import random
import string
from datetime import datetime
from django.utils import timezone
from apps.fiestas.repositories import FiestaRepository, InvitadoRepository


def _generar_codigo(longitud=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=longitud))


class FiestaService:
    """Lógica de negocio para fiestas."""

    @staticmethod
    def listar_fiestas_disponibles():
        """Retorna fiestas abiertas con cupo, ordenadas por fecha."""
        fiestas = FiestaRepository.get_disponibles()
        return [f for f in fiestas if f.tiene_cupo]

    @staticmethod
    def listar_todas():
        return FiestaRepository.get_all()

    @staticmethod
    def obtener_fiesta(fiesta_id):
        fiesta = FiestaRepository.get_by_id(fiesta_id)
        if not fiesta:
            raise ValueError(f"Fiesta con ID {fiesta_id} no encontrada.")
        return fiesta

    @staticmethod
    def crear_fiesta(nombre, descripcion, direccion, capacidad,
                     fecha_hora_str, latitud=None, longitud=None):
        """
        Crea una nueva fiesta con validaciones de negocio.
        fecha_hora_str: string ISO 'YYYY-MM-DDTHH:MM'
        """
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de la fiesta es obligatorio.")
        if not direccion or not direccion.strip():
            raise ValueError("La dirección es obligatoria.")
        try:
            capacidad = int(capacidad)
            if capacidad < 2:
                raise ValueError("La capacidad mínima es 2 personas.")
            if capacidad > 500:
                raise ValueError("La capacidad máxima es 500 personas.")
        except (TypeError, ValueError) as e:
            if "capacidad" in str(e):
                raise
            raise ValueError("La capacidad debe ser un número entero.")

        try:
            fecha_hora = datetime.fromisoformat(fecha_hora_str)
            if timezone.is_naive(fecha_hora):
                fecha_hora = timezone.make_aware(fecha_hora)
        except (ValueError, TypeError):
            raise ValueError("Formato de fecha inválido. Usa YYYY-MM-DDTHH:MM.")

        if fecha_hora <= timezone.now():
            raise ValueError("La fiesta debe ser en el futuro.")

        codigo = _generar_codigo()
        while FiestaRepository.get_by_codigo(codigo):
            codigo = _generar_codigo()

        return FiestaRepository.crear(
            nombre=nombre.strip(),
            descripcion=descripcion.strip() if descripcion else '',
            direccion=direccion.strip(),
            capacidad=capacidad,
            fecha_hora=fecha_hora,
            codigo_acceso=codigo,
            latitud=latitud,
            longitud=longitud,
        )

    @staticmethod
    def cancelar_fiesta(fiesta_id):
        fiesta = FiestaRepository.get_by_id(fiesta_id)
        if not fiesta:
            raise ValueError("Fiesta no encontrada.")
        if fiesta.estado == 'cancelada':
            raise ValueError("La fiesta ya está cancelada.")
        return FiestaRepository.actualizar_estado(fiesta, 'cancelada')


class InvitadoService:
    """Lógica de negocio para gestión de invitados."""

    @staticmethod
    def solicitar_ingreso(fiesta_id, nombre, alias, telefono=''):
        """
        Registra una solicitud de ingreso a una fiesta.
        Retorna (invitado, mensaje).
        """
        fiesta = FiestaRepository.get_by_id(fiesta_id)
        if not fiesta:
            raise ValueError("Fiesta no encontrada.")
        if not fiesta.tiene_cupo:
            raise ValueError("La fiesta está llena o cerrada.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        if not alias or not alias.strip():
            raise ValueError("El alias es obligatorio.")

        existente = InvitadoRepository.get_by_alias_y_fiesta(alias.strip(), fiesta)
        if existente:
            raise ValueError(f"El alias '{alias}' ya está registrado en esta fiesta.")

        codigo = _generar_codigo(8)
        invitado = InvitadoRepository.crear(
            fiesta=fiesta,
            nombre=nombre.strip(),
            alias=alias.strip(),
            telefono=telefono.strip(),
            codigo_acceso=codigo,
        )
        return invitado, f"Solicitud enviada. Tu código de acceso: {codigo}"

    @staticmethod
    def confirmar_invitado(invitado_id):
        from apps.fiestas.models import Invitado
        try:
            inv = Invitado.objects.get(pk=invitado_id)
        except Invitado.DoesNotExist:
            raise ValueError("Invitado no encontrado.")
        if inv.estado == 'confirmado':
            raise ValueError("El invitado ya está confirmado.")
        if not inv.fiesta.tiene_cupo:
            raise ValueError("No hay cupo disponible.")
        inv = InvitadoRepository.confirmar(inv)

        # Si se llenó, actualizar estado fiesta
        if not inv.fiesta.tiene_cupo:
            FiestaRepository.actualizar_estado(inv.fiesta, 'llena')

        return inv

    @staticmethod
    def rechazar_invitado(invitado_id):
        from apps.fiestas.models import Invitado
        try:
            inv = Invitado.objects.get(pk=invitado_id)
        except Invitado.DoesNotExist:
            raise ValueError("Invitado no encontrado.")
        return InvitadoRepository.rechazar(inv)

    @staticmethod
    def listar_invitados(fiesta_id):
        fiesta = FiestaRepository.get_by_id(fiesta_id)
        if not fiesta:
            raise ValueError("Fiesta no encontrada.")
        return InvitadoRepository.get_by_fiesta(fiesta), fiesta

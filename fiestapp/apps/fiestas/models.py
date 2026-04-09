from django.db import models


class Fiesta(models.Model):
    ESTADO_CHOICES = [
        ('abierta', 'Abierta'),
        ('llena', 'Llena'),
        ('cancelada', 'Cancelada'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=300)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    capacidad = models.PositiveIntegerField()
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='abierta')
    codigo_acceso = models.CharField(max_length=10, unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_hora']
        verbose_name = 'Fiesta'
        verbose_name_plural = 'Fiestas'

    def __str__(self):
        return f"{self.nombre} ({self.fecha_hora.strftime('%d/%m/%Y')})"

    @property
    def invitados_confirmados(self):
        return self.invitado_set.filter(estado='confirmado').count()

    @property
    def cupos_disponibles(self):
        return self.capacidad - self.invitados_confirmados

    @property
    def tiene_cupo(self):
        return self.cupos_disponibles > 0 and self.estado == 'abierta'


class Invitado(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('rechazado', 'Rechazado'),
    ]

    fiesta = models.ForeignKey(Fiesta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    alias = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    solicitado_en = models.DateTimeField(auto_now_add=True)
    codigo_acceso = models.CharField(max_length=10)

    class Meta:
        ordering = ['solicitado_en']
        unique_together = ['fiesta', 'alias']

    def __str__(self):
        return f"{self.alias} → {self.fiesta.nombre}"

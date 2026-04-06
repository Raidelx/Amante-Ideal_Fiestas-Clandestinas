from django.contrib import admin
from apps.fiestas.models import Fiesta, Invitado


@admin.register(Fiesta)
class FiestaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_hora', 'estado', 'capacidad',
                    'invitados_confirmados', 'cupos_disponibles', 'codigo_acceso']
    list_filter = ['estado']
    search_fields = ['nombre', 'direccion', 'codigo_acceso']
    readonly_fields = ['codigo_acceso', 'creado_en']


@admin.register(Invitado)
class InvitadoAdmin(admin.ModelAdmin):
    list_display = ['alias', 'nombre', 'fiesta', 'estado', 'solicitado_en']
    list_filter = ['estado', 'fiesta']
    search_fields = ['alias', 'nombre', 'fiesta__nombre']

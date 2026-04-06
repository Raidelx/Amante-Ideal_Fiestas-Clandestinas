#!/usr/bin/env python
"""
Script: setup.py
Inicializa la base de datos y carga datos de prueba.

Uso:
    python scripts/setup.py
    python scripts/setup.py --reset   # borra DB y recrea todo
"""
import os
import sys
import argparse

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fiestapp.settings')

import django
django.setup()


def run_migrations():
    from django.core.management import call_command
    print("⚙  Creando migraciones...")
    call_command('makemigrations', 'fiestas', verbosity=0)
    print("⚙  Aplicando migraciones...")
    call_command('migrate', verbosity=0)
    print("✅ Migraciones completadas.\n")


def cargar_datos_prueba():
    from django.utils import timezone
    from datetime import timedelta
    from apps.fiestas.business import FiestaService, InvitadoService
    from apps.fiestas.models import Fiesta

    if Fiesta.objects.exists():
        print("ℹ  Ya existen datos en la BD. Usa --reset para limpiar.\n")
        return

    print("🎉 Cargando datos de prueba...\n")

    ahora = timezone.now()

    fiestas_data = [
        {
            "nombre": "La Resistencia Vol.3",
            "descripcion": "Techno oscuro y acid. Dress code: todo negro. No fotos.",
            "direccion": "Carrera 13 #85-60, Bogotá",
            "capacidad": 40,
            "fecha_hora_str": (ahora + timedelta(days=3, hours=6)).strftime("%Y-%m-%dT%H:%M"),
            "latitud": "4.676",
            "longitud": "-74.048",
        },
        {
            "nombre": "Finca El Silencio",
            "descripcion": "House y cumbia electrónica en finca privada. Traer sleeping bag.",
            "direccion": "Vía La Calera Km 12, Cundinamarca",
            "capacidad": 60,
            "fecha_hora_str": (ahora + timedelta(days=7, hours=8)).strftime("%Y-%m-%dT%H:%M"),
            "latitud": "4.723",
            "longitud": "-73.969",
        },
        {
            "nombre": "Rooftop Secreto 404",
            "descripcion": "DJ set en terraza con vista a la ciudad. Máximo discreción.",
            "direccion": "Calle 72 #10-07 Piso 12, Bogotá",
            "capacidad": 25,
            "fecha_hora_str": (ahora + timedelta(days=1, hours=5)).strftime("%Y-%m-%dT%H:%M"),
            "latitud": "4.657",
            "longitud": "-74.054",
        },
        {
            "nombre": "Club Underground",
            "descripcion": "Electrónica experimental. Sin teléfonos. Código estricto.",
            "direccion": "Calle 22 Sur #43-10, Medellín",
            "capacidad": 80,
            "fecha_hora_str": (ahora + timedelta(days=5, hours=7)).strftime("%Y-%m-%dT%H:%M"),
            "latitud": "6.217",
            "longitud": "-75.574",
        },
    ]

    fiestas_creadas = []
    for data in fiestas_data:
        try:
            f = FiestaService.crear_fiesta(**data)
            print(f"  ✓ Fiesta creada: '{f.nombre}' [código: {f.codigo_acceso}]")
            fiestas_creadas.append(f)
        except Exception as e:
            print(f"  ✗ Error creando fiesta: {e}")

    print()

    # Agregar algunos invitados de prueba
    if fiestas_creadas:
        invitados_data = [
            ("María García", "la_dj_maria", "+57 310 111 2222"),
            ("Carlos Ruiz", "el_toro", "+57 320 333 4444"),
            ("Sofía Torres", "sofiaT", ""),
            ("Andrés López", "andy_beats", "+57 315 555 6666"),
            ("Valentina Ríos", "valen_r", "+57 316 777 8888"),
        ]

        fiesta_prueba = fiestas_creadas[0]
        print(f"  Agregando invitados a '{fiesta_prueba.nombre}':")
        for nombre, alias, tel in invitados_data:
            try:
                inv, _ = InvitadoService.solicitar_ingreso(fiesta_prueba.id, nombre, alias, tel)
                print(f"    ✓ {alias} (pendiente)")
            except Exception as e:
                print(f"    ✗ Error: {e}")

        # Confirmar algunos
        from apps.fiestas.models import Invitado
        pendientes = Invitado.objects.filter(fiesta=fiesta_prueba, estado='pendiente')[:2]
        for inv in pendientes:
            try:
                InvitadoService.confirmar_invitado(inv.id)
                print(f"    ✓ {inv.alias} → confirmado")
            except Exception as e:
                print(f"    ✗ {e}")

    print("\n✅ Datos de prueba cargados.\n")


def main():
    parser = argparse.ArgumentParser(description='Setup inicial de FiestApp')
    parser.add_argument('--reset', action='store_true',
                        help='Elimina la BD existente y recrea todo')
    args = parser.parse_args()

    if args.reset:
        from django.conf import settings
        db_path = settings.DATABASES['default']['NAME']
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"🗑  BD eliminada: {db_path}")

    # Crear directorio data si no existe
    from django.conf import settings
    os.makedirs(os.path.dirname(settings.DATABASES['default']['NAME']), exist_ok=True)

    run_migrations()
    cargar_datos_prueba()

    print("=" * 54)
    print("  🚀 FiestApp lista para correr:")
    print()
    print("  Servidor completo:   python scripts/run_server.py")
    print("  Frontend invitados:  python scripts/run_frontend_invitados.py")
    print("  Frontend localizar:  python scripts/run_frontend_localizacion.py")
    print("=" * 54)


if __name__ == '__main__':
    main()

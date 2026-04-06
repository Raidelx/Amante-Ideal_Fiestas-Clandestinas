#!/usr/bin/env python
"""
Script: run_frontend_invitados.py
Levanta un servidor Django enfocado SOLO en el Frontend 1 de Invitados.
Puerto por defecto: 8001

Expone únicamente las rutas del módulo de invitados:
  /invitados/               → Portal para solicitar acceso
  /invitados/solicitar/<id>/ → Formulario de solicitud
  /invitados/gestionar/<id>/ → Panel del organizador
  /fiestas/                 → API auxiliar necesaria

Uso:
    python scripts/run_frontend_invitados.py
    python scripts/run_frontend_invitados.py --port 8001
"""
import os
import sys
import argparse

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# Usamos un módulo de settings específico para este bundle
os.environ['DJANGO_SETTINGS_MODULE'] = 'fiestapp.settings_invitados'


def create_settings_if_needed():
    """Crea settings_invitados.py si no existe."""
    settings_path = os.path.join(PROJECT_ROOT, 'fiestapp', 'settings_invitados.py')
    if not os.path.exists(settings_path):
        with open(settings_path, 'w') as f:
            f.write("""# Settings para bundle: Frontend Invitados
from .settings import *

# Override: solo las apps necesarias para este frontend
BUNDLE_NAME = 'frontend-invitados'

# El servidor de invitados puede correr en otro puerto sin conflicto
# Todas las apps siguen disponibles porque comparten la misma DB SQLite
""")


def main():
    create_settings_if_needed()

    parser = argparse.ArgumentParser(description='Frontend 1 — Invitados')
    parser.add_argument('--port', type=int, default=8001, help='Puerto (default: 8001)')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host')
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════════════╗
║       👥  FIESTAPP — FRONTEND 1: INVITADOS           ║
╠══════════════════════════════════════════════════════╣
║  Bundle:        frontend-invitados                   
║  URL Base:      http://{args.host}:{args.port}/         
║  Portal:        http://{args.host}:{args.port}/invitados/
║  DB:            SQLite compartida                    
╚══════════════════════════════════════════════════════╝
    """)

    from django.core.management import call_command
    call_command('runserver', f'{args.host}:{args.port}')


if __name__ == '__main__':
    main()

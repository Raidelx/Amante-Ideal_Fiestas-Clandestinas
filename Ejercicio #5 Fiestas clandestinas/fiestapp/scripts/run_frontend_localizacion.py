#!/usr/bin/env python
"""
Script: run_frontend_localizacion.py
Levanta un servidor Django enfocado SOLO en el Frontend 2 de Localización.
Puerto por defecto: 8002

Expone únicamente las rutas del módulo de localización:
  /localizacion/       → Radar / mapa de fiestas
  /localizacion/<id>/  → Detalle con mapa individual

Uso:
    python scripts/run_frontend_localizacion.py
    python scripts/run_frontend_localizacion.py --port 8002
"""
import os
import sys
import argparse

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'fiestapp.settings_localizacion'


def create_settings_if_needed():
    settings_path = os.path.join(PROJECT_ROOT, 'fiestapp', 'settings_localizacion.py')
    if not os.path.exists(settings_path):
        with open(settings_path, 'w') as f:
            f.write("""# Settings para bundle: Frontend Localización
from .settings import *

BUNDLE_NAME = 'frontend-localizacion'
""")


def main():
    create_settings_if_needed()

    parser = argparse.ArgumentParser(description='Frontend 2 — Localización')
    parser.add_argument('--port', type=int, default=8002, help='Puerto (default: 8002)')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host')
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════════════╗
║       🗺  FIESTAPP — FRONTEND 2: LOCALIZACIÓN        ║
╠══════════════════════════════════════════════════════╣
║  Bundle:        frontend-localizacion                
║  URL Base:      http://{args.host}:{args.port}/         
║  Radar:         http://{args.host}:{args.port}/localizacion/
║  DB:            SQLite compartida                    
╚══════════════════════════════════════════════════════╝
    """)

    from django.core.management import call_command
    call_command('runserver', f'{args.host}:{args.port}')


if __name__ == '__main__':
    main()

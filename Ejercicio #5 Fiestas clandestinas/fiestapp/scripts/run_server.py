#!/usr/bin/env python
"""
Script: run_server.py
Levanta el servidor Django completo en el puerto 8000.
Incluye todas las rutas: /fiestas/, /invitados/, /localizacion/

Uso:
    python scripts/run_server.py
    python scripts/run_server.py --port 9000
"""
import os
import sys
import argparse

# Asegurar que el directorio raíz del proyecto esté en el path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fiestapp.settings')


def main():
    parser = argparse.ArgumentParser(description='Servidor Django completo')
    parser.add_argument('--port', type=int, default=8000, help='Puerto (default: 8000)')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host (default: 127.0.0.1)')
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════════════╗
║           🎉  FIESTAPP — SERVIDOR PRINCIPAL          ║
╠══════════════════════════════════════════════════════╣
║  URL:           http://{args.host}:{args.port}/         
║  Fiestas:       http://{args.host}:{args.port}/fiestas/
║  Invitados:     http://{args.host}:{args.port}/invitados/
║  Localización:  http://{args.host}:{args.port}/localizacion/
║  Admin:         http://{args.host}:{args.port}/admin/
╚══════════════════════════════════════════════════════╝
    """)

    from django.core.management import call_command
    call_command('runserver', f'{args.host}:{args.port}')


if __name__ == '__main__':
    main()

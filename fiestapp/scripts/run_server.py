#!/usr/bin/env python
"""
Script: run_server.py
Levanta el servidor Django completo en el puerto 8000.

Uso:
    python scripts/run_server.py
    python scripts/run_server.py --port 9000
"""
import os
import sys
import argparse
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

    manage = os.path.join(PROJECT_ROOT, 'manage.py')
    subprocess.run([sys.executable, manage, 'runserver', f'{args.host}:{args.port}'], cwd=PROJECT_ROOT)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
"""
Script: run_frontend_localizacion.py
Frontend 2 — Localización en puerto 8002.

Uso:
    python scripts/run_frontend_localizacion.py
    python scripts/run_frontend_localizacion.py --port 8002
"""
import os
import sys
import argparse
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    parser = argparse.ArgumentParser(description='Frontend 2 — Localización')
    parser.add_argument('--port', type=int, default=8002, help='Puerto (default: 8002)')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host')
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════════════╗
║       🗺  FIESTAPP — FRONTEND 2: LOCALIZACIÓN        ║
╠══════════════════════════════════════════════════════╣
║  Bundle:        frontend-localizacion
║  Radar:         http://{args.host}:{args.port}/localizacion/
║  DB:            SQLite compartida
╚══════════════════════════════════════════════════════╝
    """)

    manage = os.path.join(PROJECT_ROOT, 'manage.py')
    subprocess.run([sys.executable, manage, 'runserver', f'{args.host}:{args.port}'], cwd=PROJECT_ROOT)


if __name__ == '__main__':
    main()

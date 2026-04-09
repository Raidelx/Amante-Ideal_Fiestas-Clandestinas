#!/usr/bin/env python
"""
Script: run_frontend_invitados.py
Frontend 1 — Invitados en puerto 8001.

Uso:
    python scripts/run_frontend_invitados.py
    python scripts/run_frontend_invitados.py --port 8001
"""
import os
import sys
import argparse
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    parser = argparse.ArgumentParser(description='Frontend 1 — Invitados')
    parser.add_argument('--port', type=int, default=8001, help='Puerto (default: 8001)')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host')
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════════════╗
║       👥  FIESTAPP — FRONTEND 1: INVITADOS           ║
╠══════════════════════════════════════════════════════╣
║  Bundle:        frontend-invitados
║  Portal:        http://{args.host}:{args.port}/invitados/
║  DB:            SQLite compartida
╚══════════════════════════════════════════════════════╝
    """)

    manage = os.path.join(PROJECT_ROOT, 'manage.py')
    subprocess.run([sys.executable, manage, 'runserver', f'{args.host}:{args.port}'], cwd=PROJECT_ROOT)


if __name__ == '__main__':
    main()

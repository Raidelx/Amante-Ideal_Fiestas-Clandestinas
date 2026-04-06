# ============================================================
#  FiestApp — Makefile
#  Atajos para correr cada bundle de forma independiente
# ============================================================

.PHONY: setup server fe-invitados fe-localizacion reset-db migrate help

help:
	@echo ""
	@echo "  🎉  FiestApp — Comandos disponibles"
	@echo ""
	@echo "  make setup           Instala deps, migra BD y carga datos de prueba"
	@echo "  make server          Servidor completo en :8000"
	@echo "  make fe-invitados    Frontend 1 (Invitados) en :8001"
	@echo "  make fe-localizacion Frontend 2 (Localización) en :8002"
	@echo "  make migrate         Solo corre migraciones"
	@echo "  make reset-db        Borra BD y recarga datos de prueba"
	@echo ""

setup:
	pip install -r requirements.txt
	python scripts/setup.py

migrate:
	python manage.py makemigrations fiestas
	python manage.py migrate

server:
	python scripts/run_server.py

fe-invitados:
	python scripts/run_frontend_invitados.py

fe-localizacion:
	python scripts/run_frontend_localizacion.py

reset-db:
	python scripts/setup.py --reset

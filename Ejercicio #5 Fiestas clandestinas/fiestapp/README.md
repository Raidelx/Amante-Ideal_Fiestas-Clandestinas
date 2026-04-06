# 🎉 FiestApp — Monolito Django para Fiestas Clandestinas

Aplicación Django con Server-Side Rendering para publicar fiestas en casas/fincas,
gestionar invitados y localizar eventos en mapa. Arquitectura monolítica con separación
lógica en capas y dos frontends independientes.

---

## Arquitectura

```
fiestapp/
├── fiestapp/              # Configuración Django (settings, urls, wsgi)
├── apps/
│   ├── fiestas/           # App principal — dominio central
│   │   ├── models.py          → Capa de Modelo (Fiesta, Invitado)
│   │   ├── repositories/      → Capa de Repositorio (acceso a datos)
│   │   │   └── fiesta_repository.py
│   │   ├── business/          → Capa de Lógica de Negocio
│   │   │   └── fiesta_service.py
│   │   ├── views.py           → GET/POST /fiestas/ (HTML + JSON)
│   │   └── urls.py
│   ├── invitados/         # Frontend 1 — Gestión de invitados
│   │   ├── views.py
│   │   └── urls.py
│   └── localizacion/      # Frontend 2 — Radar/mapa de fiestas
│       ├── views.py
│       └── urls.py
├── templates/
│   ├── base.html
│   ├── fiestas/
│   ├── invitados/         → Templates del Frontend 1
│   └── localizacion/      → Templates del Frontend 2
├── scripts/
│   ├── setup.py               → Migraciones + datos de prueba
│   ├── run_server.py          → Servidor completo :8000
│   ├── run_frontend_invitados.py    → Bundle FE1 :8001
│   └── run_frontend_localizacion.py → Bundle FE2 :8002
├── data/                  → SQLite db.sqlite3 (generada automáticamente)
├── manage.py
├── requirements.txt
└── Makefile
```

### Capas de la arquitectura

| Capa | Ubicación | Responsabilidad |
|------|-----------|-----------------|
| **Model** | `apps/fiestas/models.py` | Entidades Django ORM (`Fiesta`, `Invitado`) |
| **Repository** | `apps/fiestas/repositories/` | Queries y acceso a datos, abstrae el ORM |
| **Business Logic** | `apps/fiestas/business/` | Reglas de negocio, validaciones de dominio |
| **Views** | `apps/*/views.py` | HTTP handlers, renderizado de templates |

---

## Instalación y setup

### Requisitos
- Python 3.10+
- pip

### Pasos

```bash
# 1. Clonar / descomprimir el proyecto
cd fiestapp

# 2. (Recomendado) Crear entorno virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Setup completo (migraciones + datos de prueba)
python scripts/setup.py
# O con make:
make setup
```

---

## Correr los servidores

### Opción A — Servidor completo (todas las rutas)

```bash
python scripts/run_server.py
# http://127.0.0.1:8000/
```

### Opción B — Bundles por separado (independientes)

```bash
# Terminal 1 — Frontend Invitados
python scripts/run_frontend_invitados.py
# http://127.0.0.1:8001/invitados/

# Terminal 2 — Frontend Localización
python scripts/run_frontend_localizacion.py
# http://127.0.0.1:8002/localizacion/
```

### Con Make

```bash
make server          # Servidor completo :8000
make fe-invitados    # Frontend 1 :8001
make fe-localizacion # Frontend 2 :8002
```

> Los tres servidores comparten la **misma base de datos SQLite**, por lo que
> los datos creados en uno son visibles en los otros.

---

## API REST

### `POST /fiestas/` — Crear fiesta

```bash
curl -X POST http://127.0.0.1:8000/fiestas/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "La Resistencia Vol.4",
    "descripcion": "Techno oscuro, sin fotos",
    "direccion": "Calle 100 #15-20, Bogotá",
    "capacidad": 50,
    "fecha_hora": "2025-12-31T23:00",
    "latitud": 4.710,
    "longitud": -74.072
  }'
```

Respuesta `201`:
```json
{
  "id": 5,
  "nombre": "La Resistencia Vol.4",
  "codigo_acceso": "XK3M9P",
  "mensaje": "Fiesta creada exitosamente."
}
```

### `GET /fiestas/` — Listar fiestas

```bash
curl http://127.0.0.1:8000/fiestas/ -H "Accept: application/json"
```

Respuesta `200`:
```json
{
  "fiestas": [
    {
      "id": 1,
      "nombre": "La Resistencia Vol.3",
      "direccion": "Carrera 13 #85-60, Bogotá",
      "latitud": 4.676,
      "longitud": -74.048,
      "capacidad": 40,
      "invitados_confirmados": 2,
      "cupos_disponibles": 38,
      "fecha_hora": "2025-12-15T03:00:00+00:00",
      "estado": "abierta",
      "codigo_acceso": "ABC123"
    }
  ]
}
```

---

## URLs de los frontends

### Frontend 1 — Invitados (`:8001` o `/invitados/`)

| URL | Descripción |
|-----|-------------|
| `/invitados/` | Portal — lista fiestas disponibles para solicitar |
| `/invitados/solicitar/<id>/` | Formulario de solicitud de ingreso |
| `/invitados/gestionar/<id>/` | Panel del organizador: confirmar/rechazar |
| `/invitados/confirmar/<id>/` | POST — confirmar invitado |
| `/invitados/rechazar/<id>/` | POST — rechazar invitado |

### Frontend 2 — Localización (`:8002` o `/localizacion/`)

| URL | Descripción |
|-----|-------------|
| `/localizacion/` | Radar — mapa interactivo con todas las fiestas |
| `/localizacion/<id>/` | Detalle de fiesta con mapa individual |

---

## Reglas de negocio implementadas

- Una fiesta debe tener fecha futura
- Capacidad entre 2 y 500 personas
- El código de acceso se genera automáticamente (único, 6 caracteres)
- Los alias de invitados son únicos por fiesta
- Al llenarse, la fiesta cambia automáticamente a estado `llena`
- No se pueden confirmar invitados si no hay cupo disponible

---

## Reset de datos

```bash
python scripts/setup.py --reset
# O:
make reset-db
```

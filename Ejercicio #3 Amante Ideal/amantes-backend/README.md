# 💕 Amantes Backend

API REST para encontrar tu amante ideal — Node.js + Express + MongoDB.

## Arquitectura en capas

```
src/
├── config/         → Configuración de BD
├── controllers/    → Manejo de requests HTTP
├── dtos/           → Validación y transformación de datos de entrada
├── models/         → Esquemas de Mongoose
├── repositories/   → Acceso a datos (CRUD)
├── routes/         → Definición de endpoints
├── seed/           → Datos iniciales automáticos
└── services/       → Lógica de negocio
```

## Requisitos

- Node.js >= 18
- MongoDB corriendo localmente en `mongodb://localhost:27017`

## Instalación

```bash
npm install
```

## Scripts

```bash
npm run dev    # Desarrollo con nodemon (hot reload)
npm run start  # Producción
```

## Endpoints

### POST /amantes
Crea un perfil de amante.

**Body:**
```json
{
  "nombre": "Ana",
  "edad": 25,
  "intereses": ["viajes", "música"],
  "descripcion": "Opcional"
}
```

### GET /amantes
Lista todos los amantes.

### GET /amantes?interes=viajes
Filtra amantes por interés.

## Seed

Al iniciar, si la BD está vacía se cargan automáticamente 8 perfiles de ejemplo.

# 💕 Amantes Frontend

Interfaz React (CSR) para el proyecto Amante Ideal.

## Estructura

```
src/
├── components/
│   ├── AmanteCard.jsx       → Tarjeta de perfil
│   ├── SearchBar.jsx        → Buscador con chips de intereses
│   └── CreateAmanteForm.jsx → Modal para crear perfil
├── hooks/
│   └── useAmantes.js        → Estado y lógica de negocio del cliente
├── pages/
│   └── HomePage.jsx         → Página principal
├── services/
│   └── amantes.service.js   → Capa HTTP (fetch al backend)
├── App.jsx
├── index.css
└── main.jsx
```

## Requisitos

- Node.js >= 18
- Backend corriendo en `http://localhost:3001`

## Instalación

```bash
npm install
```

## Scripts

```bash
npm run dev    # Desarrollo con Vite (hot reload) — http://localhost:5173
npm run build  # Build de producción
npm run start  # Preview del build — http://localhost:4173
```

## Proxy

Vite proxea `/amantes` → `http://localhost:3001` durante el desarrollo,
por lo que no es necesario configurar CORS en el frontend.

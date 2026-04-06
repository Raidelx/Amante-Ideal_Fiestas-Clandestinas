import React, { useState } from 'react';
import { useAmantes } from '../hooks/useAmantes';
import { AmanteCard } from '../components/AmanteCard';
import { SearchBar } from '../components/SearchBar';
import { CreateAmanteForm } from '../components/CreateAmanteForm';

export function HomePage() {
  const { amantes, loading, error, filtro, buscar, crear } = useAmantes();
  const [mostrarForm, setMostrarForm] = useState(false);

  return (
    <div className="page">
      {/* Header */}
      <header className="hero">
        <div className="hero-inner">
          <p className="hero-eyebrow">Encuentra tu</p>
          <h1 className="hero-title">Amante Ideal</h1>
          <p className="hero-sub">
            Perfiles únicos, intereses compartidos, conexiones reales.
          </p>
          <button
            className="btn btn-primary btn-lg"
            onClick={() => setMostrarForm(true)}
          >
            + Crear mi perfil
          </button>
        </div>
        <div className="hero-deco" aria-hidden="true">
          <span>💕</span><span>✨</span><span>🌹</span>
        </div>
      </header>

      {/* Búsqueda */}
      <main className="main">
        <SearchBar onBuscar={buscar} filtroActual={filtro} />

        {/* Resultados */}
        <div className="results-header">
          {filtro ? (
            <p className="results-info">
              Mostrando <strong>{amantes.length}</strong> resultado{amantes.length !== 1 ? 's' : ''}{' '}
              para <em>"{filtro}"</em>
            </p>
          ) : (
            <p className="results-info">
              <strong>{amantes.length}</strong> perfil{amantes.length !== 1 ? 'es' : ''} disponible{amantes.length !== 1 ? 's' : ''}
            </p>
          )}
        </div>

        {loading && (
          <div className="state-message">
            <div className="spinner" />
            <p>Buscando tu media naranja...</p>
          </div>
        )}

        {error && (
          <div className="alert alert-error">
            ⚠️ {error} — Asegúrate de que el backend está corriendo.
          </div>
        )}

        {!loading && !error && amantes.length === 0 && (
          <div className="state-message empty">
            <span className="empty-icon">💔</span>
            <p>No se encontraron perfiles{filtro ? ` con interés en "${filtro}"` : ''}.</p>
            <button className="btn btn-ghost" onClick={() => setMostrarForm(true)}>
              ¡Sé el primero!
            </button>
          </div>
        )}

        <div className="grid">
          {amantes.map((a) => (
            <AmanteCard key={a._id} amante={a} />
          ))}
        </div>
      </main>

      {/* Modal formulario */}
      {mostrarForm && (
        <CreateAmanteForm
          onCrear={crear}
          onClose={() => setMostrarForm(false)}
        />
      )}
    </div>
  );
}

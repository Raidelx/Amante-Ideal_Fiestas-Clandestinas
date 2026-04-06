import React, { useState } from 'react';

const INTERESES_SUGERIDOS = [
  'viajes', 'música', 'cocina', 'yoga',
  'libros', 'café', 'arte', 'fotografía',
  'deporte', 'tecnología',
];

export function SearchBar({ onBuscar, filtroActual }) {
  const [valor, setValor] = useState(filtroActual || '');

  const handleSubmit = (e) => {
    e.preventDefault();
    onBuscar(valor.trim());
  };

  const handleChip = (interes) => {
    const nuevo = filtroActual === interes ? '' : interes;
    setValor(nuevo);
    onBuscar(nuevo);
  };

  const handleLimpiar = () => {
    setValor('');
    onBuscar('');
  };

  return (
    <section className="search-section">
      <form className="search-form" onSubmit={handleSubmit}>
        <input
          className="search-input"
          type="text"
          placeholder="Buscar por interés..."
          value={valor}
          onChange={(e) => setValor(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">Buscar</button>
        {filtroActual && (
          <button type="button" className="btn btn-ghost" onClick={handleLimpiar}>
            Limpiar
          </button>
        )}
      </form>
      <div className="chips">
        {INTERESES_SUGERIDOS.map((i) => (
          <button
            key={i}
            className={`chip ${filtroActual === i ? 'chip-active' : ''}`}
            onClick={() => handleChip(i)}
            type="button"
          >
            {i}
          </button>
        ))}
      </div>
    </section>
  );
}

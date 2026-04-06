import React from 'react';

const INTERESES_EMOJIS = {
  viajes: '✈️',
  música: '🎵',
  musica: '🎵',
  cocina: '🍳',
  yoga: '🧘',
  libros: '📚',
  café: '☕',
  cafe: '☕',
  arte: '🎨',
  fotografía: '📷',
  fotografia: '📷',
  deporte: '🏃',
  tecnología: '💻',
  tecnologia: '💻',
};

const getEmoji = (interes) =>
  INTERESES_EMOJIS[interes.toLowerCase()] || '✨';

export function AmanteCard({ amante }) {
  const { nombre, edad, intereses, descripcion, avatar } = amante;

  return (
    <article className="card">
      <div className="card-avatar">
        {avatar ? (
          <img src={avatar} alt={nombre} />
        ) : (
          <div className="card-avatar-fallback">
            {nombre.charAt(0).toUpperCase()}
          </div>
        )}
      </div>
      <div className="card-body">
        <div className="card-header">
          <h3 className="card-name">{nombre}</h3>
          <span className="card-age">{edad} años</span>
        </div>
        {descripcion && <p className="card-desc">{descripcion}</p>}
        <ul className="card-tags">
          {intereses.map((i) => (
            <li key={i} className="tag">
              <span>{getEmoji(i)}</span> {i}
            </li>
          ))}
        </ul>
      </div>
    </article>
  );
}

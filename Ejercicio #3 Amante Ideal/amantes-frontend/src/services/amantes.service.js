const BASE_URL = '/amantes';

/**
 * Capa de servicio del frontend.
 * Abstrae las llamadas HTTP al backend.
 */
export const amantesService = {
  /**
   * Obtiene todos los amantes o filtra por interés.
   * @param {string} [interes]
   */
  async listar(interes = '') {
    const url = interes
      ? `${BASE_URL}?interes=${encodeURIComponent(interes)}`
      : BASE_URL;
    const res = await fetch(url);
    if (!res.ok) throw new Error('Error al obtener perfiles');
    return res.json();
  },

  /**
   * Crea un nuevo perfil de amante.
   * @param {Object} datos
   */
  async crear(datos) {
    const res = await fetch(BASE_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos),
    });
    return res.json();
  },
};

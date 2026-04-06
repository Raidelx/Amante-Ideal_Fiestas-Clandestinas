import { useState, useEffect, useCallback } from 'react';
import { amantesService } from '../services/amantes.service';

/**
 * Hook personalizado para gestionar el estado de amantes.
 */
export function useAmantes() {
  const [amantes, setAmantes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [filtro, setFiltro] = useState('');

  const listar = useCallback(async (interes = '') => {
    setLoading(true);
    setError(null);
    try {
      const res = await amantesService.listar(interes);
      setAmantes(res.data || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  const crear = async (datos) => {
    const res = await amantesService.crear(datos);
    if (res.ok) {
      await listar(filtro);
    }
    return res;
  };

  const buscar = (interes) => {
    setFiltro(interes);
    listar(interes);
  };

  useEffect(() => {
    listar();
  }, [listar]);

  return { amantes, loading, error, filtro, buscar, crear };
}

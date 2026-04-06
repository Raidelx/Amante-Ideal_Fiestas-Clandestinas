import React, { useState } from 'react';

const CAMPOS_INICIALES = {
  nombre: '',
  edad: '',
  intereses: '',
  descripcion: '',
};

export function CreateAmanteForm({ onCrear, onClose }) {
  const [campos, setCampos] = useState(CAMPOS_INICIALES);
  const [errores, setErrores] = useState([]);
  const [exito, setExito] = useState(false);
  const [cargando, setCargando] = useState(false);

  const handleChange = (e) => {
    setCampos({ ...campos, [e.target.name]: e.target.value });
    setErrores([]);
  };

  // Validación básica en cliente (espejo del DTO del backend)
  const validar = () => {
    const errs = [];
    if (!campos.nombre.trim() || campos.nombre.trim().length < 2)
      errs.push('El nombre debe tener al menos 2 caracteres.');
    const edad = Number(campos.edad);
    if (!campos.edad || !Number.isInteger(edad) || edad < 18 || edad > 100)
      errs.push('La edad debe ser un número entero entre 18 y 100.');
    const interesesArr = campos.intereses
      .split(',')
      .map((i) => i.trim())
      .filter(Boolean);
    if (interesesArr.length === 0)
      errs.push('Debes ingresar al menos un interés (separados por coma).');
    if (campos.descripcion.length > 300)
      errs.push('La descripción no puede superar 300 caracteres.');
    return errs;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const errs = validar();
    if (errs.length > 0) {
      setErrores(errs);
      return;
    }

    setCargando(true);
    const datos = {
      nombre: campos.nombre.trim(),
      edad: Number(campos.edad),
      intereses: campos.intereses.split(',').map((i) => i.trim()).filter(Boolean),
      descripcion: campos.descripcion.trim(),
    };

    try {
      const res = await onCrear(datos);
      if (res.ok) {
        setExito(true);
        setCampos(CAMPOS_INICIALES);
        setTimeout(() => {
          setExito(false);
          onClose();
        }, 1800);
      } else {
        setErrores(res.errors || ['Error al crear el perfil.']);
      }
    } catch {
      setErrores(['Error de conexión con el servidor.']);
    } finally {
      setCargando(false);
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <button className="modal-close" onClick={onClose} aria-label="Cerrar">✕</button>
        <h2 className="modal-title">Crear perfil 💕</h2>

        {exito && (
          <div className="alert alert-success">
            ¡Perfil creado exitosamente!
          </div>
        )}

        {errores.length > 0 && (
          <div className="alert alert-error">
            <ul>
              {errores.map((e, i) => <li key={i}>{e}</li>)}
            </ul>
          </div>
        )}

        <form className="form" onSubmit={handleSubmit} noValidate>
          <div className="form-group">
            <label>Nombre *</label>
            <input
              name="nombre"
              value={campos.nombre}
              onChange={handleChange}
              placeholder="Tu nombre"
              maxLength={50}
            />
          </div>

          <div className="form-group">
            <label>Edad *</label>
            <input
              name="edad"
              type="number"
              value={campos.edad}
              onChange={handleChange}
              placeholder="18 – 100"
              min={18}
              max={100}
            />
          </div>

          <div className="form-group">
            <label>Intereses * <small>(separados por coma)</small></label>
            <input
              name="intereses"
              value={campos.intereses}
              onChange={handleChange}
              placeholder="viajes, música, café"
            />
          </div>

          <div className="form-group">
            <label>Descripción <small>(opcional, máx. 300 caracteres)</small></label>
            <textarea
              name="descripcion"
              value={campos.descripcion}
              onChange={handleChange}
              placeholder="Cuéntanos un poco sobre ti..."
              rows={3}
              maxLength={300}
            />
            <small className="char-count">{campos.descripcion.length}/300</small>
          </div>

          <button type="submit" className="btn btn-primary btn-full" disabled={cargando}>
            {cargando ? 'Creando...' : 'Crear perfil'}
          </button>
        </form>
      </div>
    </div>
  );
}

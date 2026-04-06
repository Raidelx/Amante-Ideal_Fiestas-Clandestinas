/**
 * DTO (Data Transfer Object) para validar y transformar datos de entrada
 * de un perfil de amante.
 */

class CreateAmanteDTO {
  constructor({ nombre, edad, intereses, descripcion, avatar }) {
    this.nombre = nombre;
    this.edad = edad;
    this.intereses = intereses;
    this.descripcion = descripcion || '';
    this.avatar = avatar || '';
  }

  /**
   * Valida los datos del DTO.
   * @returns {{ valid: boolean, errors: string[] }}
   */
  validate() {
    const errors = [];

    // Nombre
    if (!this.nombre || typeof this.nombre !== 'string') {
      errors.push('El nombre es obligatorio y debe ser texto.');
    } else {
      const nombreTrim = this.nombre.trim();
      if (nombreTrim.length < 2) errors.push('El nombre debe tener al menos 2 caracteres.');
      if (nombreTrim.length > 50) errors.push('El nombre no puede superar 50 caracteres.');
    }

    // Edad
    const edadNum = Number(this.edad);
    if (this.edad === undefined || this.edad === null || this.edad === '') {
      errors.push('La edad es obligatoria.');
    } else if (!Number.isInteger(edadNum) || edadNum < 18 || edadNum > 100) {
      errors.push('La edad debe ser un número entero entre 18 y 100.');
    }

    // Intereses
    if (!this.intereses) {
      errors.push('Los intereses son obligatorios.');
    } else if (!Array.isArray(this.intereses)) {
      errors.push('Los intereses deben ser un arreglo de strings.');
    } else if (this.intereses.length === 0) {
      errors.push('Debe proporcionar al menos un interés.');
    } else {
      const invalidos = this.intereses.filter(
        (i) => typeof i !== 'string' || i.trim().length === 0
      );
      if (invalidos.length > 0) {
        errors.push('Todos los intereses deben ser strings no vacíos.');
      }
    }

    // Descripción (opcional)
    if (this.descripcion && this.descripcion.length > 300) {
      errors.push('La descripción no puede superar 300 caracteres.');
    }

    return { valid: errors.length === 0, errors };
  }

  /**
   * Retorna objeto sanitizado listo para persistir.
   */
  toEntity() {
    return {
      nombre: this.nombre.trim(),
      edad: Number(this.edad),
      intereses: this.intereses.map((i) => i.trim().toLowerCase()),
      descripcion: this.descripcion.trim(),
      avatar: this.avatar.trim(),
    };
  }
}

module.exports = { CreateAmanteDTO };

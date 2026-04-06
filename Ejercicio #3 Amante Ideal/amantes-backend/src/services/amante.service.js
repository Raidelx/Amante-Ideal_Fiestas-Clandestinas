const amanteRepository = require('../repositories/amante.repository');
const { CreateAmanteDTO } = require('../dtos/amante.dto');

/**
 * Servicio: lógica de negocio.
 * Orquesta validaciones, transformaciones y llamadas al repositorio.
 */
class AmanteService {
  /**
   * Crea un nuevo perfil de amante.
   * @param {Object} rawData - Datos crudos del request body.
   * @returns {Promise<{ success: boolean, data?: Document, errors?: string[] }>}
   */
  async crearAmante(rawData) {
    // 1. Construir y validar DTO
    const dto = new CreateAmanteDTO(rawData);
    const { valid, errors } = dto.validate();

    if (!valid) {
      return { success: false, errors };
    }

    // 2. Reglas de negocio adicionales
    const existe = await amanteRepository.existsByNombre(dto.nombre);
    if (existe) {
      return { success: false, errors: [`Ya existe un perfil con el nombre "${dto.nombre}".`] };
    }

    // 3. Persistir entidad
    const entity = dto.toEntity();
    const amante = await amanteRepository.create(entity);

    return { success: true, data: amante };
  }

  /**
   * Lista amantes por interés o todos si no se filtra.
   * @param {string|undefined} interes
   * @returns {Promise<Document[]>}
   */
  async listarAmantes(interes) {
    if (interes && interes.trim().length > 0) {
      return await amanteRepository.findByInteres(interes);
    }
    return await amanteRepository.findAll();
  }
}

module.exports = new AmanteService();

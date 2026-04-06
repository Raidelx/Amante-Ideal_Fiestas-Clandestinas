const Amante = require('../models/amante.model');

/**
 * Repositorio: capa de acceso a datos.
 * Solo interactúa con el modelo de Mongoose.
 */
class AmanteRepository {
  /**
   * Crea y guarda un nuevo amante en la base de datos.
   * @param {Object} data - Datos ya validados y sanitizados del DTO.
   * @returns {Promise<Document>}
   */
  async create(data) {
    const amante = new Amante(data);
    return await amante.save();
  }

  /**
   * Busca amantes cuyo arreglo de intereses contenga el interés dado.
   * La búsqueda es case-insensitive gracias al regex.
   * @param {string} interes
   * @returns {Promise<Document[]>}
   */
  async findByInteres(interes) {
    return await Amante.find({
      intereses: { $regex: new RegExp(`^${interes.trim()}$`, 'i') },
    }).sort({ createdAt: -1 });
  }

  /**
   * Retorna todos los amantes registrados.
   * @returns {Promise<Document[]>}
   */
  async findAll() {
    return await Amante.find().sort({ createdAt: -1 });
  }

  /**
   * Verifica si ya existe un perfil con ese nombre exacto.
   * @param {string} nombre
   * @returns {Promise<boolean>}
   */
  async existsByNombre(nombre) {
    const found = await Amante.findOne({
      nombre: { $regex: new RegExp(`^${nombre.trim()}$`, 'i') },
    });
    return !!found;
  }

  /**
   * Borra todos los documentos (usado solo por el seed).
   */
  async deleteAll() {
    return await Amante.deleteMany({});
  }

  /**
   * Inserta múltiples documentos de una vez (usado por el seed).
   * @param {Object[]} docs
   */
  async insertMany(docs) {
    return await Amante.insertMany(docs);
  }
}

module.exports = new AmanteRepository();

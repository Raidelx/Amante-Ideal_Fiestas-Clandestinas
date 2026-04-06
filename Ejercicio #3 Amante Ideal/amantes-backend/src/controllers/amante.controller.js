const amanteService = require('../services/amante.service');

/**
 * Controlador: maneja los requests HTTP y delega al servicio.
 */
class AmanteController {
  /**
   * POST /amantes
   * Crea un nuevo perfil de amante.
   */
  async crear(req, res) {
    try {
      const result = await amanteService.crearAmante(req.body);

      if (!result.success) {
        return res.status(400).json({
          ok: false,
          errors: result.errors,
        });
      }

      return res.status(201).json({
        ok: true,
        message: '¡Perfil creado exitosamente! 💕',
        data: result.data,
      });
    } catch (error) {
      console.error('[AmanteController.crear]', error);
      return res.status(500).json({
        ok: false,
        errors: ['Error interno del servidor.'],
      });
    }
  }

  /**
   * GET /amantes?interes=x
   * Lista amantes, filtrando por interés si se provee.
   */
  async listar(req, res) {
    try {
      const { interes } = req.query;
      const amantes = await amanteService.listarAmantes(interes);

      return res.status(200).json({
        ok: true,
        total: amantes.length,
        filtro: interes || null,
        data: amantes,
      });
    } catch (error) {
      console.error('[AmanteController.listar]', error);
      return res.status(500).json({
        ok: false,
        errors: ['Error interno del servidor.'],
      });
    }
  }
}

module.exports = new AmanteController();

const { Router } = require('express');
const amanteController = require('../controllers/amante.controller');

const router = Router();

router.post('/', (req, res) => amanteController.crear(req, res));
router.get('/', (req, res) => amanteController.listar(req, res));

module.exports = router;

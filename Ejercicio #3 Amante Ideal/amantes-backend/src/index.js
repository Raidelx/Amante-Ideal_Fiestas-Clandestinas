require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/database');
const amanteRoutes = require('./routes/amante.routes');
const runSeed = require('./seed/seed');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

app.use('/amantes', amanteRoutes);

app.get('/', (req, res) => {
  res.json({ ok: true, message: 'API Amantes funcionando correctamente' });
});

app.use((req, res) => {
  res.status(404).json({ ok: false, message: 'Ruta no encontrada' });
});

const start = async () => {
  await connectDB();
  await runSeed();
  app.listen(PORT, () => {
    console.log('Servidor corriendo en http://localhost:' + PORT);
  });
};

start();

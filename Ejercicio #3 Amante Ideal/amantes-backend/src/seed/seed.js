const amanteRepository = require('../repositories/amante.repository');

const seedData = [
  {
    nombre: 'Valentina',
    edad: 27,
    intereses: ['viajes', 'cocina', 'yoga'],
    descripcion: 'Amo explorar culturas nuevas y cocinar recetas del mundo. El yoga es mi zen diario.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Valentina',
  },
  {
    nombre: 'Sebastián',
    edad: 31,
    intereses: ['música', 'fotografía', 'viajes'],
    descripcion: 'Guitarrista de alma, fotógrafo de corazón. Siempre buscando la próxima aventura.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Sebastian',
  },
  {
    nombre: 'Camila',
    edad: 24,
    intereses: ['libros', 'café', 'yoga'],
    descripcion: 'Lectora empedernida. Me encontrarás en alguna cafetería con un libro y un flat white.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Camila',
  },
  {
    nombre: 'Andrés',
    edad: 29,
    intereses: ['deporte', 'cocina', 'música'],
    descripcion: 'Cocinero amateur y maratonista aficionado. La vida es mejor con buena comida y música.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Andres',
  },
  {
    nombre: 'Isabella',
    edad: 26,
    intereses: ['arte', 'viajes', 'fotografía'],
    descripcion: 'Pintora y viajera. Cada ciudad es un lienzo nuevo esperando ser explorado.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Isabella',
  },
  {
    nombre: 'Mateo',
    edad: 33,
    intereses: ['tecnología', 'deporte', 'libros'],
    descripcion: 'Desarrollador de día, ciclista de fin de semana. Apasionado por la ciencia ficción.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Mateo',
  },
  {
    nombre: 'Sofía',
    edad: 28,
    intereses: ['café', 'arte', 'música'],
    descripcion: 'Barista profesional y melómana. El jazz y el espresso son mi combinación perfecta.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Sofia',
  },
  {
    nombre: 'Diego',
    edad: 25,
    intereses: ['fotografía', 'deporte', 'viajes'],
    descripcion: 'Surfista y fotógrafo. Persigo olas y luz perfecta por todo el Pacífico.',
    avatar: 'https://api.dicebear.com/8.x/lorelei/svg?seed=Diego',
  },
];

const runSeed = async () => {
  try {
    const count = (await amanteRepository.findAll()).length;
    if (count > 0) {
      console.log(`🌱 Seed omitido: ya existen ${count} perfiles en la base de datos.`);
      return;
    }
    await amanteRepository.insertMany(seedData);
    console.log(`🌱 Seed completado: ${seedData.length} perfiles cargados.`);
  } catch (error) {
    console.error('❌ Error en seed:', error.message);
  }
};

module.exports = runSeed;

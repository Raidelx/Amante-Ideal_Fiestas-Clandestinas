const mongoose = require('mongoose');

const amanteSchema = new mongoose.Schema(
  {
    nombre: {
      type: String,
      required: [true, 'El nombre es obligatorio'],
      trim: true,
      minlength: [2, 'El nombre debe tener al menos 2 caracteres'],
      maxlength: [50, 'El nombre no puede superar 50 caracteres'],
    },
    edad: {
      type: Number,
      required: [true, 'La edad es obligatoria'],
      min: [18, 'Debe ser mayor de edad'],
      max: [100, 'Edad no válida'],
    },
    intereses: {
      type: [String],
      required: [true, 'Los intereses son obligatorios'],
      validate: {
        validator: (arr) => arr.length > 0,
        message: 'Debe tener al menos un interés',
      },
    },
    descripcion: {
      type: String,
      trim: true,
      maxlength: [300, 'La descripción no puede superar 300 caracteres'],
      default: '',
    },
    avatar: {
      type: String,
      default: '',
    },
  },
  {
    timestamps: true,
    versionKey: false,
  }
);

// Index para búsquedas por interés
amanteSchema.index({ intereses: 1 });

module.exports = mongoose.model('Amante', amanteSchema);

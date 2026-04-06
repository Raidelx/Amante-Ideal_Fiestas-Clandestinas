const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    const uri = process.env.MONGODB_URI || 'mongodb://localhost:27017/amantes_db';
    await mongoose.connect(uri);
    console.log('✅ MongoDB conectado:', uri);
  } catch (error) {
    console.error('❌ Error conectando MongoDB:', error.message);
    process.exit(1);
  }
};

module.exports = connectDB;

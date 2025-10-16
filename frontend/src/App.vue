<template>
  <div class="inscripcion-container">
    <h2>Inscríbete en el Sorteo de San Valentín</h2>
    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>

    <form @submit.prevent="handleSubmit" v-else>
      <div class="form-group">
        <label for="nombre">Nombre Completo</label>
        <input type="text" id="nombre" v-model="form.nombre_completo" required>
      </div>
      <div class="form-group">
        <label for="email">Correo Electrónico</label>
        <input type="email" id="email" v-model="form.email" required>
        <p v-if="errors.email" class="error-message">{{ errors.email }}</p>
      </div>
      <div class="form-group">
        <label for="telefono">Teléfono</label>
        <input type="tel" id="telefono" v-model="form.telefono" required>
      </div>
      <button type="submit" :disabled="loading">
        {{ loading ? 'Registrando...' : 'Participar Ahora' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/inscripcion/'; // Ajustar según puerto de Django

const form = ref({
  nombre_completo: '',
  email: '',
  telefono: ''
});

const errors = ref({});
const loading = ref(false);
const successMessage = ref('');

const handleSubmit = async () => {
  loading.value = true;
  errors.value = {};
  
  try {
    const response = await axios.post(API_URL, form.value);
    
    // Al finalizar, mostrar mensaje: "¡Gracias por registrarte! Revisa tu correo..." [cite: 41]
    successMessage.value = response.data.message; 

  } catch (error) {
    if (error.response && error.response.data) {
      // Manejo de errores de validación, especialmente el duplicado [cite: 40]
      if (error.response.data.email) {
        errors.value.email = error.response.data.email[0];
      }
      // Manejo de otros errores...
    } else {
      alert('Ocurrió un error inesperado al registrarse.');
    }
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* Estilos básicos para el formulario */
.inscripcion-container { max-width: 400px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; }
.form-group { margin-bottom: 15px; }
label { display: block; margin-bottom: 5px; font-weight: bold; }
input { width: 100%; padding: 10px; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px; }
button { padding: 10px 15px; background-color: #d9534f; color: white; border: none; border-radius: 4px; cursor: pointer; }
.error-message { color: red; font-size: 0.9em; margin-top: 5px; }
.success-message { color: green; font-weight: bold; padding: 15px; background-color: #e6ffe6; border-radius: 4px; }
</style>
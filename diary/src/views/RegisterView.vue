<template>
    <div>
      <h1>Регистрация</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">Имя пользователя:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Пароль:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { useAuthStore } from '../stores/auth.ts';
  
  const username = ref('');
  const password = ref('');
  const authStore = useAuthStore();
  
  const register = () => {
    console.log('Регистрация:', { username: username.value, password: password.value });
    // После успешной регистрации можно установить токен
    // authStore.setToken('ваш_токен');
  };
  </script>
  
  <style scoped>
  /* Добавьте стили для вашего компонента */
  </style>
<template>
    <div class="login-container">
      <h2>Вход</h2>
      <form @submit.prevent="login" class="login-form">
        <div class="form-group">
          <label for="username">Имя пользователя:<br></label>
          <input type="text" id="username" v-model="username" required class="form-input" />
        </div>
        <div class="form-group">
          <label for="password">Пароль:<br></label>
          <input type="password" id="password" v-model="password" required class="form-input" />
        </div>
        <button type="submit" class="submit-button">Войти</button>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </form>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  const username = ref('');
  const password = ref('');
  const errorMessage = ref('');
  
  const login = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username.value, password: password.value }),
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Ошибка при входе');
      }
  
      const data = await response.json();
      console.log(data); // Успешный вход
      // Здесь можно сохранить токен и перенаправить пользователя на страницу дневника
    } catch (error) {
      errorMessage.value = "Ошибочка вышла" // Отображение ошибки
    }
  };
  </script>
  
  <style scoped>
  /* Ваши стили */
  .error {
    color: red;
  }
  </style>
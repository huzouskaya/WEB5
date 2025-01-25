<template>
  <HeaderView />
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
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth.ts';
import HeaderView from '@/components/HeaderView.vue';

const username = ref('');
const password = ref('');
const authStore = useAuthStore();

const login = () => {
  console.log('Вход:', { username: username.value, password: password.value });
  // Здесь можно добавить логику для аутентификации
  // authStore.setToken('ваш_токен');
};
</script>

<style scoped>
.login-container {
  display: flex; /* Добавлено для центрирования содержимого */
  flex-direction: column; /* Вертикальное выравнивание */
  justify-content: center; /* Центрирование по вертикали */
  align-items: center; /* Центрирование по горизонтали */
  max-width: 400px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #084b47;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  background-color: rgba(77, 233, 225, 0.986);
  z-index: 3;
  margin-top: 80px;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #084b47;
}

.registration-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  margin-bottom: 5px;
  color: #084b47;
}

.form-input {
  color: #084b47;
  padding: 10px;
  border: 1px solid #084b47;
  border-radius: 4px;
  font-size: 16px;
}

.form-input:focus {
  border-color: rgba(77, 233, 225, 0.986);
  outline: none;
}

.submit-button {
  padding: 10px;
  background-color: #084b47;
  color: rgba(77, 233, 225, 0.986);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  /* align-items: center;
  justify-content: center; */
}

.submit-button:hover {
  background-color: rgba(17, 99, 95, 0.986);
}
</style>

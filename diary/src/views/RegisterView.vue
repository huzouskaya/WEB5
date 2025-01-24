<template>
  <HeaderView />
  <div class="registration-container">
    <h2>Регистрация</h2>
    <form @submit.prevent="register" class="registration-form">
      <div class="form-group">
        <label for="username">Имя пользователя:<br></label>
        <input type="text" id="username" v-model="username" required class="form-input" />
      </div>
      <div class="form-group">
        <label for="password">Пароль:<br></label>
        <input type="password" id="password" v-model="password" required class="form-input" />
      </div>
      <button type="submit" class="submit-button">Зарегистрироваться</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import HeaderView from '@/components/HeaderView.vue';

const username = ref('');
const password = ref('');
const errorMessage = ref('');

const isPasswordStrong = (password: string): boolean => {
  const minLength = 8; // Минимальная длина пароля
  const hasUpperCase = /[A-Z]/.test(password); // Наличие заглавной буквы
  const hasLowerCase = /[a-z]/.test(password); // Наличие строчной буквы
  const hasNumbers = /\d/.test(password); // Наличие цифр
  const hasSpecialChars = /[!@#$%^&*(),.?":{}|<>]/.test(password); // Наличие специальных символов

  return (
    password.length >= minLength &&
    hasUpperCase &&
    hasLowerCase &&
    hasNumbers &&
    hasSpecialChars
  );
};

const register = async () => {
  if (!isPasswordStrong(password.value)) {
    errorMessage.value = 'Пароль - минимум 8 символов (заглавные и строчные буквы, цифры и спецсимволы)';
    return; // Прерываем выполнение, если пароль не надежный
  }
  try {
    const response = await fetch('http://localhost:8000/api/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username: username.value, password: password.value }),
    });

    if (!response.ok) {
      throw new Error('Ошибка при регистрации');
    }

    const data = await response.json();
    console.log(data); // Успешная регистрация
    // Здесь можно перенаправить пользователя на страницу входа или дневника
  } catch (error) {
    errorMessage.value = 'Не удалось зарегистрироваться. Пожалуйста, проверьте правильность ввода.'; // Статическое сообщение
  }
};
</script>

<style scoped>
.registration-container {
  max-width: 280px;
  margin: 0 auto;
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
  font-weight: medium;
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
  font-weight: bold;
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
}

.submit-button:hover {
  background-color: rgba(17, 99, 95, 0.986);
}
</style>

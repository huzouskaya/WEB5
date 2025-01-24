<!-- src/components/Login.vue -->
<template>
  <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
      return {
          username: '',
          password: ''
      };
  },
  methods: {
      async login() {
          try {
              const response = await axios.post('http://localhost:8000/login/', {
                  username: this.username,
                  password: this.password
              });
              console.log('Login successful:', response.data);
              // Здесь вы можете сохранить токен или выполнить другие действия
          } catch (error) {
              console.error('Login error:', error.response.data);
          }
      }
  }
};
</script>



<!-- <template>
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
      console.log(data);
    } catch (error) {
      errorMessage.value = "Ошибочка вышла"
    }
  };
  </script>
  

  <style scoped>
  .login-container {
    display: flex; /* Добавлено для центрирования содержимого */
    flex-direction: column; /* Вертикальное выравнивание */
    justify-content: center; /* Центрирование по вертикали */
    align-items: center; /* Центрирование по горизонтали */
    max-width: 400px;
    margin: 20 auto;
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
    /* align-items: center;
    justify-content: center; */
  }

  .submit-button:hover {
    background-color: rgba(17, 99, 95, 0.986);
  }
  </style> -->

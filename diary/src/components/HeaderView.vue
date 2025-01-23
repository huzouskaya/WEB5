<template>
    <header class="header">
      <div class="logo">
        <img src="../assets/logo.png" alt="Личный дневник" />
        <h1>Личный дневник</h1>
      </div>
      <nav class="nav">
        <router-link to="/" class="nav-link">Главная</router-link>
        <router-link to="/diary" class="nav-link">Дневник</router-link>
        <template v-if="isAuthenticated">
          <router-link to="/entry-editor" class="nav-link">Создать запись</router-link>
        </template>
        <router-link to="/about" class="nav-link">О приложении</router-link>
      </nav>
      <div class="auth">
        <template v-if="isAuthenticated">
          <div class="profile">
            <img :src="userAvatar" alt="Аватар" class="avatar" />
            <span class="username">{{ username }}</span>
          </div>
          <button @click="logout" class="logout-button">Выйти</button>
        </template>
        <template v-else>
          <router-link to="/login" class="auth-link">Войти</router-link>
          <router-link to="/register" class="auth-link">Регистрация</router-link>
        </template>
      </div>
    </header>
  </template>
  
  <script setup lang="ts">
  import { computed } from 'vue';
  import { useAuthStore } from '../stores/auth'; // Импортируйте ваш store
  
  const authStore = useAuthStore();
  const isAuthenticated = computed(() => !!authStore.token);
  const username = computed(() => authStore.username || 'Пользователь'); // Получаем имя пользователя из store
  const userAvatar = computed(() => authStore.avatar || '../assets/default-avatar.png'); // Получаем аватар из store
  
  const logout = () => {
    authStore.logout();
  };
  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #084b47;
    color: rgba(77, 233, 225, 0.986);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
  }
  
  .logo {
    display: flex;
    align-items: center;
  }
  
  .logo img {
    width: 40px;
    height: 40px;
    margin-right: 10px;
  }
  
  .nav {
    display: flex;
    gap: 20px;
  }
  
  .nav-link {
    text-decoration: none;
    color: rgba(77, 233, 225, 0.986);
    transition: color 0.5s;
  }
  
  /* .nav-link:hover {
    color: rgba(17, 99, 95, 0.986);
  } */
  
  .auth {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  
  .profile {
    display: flex;
    align-items: center;
  }
  
  .avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-right: 5px;
  }
  
  .logout-button,
  .auth-link {
    background: none;
    border: none;
    color: rgba(77, 233, 225, 0.986); /* Цвет кнопки выхода и ссылок */
    cursor: pointer;
    text-decoration: underline;
  }
  </style>


<!-- <template>
    <header class="header">
      <div class="logo">
        <img src="../assets/logo.png" alt="Личный дневник" />
        <h1>Личный дневник</h1>
      </div>
      <nav class="nav">
        <router-link to="/" class="nav-link">Главная</router-link>
        <router-link to="/diary" class="nav-link">Дневник</router-link>
        <router-link to="/about" class="nav-link">О приложении</router-link>
      </nav>
      <div class="auth">
        <template v-if="isAuthenticated">
          <div class="profile">
            <img :src="userAvatar" alt="Аватар" class="avatar" />
            <span class="username">{{ username }}</span>
          </div>
          <button @click="logout" class="logout-button">Выйти</button>
        </template>
        <template v-else>
          <router-link to="/login" class="auth-link">Войти</router-link>
          <router-link to="/register" class="auth-link">Регистрация</router-link>
        </template>
      </div>
    </header>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { useAuthStore } from '../stores/auth';
  
  const authStore = useAuthStore();
  const isAuthenticated = ref(!!authStore.token);
  const username = ref(authStore.username || 'Пользователь');
  const userAvatar = ref(authStore.avatar || '../assets/default-avatar.png');
  
  const logout = () => {
    authStore.logout(); // Сброс токена
    // Дополнительная логика выхода, если необходимо
  };
  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #f8f9fa;
    border-bottom: 1px solid #ddd;
  }
  
  .logo {
    display: flex;
    align-items: center;
  }
  
  .logo img {
    width: 40px; /* Размер логотипа */
    height: 40px;
    margin-right: 10px;
  }
  
  .nav {
    display: flex;
    gap: 20px;
  }
  
  .nav-link {
    text-decoration: none;
    color: #007bff;
  }
  
  .auth {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  
  .profile {
    display: flex;
    align-items: center;
  }
  
  .avatar {
    width: 30px; /* Размер аватара */
    height: 30px;
    border-radius: 50%;
    margin-right: 5px;
  }
  
  .logout-button,
  .auth-link {
    background: none;
    border: none;
    color: #007bff;
    cursor: pointer;
    text-decoration: underline;
  }
  </style> -->
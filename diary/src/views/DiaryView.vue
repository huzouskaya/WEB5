<template>
    <div class="diary">
      <h2>Мой Дневник</h2>
      <template v-if=1 >
        <!-- "isAuthenticated" -->
        <div v-if="entries.length === 0">
          <p>У вас пока нет записей. Создайте первую запись!</p>
        </div>
        <ul v-else>
          <!-- <li v-for="entry in entries" :key="entry.id" class="entry">
            <h3>{{ entry.title }}</h3>
            <p>{{ entry.content }}</p>
            <p><small>Создано: {{ formatDate(entry.createdAt) }}</small></p>
            <router-link :to="`/entry/${entry.id}`" class="view-link">Просмотреть</router-link>
          </li> -->
        </ul>
      </template>
      <template v-else>
        <p>Пожалуйста, <router-link to="/login">войдите</router-link>, чтобы увидеть ваши записи.</p>
      </template>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useAuthStore } from '../stores/auth.ts';
  import { useRouter } from 'vue-router';
  
  const authStore = useAuthStore();
  const router = useRouter();
  
//   const isAuthenticated = authStore.isAuthenticated;
  const entries = ref([]);
  
  // Функция для получения записей
  const fetchEntries = async () => {
    // Здесь вы можете сделать запрос к вашему API для получения записей
    // Пример:
    // const response = await fetch('/api/entries');
    // entries.value = await response.json();
  
    // Для примера, добавим статические данные
    entries.value = [
    //   { id: 1, title: 'Первая запись', content: 'Это содержимое первой записи.', createdAt: new Date() },
    //   { id: 2, title: 'Вторая запись', content: 'Это содержимое второй записи.', createdAt: new Date() },
    ];
  };
  
//   // Перенаправление на страницу входа, если пользователь не аутентифицирован
//   if (!isAuthenticated) {
//     router.push('/login');
//   }
  
//   // Получение записей при монтировании компонента
//   onMounted(() => {
//     if (isAuthenticated) {
//       fetchEntries();
//     }
//   });
  
//   // Функция для форматирования даты
//   const formatDate = (date) => {
//     return new Date(date).toLocaleDateString();
//   };
  </script>
  
  <style scoped>
  .diary {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .entry {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .view-link {
    color: #007bff;
    text-decoration: none;
  }
  
  .view-link:hover {
    text-decoration: underline;
  }
  </style>
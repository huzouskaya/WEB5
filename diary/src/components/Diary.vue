<template>
  <div class="diary">
    <h2>Мой Дневник</h2>
    <ul>
      <li v-for="entry in entries" :key="entry.id">
        <h3>{{ entry.title }}</h3>
        <p>{{ entry.content }}</p>
      </li>
    </ul>
    <p v-if="entries.length === 0">У вас пока нет записей.</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth.ts';
import { useRouter } from 'vue-router';

interface Entry {
  id: number;
  title: string;
  content: string;
}

const authStore = useAuthStore();
const router = useRouter();
const entries = ref<Entry[]>([]); // Объявляем entries как массив объектов типа Entry

// Проверка аутентификации
if (!authStore.isAuthenticated) {
  router.push('/login');
}

// Функция для получения записей
const fetchEntries = async () => {
  try {
    const response = await fetch('/api/entries/');
    if (!response.ok) {
      throw new Error('Ошибка при получении записей');
    }
    entries.value = await response.json();
  } catch (error) {
    console.error('Ошибка:', error);
  }
};

// Получение записей при монтировании компонента
onMounted(() => {
  fetchEntries();
});
</script>

<style scoped>
.diary {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
</style>
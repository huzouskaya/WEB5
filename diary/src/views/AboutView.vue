<template>
  <div class="about">
    <HeaderView />
    <div class="about-content">
      <h2>О нас</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
        ea commodo consequat.
      </p>
      <p>
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import HeaderView from '@/components/HeaderView.vue';
</script>

<style>
.about {
  min-height: 100vh; /* Занимает всю высоту экрана */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* Центрирование содержимого */
  background-color: #e0f7fa; /* Неброский светлый фон */
  padding: 20px; /* Отступы */
}

.about-content {
  max-width: 800px; /* Максимальная ширина контента */
  text-align: center; /* Центрирование текста */
  background-color: rgba(255, 255, 255, 0.9); /* Полупрозрачный белый фон для контента */
  border-radius: 8px; /* Закругление углов */
  padding: 40px; /* Внутренние отступы */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Тень для выделения */
  margin: 20px; /* Отступы вокруг контента */
}

h2 {
  font-size: 2.5rem; /* Размер заголовка */
  margin-bottom: 20px;
  color: #00796b; /* Цвет заголовка */
}

p {
  font-size: 1.2rem; /* Размер текста */
  line-height: 1.6; /* Межстрочный интервал */
  color: #333; /* Цвет текста */
}

@media (min-width: 1024px) {
  .about {
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
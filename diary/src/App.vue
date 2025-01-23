<template>
  <head>
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" /> 
  </head>
  <div class="app-container">
    <FullBackground /> <!-- Компонент фона -->
    <router-view /> <!-- Здесь будут отображаться ваши маршруты -->
  </div>
</template>

<script setup lang="ts">
import FullBackground from './components/FullBackground.vue'; // Импортируем компонент фона
</script>

<style>
.app-container {
  position: relative; /* Убедитесь, что контейнер имеет относительное позиционирование */
  min-height: 100vh; /* Убедитесь, что контейнер занимает всю высоту экрана */
  z-index: 1; /* Убедитесь, что контейнер находится поверх фона */
}
</style>
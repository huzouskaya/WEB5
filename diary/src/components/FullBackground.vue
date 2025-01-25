<template>
    <div class="full-background">
      <slot></slot> <!-- Позволяет вставлять другие компоненты или элементы внутрь -->
    </div>
  </template>
  
  <script setup lang="ts">
  // Здесь можно добавить логику, если нужно
  </script>
  
  <style scoped>
  .full-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(104, 211, 188, 0.986);
    background-image: url('@/assets/pattern.jpg'); 
    background-size: cover;
    background-position: center;
    opacity: 0.5;
    background-color: rgba(104, 211, 188, 0.5);
    z-index: -1;
  }
  </style>
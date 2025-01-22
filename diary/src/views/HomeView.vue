<template>
  <main class="home-view">
    <HeaderView />
    <header class="home-header">
      
      <h1>Добро пожаловать на наш сайт!</h1>
      <p>Здесь вы найдете множество интересного контента.</p>
    </header>
    <!-- <TheWelcome /> -->
    <section class="home-content">
      <h2>Что мы предлагаем</h2>
      <ul>
        <li>Информативные статьи</li>
        <li>Полезные советы</li>
        <li>Сообщество единомышленников</li>
      </ul>
    </section>
  </main>
</template>

<script setup lang="ts">
import HeaderView from '@/components/HeaderView.vue';
import TheWelcome from '../components/TheWelcome.vue'
</script>

<style scoped>
.home-view {
  padding: 20px;
  text-align: center;
}

.home-header {
  margin-bottom: 20px;
}

.home-content {
  margin-top: 30px;
}
</style>
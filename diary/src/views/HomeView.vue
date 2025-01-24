<template>
  <main class="home-view">
    <HeaderView />
    <header class="home-header">
      <h1 class="on_light">Добро пожаловать в приложение "Личный Дневник"!</h1>
    </header>
    <!-- <TheWelcome /> -->
    <div class="container">
      <p>Здесь вы можете записывать свои мысли, идеи и события из жизни. Это простое и удобное место для того, чтобы делиться своими переживаниями и отслеживать свои эмоции.
      <section class="home-content">
        <h2>Как это работает?</h2>
        <ul>
          <li>Записи:</li> Легко добавляйте новые записи, чтобы не забыть важные моменты.
          <li>Организация:</li> Удобный интерфейс поможет вам быстро находить нужные записи.
          <li>Безопасность:</li> Все ваши записи хранятся в защищенном облаке, доступ к которому есть только у вас.
        </ul>
      </section>
      Зачем вести дневник?
      Ведение дневника помогает лучше понять себя, справляться с эмоциями и фиксировать свои достижения. Это отличный способ для саморефлексии и личного роста.
      Попробуйте "Личный Дневник" и начните записывать свои мысли уже когда-нибудь завтра!</p>
    </div>
  </main>
</template>

<script setup lang="ts">
import HeaderView from '@/components/HeaderView.vue';
import TheWelcome from '../components/TheWelcome.vue'
</script>

<style scoped>
.container {
  color: #002519;
  font-size: 20px;
  background-color: rgb(175, 255, 235);
  padding: 5%;
  max-width: 90vw;
  min-width: 60vw;
  font-weight: 400;
}

.on_light {
  color: black;
  font-weight: bold;
  background-color: rgb(193, 221, 212);
}

.home-view {
  padding: 20px;
  text-align: center;
}

.home-header {
  margin-top: 80px;
  margin-bottom: 30px;
}

.home-content {
  margin-top: 50px;
}
</style>
<template>
  <div id="app">
    <Diary />
  </div>
</template>

<script>
import Diary from "./components/Diary.vue"; // Импортируем компонент Diary

export default {
  name: "App",
  components: {
    Diary, // Используем компонент Diary
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<template>
  <head>
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" /> 
  </head>
  <div class="app-container">
    <FullBackground />
    <router-view /> 
  </div>
</template>

<script setup lang="ts">
import FullBackground from './components/FullBackground.vue';
</script>

<style>
.app-container {
  position: relative;
  min-height: 100vh;
  z-index: 1;
}
</style>
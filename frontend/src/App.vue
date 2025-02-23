<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Análisis de Sentimientos</h1>
    <!-- Se despliega la vista principal -->
    <HomeView />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import HomeView from './views/HomeView.vue'

export default defineComponent({
  name: 'App',
  components: { HomeView }
})
</script>

<style>
/* Estilos globales personalizados */
</style> 
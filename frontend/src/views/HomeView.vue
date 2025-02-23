<template>
  <div>
    <h2 class="text-2xl font-bold mb-2">Opiniones Analizadas</h2>
    <div v-if="opiniones.length === 0">Cargando opiniones...</div>
    <ReviewCard v-for="op in opiniones" :key="op.id" :opinion="op" />
    
    <h2 class="text-2xl font-bold mt-8 mb-2">Trending Topics</h2>
    <div v-if="trendingList.length === 0">Cargando trending topics...</div>
    <TrendingCard v-for="trend in trendingList" :key="trend.id" :trending="trend" />
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import ReviewCard from '../components/ReviewCard.vue'
import TrendingCard from '../components/TrendingCard.vue'
import apiService from '../services/apiService'
import { Opinion } from '../models/Opinion'
import { Trending } from '../models/Trending'

export default defineComponent({
  name: 'HomeView',
  components: {
    ReviewCard,
    TrendingCard
  },
  setup() {
    const opiniones = ref<Opinion[]>([])
    const trendingList = ref<Trending[]>([])

    const cargarDatos = async () => {
      try {
        opiniones.value = await apiService.getOpiniones()
        trendingList.value = await apiService.getTrending()
      } catch (error) {
        console.error("Error al cargar los datos", error)
      }
    }

    onMounted(() => {
      cargarDatos()
    })

    return { opiniones, trendingList }
  }
})
</script> 
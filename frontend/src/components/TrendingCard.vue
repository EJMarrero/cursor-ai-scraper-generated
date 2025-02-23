<template>
  <div class="bg-blue-100 shadow-md rounded p-4 mb-4">
    <a :href="trending.url" target="_blank" class="text-blue-800 font-semibold hover:underline">
      {{ trending.topic }}
    </a>
    <p class="text-xs text-blue-600 mt-1">Obtenido: {{ trending.obtenido_en }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Trending } from '../models/Trending'

export default defineComponent({
  name: 'TrendingCard',
  props: {
    trending: {
      type: Object as PropType<Trending>,
      required: true
    }
  }
})
</script> 
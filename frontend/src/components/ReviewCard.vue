<template>
  <div class="bg-white shadow-md rounded p-4 mb-4">
    <p class="text-gray-700">{{ opinion.texto }}</p>
    <p class="text-sm text-gray-500 mt-2">Sentimiento: {{ opinion.sentimiento }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Opinion } from '../models/Opinion'

export default defineComponent({
  name: 'ReviewCard',
  props: {
    opinion: {
      type: Object as PropType<Opinion>,
      required: true
    }
  }
})
</script> 
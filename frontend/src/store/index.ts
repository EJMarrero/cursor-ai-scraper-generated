import { defineStore } from 'pinia'
import apiService from '../services/apiService'
import { Opinion } from '../models/Opinion'
import { Trending } from '../models/Trending'

export const useDataStore = defineStore('dataStore', {
  state: () => ({
    opiniones: [] as Opinion[],
    trending: [] as Trending[]
  }),
  actions: {
    async fetchOpiniones() {
      this.opiniones = await apiService.getOpiniones()
    },
    async fetchTrending() {
      this.trending = await apiService.getTrending()
    }
  }
}) 
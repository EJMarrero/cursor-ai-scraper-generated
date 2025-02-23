import axios from 'axios'
import { Opinion } from '../models/Opinion'
import { Trending } from '../models/Trending'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:3000/api'

export default {
  async getOpiniones(): Promise<Opinion[]> {
    try {
      const response = await axios.get(`${API_URL}/opiniones`)
      return response.data
    } catch (error) {
      console.error('Error al obtener opiniones:', error)
      return []
    }
  },
  async getTrending(): Promise<Trending[]> {
    try {
      const response = await axios.get(`${API_URL}/trending`)
      return response.data
    } catch (error) {
      console.error('Error al obtener trending topics:', error)
      return []
    }
  }
} 
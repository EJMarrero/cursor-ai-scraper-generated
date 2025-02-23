import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import '../index.css' // Actualizado para buscar index.css en la carpeta superior

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.mount('#app') 
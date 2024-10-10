import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Import Vuetify
import { createVuetify } from 'vuetify'
// Import Vuetify styles
import 'vuetify/styles'
// Import any Vuetify icons you plan to use (optional)
import { aliases, mdi } from 'vuetify/lib/iconsets/mdi-svg'

// Vuetify instance
const vuetify = createVuetify({
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
})

createApp(App).use(router, vuetify).mount('#app')

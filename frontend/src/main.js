import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import './registerServiceWorker'
import VueLocalStorage from 'vue-localstorage'
import '@mdi/font/css/materialdesignicons.css'

Vue.use(VueLocalStorage)

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')

import Vue from 'vue'
import App from './App.vue'
import store from "./store";
import VueCookies from 'vue-cookies'

require('./assets/droiche.css')
require('./assets/buttons.css')

Vue.config.productionTip = false;

Vue.use(VueCookies)
Vue.$cookies.config('30d')

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')

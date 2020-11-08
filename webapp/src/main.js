import Vue from 'vue'
import App from './App.vue'
import store from "./store";
require('./assets/droiche.css')
require('./assets/buttons.css')

Vue.config.productionTip = false;

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')

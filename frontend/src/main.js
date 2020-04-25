import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Login from './views/Login.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)

// const Scanner = { template: '<div>Scanner</div>' }
// const Shop = { template: '<div>Shop</div>' }
// const Rating = { template: '<div>Rating</div>' }

const routes = [
  { path: '/', component: Login },
  // { path: '/scanner', component: Scanner },
  // { path: '/shop', component: Shop },
  // { path: '/rating', component: Rating },
]

new Vue({
  render: h => h(App),
  router: new VueRouter({mode: 'history', routes})
}).$mount('#app')

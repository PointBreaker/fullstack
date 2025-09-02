import Vue from 'vue'
import App from './App.vue'
import router from './router'

// 引入Element UI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 引入axios
import axios from 'axios'

Vue.use(ElementUI)

// 配置axios
axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
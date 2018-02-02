// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import BaiduMap from "vue-baidu-map"
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import store from "./store"

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(BaiduMap, {
  ak:"IHDSKwmhHQgLvr5wZwCsZUuHyt6Thv3A"
})

/* eslint-disable no-new */
export default new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: { App }
})

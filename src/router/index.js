import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)


import app from "../views/app/app.vue"
import head from "../views/head/head.vue"
import index from "../views/index/index.vue"
import home from "../views/home/home.vue"
import footer from "../views/footer/footer.vue"
import list from "../views/list/list.vue"

import merc_detail from "../views/merc_detail/merc_detail.vue"
import shopping_card from "../views/shopping_card/shopping_card.vue"

import top from "../views/reg_login/top.vue"
import main from "../views/reg_login/main.vue"
import login from "../views/reg_login/login.vue"
import registry from "../views/reg_login/registry.vue"

import test from "../test/test.vue"

var router = new Router({
  routes: [
    {
      path: '/app',
      name: 'app',
      component: app,
      children: [
        {
          path: "home",
          components: {
            head: head,
            home: home,
            footer: footer
          },
          children: [
            {
              path: "index",
              name: "index",
              component: index,
              meta: {
                title: "首页"
              }
            },
            {
              path: "list",
              name: "list",
              component: list,
              meta: {
                  titie: "列表"
              }
            },
            {
              path: "merc-detail",
              name: "merc-detail",
              component: merc_detail,
              meta: {
                  titie: "商品详情"
              }
            }
          ]
        },
        {
          path: "main",
          name: "main",
          components: {
            head: top,
            home: main,
            footer: footer
          },
          children: [
            {
              path: "login",
              name: "login",
              component: login
            },
            {
              path: "registry",
              name: "registry",
              component: registry
            }
          ]
        }
      ]
    },{
      path: "/test",
      name: "test",
      component: test
    },{
          path: "/shopping-card",
          name: "shopping-card",
          component: shopping_card
        }
  ]
})
// router.beforeEach((from, to, next) => {
//
//   console.log(to)
//   if(to.path == "/"){
//     next({
//       path: "/app/home/index"
//     })
//   }
// })


export default router

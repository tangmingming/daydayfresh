<template>
  <div>
    <div style="height: 34px; line-height: 34px; border-bottom: 1px solid #e5e5e5; background-color: #f5f5f5;">
      <ul style="list-style-type: none; font-size: 15px; width:1200px; margin: 0">
        <li style="float: left; margin: 0px 5px;"><router-link to="" v-if="username" >{{ username }}</router-link><router-link v-else :to="{name: 'login'}">登录</router-link></li>
        <li style="float: left; margin: 0px 5px;">|</li>
        <li style="float: left; margin: 0px 5px;"><a v-if="username" @click="logout" >退出</a><router-link v-else to="router">注册</router-link></li>
        <li style="float: right">
          <el-dropdown size="small">
            <span class="el-dropdown-link">
              下拉菜单<i class="el-icon-arrow-down el-icon--right"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item style="font-size: 15px">黄金糕</el-dropdown-item>
              <el-dropdown-item style="font-size: 15px">黄金糕</el-dropdown-item>
              <el-dropdown-item style="font-size: 15px">黄金糕</el-dropdown-item>
              <el-dropdown-item>狮子头</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </li>
      </ul>
    </div>
    <div style="margin: 0 auto; width: 1200px;">
      <div style="float: left; width: 33%">
        <img src="../../static/images/head/logo.gif">
      </div>
      <div style="width: 400px; margin: auto; float: left; width: 33%">
        <el-input style="border: 2px solid green" placeholder="请输入内容" v-model="search_content" @keyup.enter.native="start_search()">
          <el-button slot="append" icon="el-icon-search" @click="start_search()"></el-button>
        </el-input>
        <ul style="margin: 0px; padding-left: 0px;">
          <router-link to="search">热搜榜:</router-link>
          <router-link to="search">啤酒</router-link>
          <router-link to="search">啤酒</router-link>
          <router-link to="search">啤酒</router-link>
        </ul>
      </div>
      <div style="float: left; width: 33%">
        <div style="width: 33%; float: right; text-align: right">正品保障</div>
        <div style="width: 33%; float: right; text-align: right">30退换货</div>
        <div style="width: 33%; float: right; text-align: right">满99包邮</div>
      </div>
    </div>
    <div style="clear: both"></div>
    <div style="background-color: black">
      <div style="width: 1200px; margin: auto">
        <el-menu
          class="el-menu-demo"
          mode="horizontal"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-submenu index="1">
            <template slot="title">我的工作台</template>
            <el-menu-item v-for="item in classes" :key="item.id" index="" @click="jump_list_by_classi('classi_id', item.id)">
              {{item.name}}
            </el-menu-item>
          </el-submenu>
          <el-menu-item v-for="item in classes" :key="item.id" index="item.id">
            <router-link :to="{name: 'list', query:{classi_id: item.id}}" tag="li" replace>{{ item.name }}</router-link>
          </el-menu-item>
          <el-menu-item style="float: right; margin: 0 30px" index="3">
            <shop_card_2></shop_card_2>
          </el-menu-item>
        </el-menu>
      </div>
    </div>

  </div>
</template>

<script>
  import shop_cart_2 from "./shop_card.vue"
  import primary from "../../api/primary.js"
  //  import ElMenuItem from "../../../node_modules/element-ui/packages/menu/src/menu-item.vue";

  export default {
    data: ()=>{
      return {
        classes: [
          {
            id: "1",
            name: "test-1",
          }
        ],
        search_content: ""
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log("key:"+key)
        console.log("keyPath："+keyPath)
      },
      logout() {
        this.$store.commit("logout")
      },
      over(){
        console.log("mouseover")
      },
      out(){
        console.log("out")
      },
      print_classes(){
        console.log(this.classes)
      },
      get_classification(){
        var self = this
        primary.get("classification").then(function (response) {
          self.classes = response.data
        })
      },
      jump_list_by_classi(value){
        this.$router.push({"name": "list", query: {classi: value}})
      },
      jump_list_by_search(value){
        this.$router.push({"name": "list", query: {search: value}})
      },
      start_search(){
        console.log(this.search_content)
        if(!this.search_content){
          this.$message('请输入搜索内容')
          return
        }
        this.jump_list_by_search(this.search_content)
      }
    },
    components: {
      shop_card_2: shop_cart_2
    },
    computed: {
      username: function (){
        return this.$store.state.username
      }
    },
    mounted: function () {
      var self = this
      primary.get("classification").then(function (response) {
        self.classes = response.data
        console.log("get classification")
      })
    }
  }
</script>

<style scoped>

</style>

<template>
  <div>
    <div style="height: 34px; line-height: 34px; border-bottom: 1px solid #e5e5e5; background-color: #f5f5f5;">
      <ul style="list-style-type: none; font-size: 15px; width:1200px">
        <li style="float: left; margin: 0px 5px;"><router-link to="router">登录</router-link></li>
        <li style="float: left; margin: 0px 5px;">|</li>
        <li style="float: left; margin: 0px 5px;"><router-link to="router">登录</router-link></li>
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
    <div style="margin: 30px auto; width: 1200px;">
      <div style="float: left; width: 33%">
        <img src="../../static/images/head/logo.gif">
      </div>
      <div style="width: 400px; margin: auto; float: left; width: 33%">
        <el-input style="border: 2px solid green" placeholder="请输入内容">
          <template slot="append" style="background: green; color: green">搜索</template>
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
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-submenu index="1">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
          </el-submenu>
          <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
          <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
          <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
          <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
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

  export default {
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    },
    components: {
      shop_card_2: shop_cart_2
    }
  }
</script>

<style scoped>

</style>

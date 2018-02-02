<template>
  <div style="width: 1200px; margin: 0 auto">
    <el-breadcrumb separator="/" style="margin: 20px">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>活动管理</el-breadcrumb-item>
      <el-breadcrumb-item>活动列表</el-breadcrumb-item>
      <el-breadcrumb-item>活动详情</el-breadcrumb-item>
    </el-breadcrumb>
    <div>
      <div style="float: left;">
        <el-card style="width: 220px">
          <div slot="header" class="clearfix">
            <span>卡片名称</span>
            <el-button style="float: right; padding: 3px 0" type="text" @click="test()">操作按钮</el-button>
          </div>
          <el-tree
            :data="classi_datas"
            :expand-on-click-node="false"
            @node-click="handleNodeClick">
          </el-tree>
        </el-card>
      </div>
      <div style="float: left; width: 960px">
        <el-card>
          <ul>
            <li style="float: left">价格</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(1,24)">1-24</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(15,20)">1-24</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(25,50)">1-24</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(50,100)">1-24</li>
            <li  style="float: left" ><input/>-<input/><button>确定</button></li>
          </ul>
        </el-card>
        <el-card style="">
          <a style="font-size: 12px">综合</a>
          <a style="font-size: 12px">综合</a>
          <a style="font-size: 12px">综合</a>
        </el-card>
        <div style="float: left; width: 226px; margin: 7px"  v-for="item of merchandises">
          <el-card :body-style="{ padding: '0px' }">
            <router-link :to="{name: 'merc-detail', query: {id: item.id}}" style="">
            <img style="width: 226px; height: 226px" v-bind:src="item.front_cover_img">
              <p style="height: 46px; margin: 2px 0px; overflow: hidden; font-size: 14px;"><span style="color:red; font-size: 18px">￥{{ item.sale_price }} </span>{{ item.name }}</p>
            </router-link>
            <p style="font-size: 12px; color: #888888; margin: 0">销量：{{ item.sales_numm }}</p>
          </el-card>
        </div>
      </div>
      <div class="block;" style="float: right">
        <el-pagination
          background
          @current-change="handle_current_change"
          layout="prev, pager, next"
          :total="page_count">
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
  import primary from "@/api/primary"

  export default {
    data() {
      return {
        classi_datas: [],
        page_is_search: true,
        merchandises: [],

        page: 1,
        page_size: 12,
        max_market_price: "",
        min_market_price: "",
        subclass: "",
        ordering: "",

        count: 0,
        page_count: 0
      }
    },
    methods: {
      handle_current_change(data){
        this.page = data
        this.get_merchandises()
      },
      handleNodeClick(data) {
        this.$router.push({name: "list", query: {classi_id: data.id}})
      },
      filter_price(min, max){
        console.log(min, max)
      },
      get_merchandises(){
        var url = `merchandise?page=${this.page}&page_size=${this.page_size}&max_market_price=${this.max_market_price}&min_market_price=${this.min_market_price}&subclass=${this.subclass}&ordering=${this.ordering}&search=${this.search}`
        var self = this
        primary.get(url).then(function (response) {
          self.merchandises = response.data.results
          self.count = response.data.count
        })
        this.page_count = this.count/this.page_size
        if(this.count % this.page_size == 0){
          this.page_count += 1
        }
        if(!this.merchandises.length){
          this.$notify({
            title: '警告',
            message: '没有相关商品',
            type: 'warning'
          });
        }
      },
      test(){
        console.log(this.classi_datas)
      }
    },
    mounted(){
      function dict_tree(datas){
        var ret = []
        for(let i of datas){
          if(i.childs){
            ret.push({
              id: i.id,
              label: i.name,
              children: dict_tree(i.childs)
            })
            continue
          }
          ret.push({
            id: i.id,
            label: i.name
          })
        }
        return ret
      }
      var self = this
      primary.get("classification").then(function (response) {
        console.log(response)
        self.classi_datas = dict_tree(response.data)
      })
    },
    updated(){
      console.log("updated")
    },
    beforupdate(){
      console.log("beforupdate")
    },
//    beforeRouteUpdate (to, from, next) {
//      // react to route changes...
//      // don't forget to call next()
//      console.log("beforRouterUpdate")
//    }
    watch: {
      '$route' (to, from) {
        if(this.$route.query.search){
          this.subclass = ""
          this.search = this.$route.query.search
          this.page = 1
        }else if(this.$route.query.classi_id){
          this.search = ""
          this.subclass = this.$route.query.classi_id
          this.page = 1
        }else{
          this.search = ""
          this.subclass = ""
          this.page = 1
        }
        this.get_merchandises()
        console.log("watch")
      }
    }
  };
</script>

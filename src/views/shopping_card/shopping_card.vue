<template>
  <div>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1">处理中心</el-menu-item>

      <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>

      <el-menu-item index="4">
      </el-menu-item>
      <el-steps :active="1" finish-status="success" simple style="margin-top: 20px">
        <el-step title="步骤 1" ></el-step>
        <el-step title="步骤 2" ></el-step>
        <el-step title="步骤 3" ></el-step>
      </el-steps>
    </el-menu>

    <div style="width: 1200px; margin: 0 auto">
      <div>
        <router-link :to="{name: 'index'}"><el-button plain>继续购物</el-button></router-link>
        <el-button type="success" plain>去结算</el-button>
      </div>
      <el-card class="box-card">
        <el-table
          ref="multipleTable"
          :data="merchandises"
          tooltip-effect="dark"
          style="width: 100%"
          @selection-change="handleSelectionChange">
          <el-table-column
            type="selection"
            width="40"
            align="center">
          </el-table-column>
          <el-table-column
            label="商品信息"
            width="360"
            align="center">
            <template slot-scope="scope">
              <img style="height: 80px; width: 80px; float: left" :src="scope.row.merchandise.front_cover_img">
              <p style="float: left; width: 230px; margin-left: 20px">{{ scope.row.merchandise.name }}</p>
            </template>
          </el-table-column>
          <el-table-column
            label="单价"
            width="200"
            align="center">
            <template slot-scope="scope">
              <p>￥{{ scope.row.merchandise.sale_price }}</p>
            </template>
          </el-table-column>
          <el-table-column
            label="数量"
            width="200"
            align="center">
            <template slot-scope="scope">
              <el-input-number v-model="scope.row.num" @change="update_merc_num(scope.row)" size="mini" :min="1" :max="10000"></el-input-number>
            </template>
          </el-table-column>
          <el-table-column
            label="金额"
            width="200"
            align="center">
            <template slot-scope="scope">
              <p style="color: #FE4407; font-weight: bold">￥{{ scope.row.merchandise.sale_price * scope.row.num }}</p>
            </template>
          </el-table-column>
          <el-table-column
            label="操作"
            align="center">
            <template slot-scope="scope">
              <el-button type="text" size="small">添加到收藏</el-button><br>
              <el-button type="text" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
      <div>
        <el-checkbox @change="handle_check_all" v-model="check_all">全选</el-checkbox>
        <el-button type="text" @click="delete_selected()">删除勾选</el-button>
        <el-button type="text" @click="clear_cart">清空购物车</el-button><br/>
        <router-link :to="{name: 'index'}"><el-button plain>继续购物</el-button></router-link><br/>
        <p style="text-align: right">已选{{ selected_mercs.length }}件商品，总价：<span style="color: green">￥{{ total_price }}元</span></p>
      </div>
      <el-card class="box-card" style="">
        <div slot="header" class="clearfix">
          <span>配送地址</span>
        </div>
        <ul style="font-size: 12px;">
          <li style="margin: 0 20px; float: left; border: 1px solid lightgray; width: 130px; height: 100px; list-style: none">+新增收货地址</li>
          <li v-for="i in addresses" :class="{active_address: i.id==active_address}" @click="select_address(i.id)" style="margin: 0 20px; float: left; border: 1px solid lightgray; width: 130px; height: 100px; list-style: none">
            <p>地址：北京市 市辖区 西城区 西城区北京市 市辖区 西城区 西城区<br/>电话：18516770799<br/>收货人：嘻嘻嘻</p>
          </li>
        </ul>
      </el-card>
      <div>
        <div style="height: 30px; background-color: silver">选择和支付方式</div>
        <div>
          <ul>
            <li style="float: left; border: 1px solid lightgray">
              <img style="width: 130px" src="../../static/images/pay/alipay.jpg">
            </li>
          </ul>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
  import primary from "@/api/primary"

  export default {
    data() {
      return {
        merchandises: [],
        addresses: [
          {
            id: 1,
            address: "xxxxxxxxxxxxxxxxxxxxx",
            mobile: "xxxxxxxxxx",
            name: "xxxxx",
          },
          {
            id: 2,
            address: "xxxxxxxxxxxxxxxxxxxxx",
            mobile: "xxxxxxxxxx",
            name: "xxxxx",
          },
          {
            id: 3,
            address: "xxxxxxxxxxxxxxxxxxxxx",
            mobile: "xxxxxxxxxx",
            name: "xxxxx",
          },
          {
            id: 4,
            address: "xxxxxxxxxxxxxxxxxxxxx",
            mobile: "xxxxxxxxxx",
            name: "xxxxx",
          },
        ],
        tableData3: [{
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }],
        multipleSelection: [],
        active_address: 2,
        checkedCities: [],
        isIndeterminate: true,
        check_all: false,
        total_price: 0,
        selected_mercs: []
      }
    },
    methods: {
      handle_check_all(data) {
        console.log("handle_check_all")
        console.log(this.check_all)
        if(this.check_all){
          console.log("else")
          this.merchandises.forEach(item => {
            console.log("item:", item)
            this.$refs.multipleTable.toggleRowSelection(item, true)
          })
        }else{
          this.$refs.multipleTable.clearSelection()
        }
      },
      handleSelectionChange(val) {
        this.selected_mercs = val
        var total_price = 0
        val.forEach(item => {
          total_price += item.merchandise.sale_price * item.num
        })
        this.total_price = total_price

        if(val.length == this.merchandises.length){
          this.check_all = true
        }else{
          this.check_all = false
        }
        this.multipleSelection = val
      },
      select_address(id){
        this.active_address = id
      },
      delete_selected(){
        this.selected_mercs.forEach(item => {
          this.delete_shopingcard_item(item)
        })
      },
      clear_cart(){
        this.merchandises.forEach(item => {
          this.delete_shopingcard_item(item)
        })
      },
      get_shopingcard_data(){
        var self = this
        primary.get("shopingcard").then(function (response) {
          self.merchandises = response.data
        })
      },
      delete_shopingcard_item(item){
        var self = this
        primary.delete("shopingcard/"+item.id).then(response =>{
          self.merchandises.forEach((i, index) => {
            if(item == i){
              this.merchandises.splice(index, 1)
              return
            }
          })
        })
      },
      update_merc_num(item){
        setTimeout( () => {
          primary.patch("shopingcard/"+item.id, {num: item.num})
        }, 200)
  },
  test(d){
    console.log("num", d.num)
    console.log("d", d)
    setTimeout(() => {
      console.log("d", d)
      console.log("num", d.num)
    }, 200)
  }
  },
  mounted(){
    this.get_shopingcard_data()
  }
  }
</script>

<style scoped>
  .active_address {
    border: 1px solid red !important
  }
  li {
    list-style: none
  }
</style>

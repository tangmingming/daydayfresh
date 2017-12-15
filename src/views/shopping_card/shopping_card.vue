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
        <el-button plain>继续购物</el-button>
        <el-button type="success" plain>去结算</el-button>
      </div>
      <el-card class="box-card">
        <el-table
          :data="tableData3"
          style="width: 100%">
          <el-table-column
            fixed
            prop="date"
            label="日期"
            width="438">
          </el-table-column>
          <el-table-column
            prop="name"
            label="姓名"
            width="240">
          </el-table-column>
          <el-table-column
            prop="province"
            label="省份"
            width="240">
          </el-table-column>
          <el-table-column
            prop="city"
            label="市区"
            width="240">
          </el-table-column>
        </el-table>
      </el-card>
      <div>
        <el-button type="text">清空购物车</el-button><br/>
        <el-button plain>继续购物</el-button><br/>
        <p style="text-align: right">3件商品，总价：<span style="color: green">￥659元</span></p>
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
  export default {
    data() {
      return {
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
        active_address: 2,
        tableData3: [{
          date: '2016-05-03',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-02',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-04',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-01',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-08',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-06',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-07',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }]
      }
    },
    methods: {
      select_address(id){
        this.active_address = id
      }
    }
  }
</script>

<style scoped>
  .active_address {
    border: 1px solid red !important;
  }
  li {
    list-style: none;
  }
</style>

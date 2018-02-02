<template>
  <div>

    <div style="width: 400px; height: 400px; float: left">
      <el-carousel indicator-position="outside">
        <el-carousel-item v-for="item in 4" :key="item">
          <h3>{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div style="width: 500px; float: left">
      <h3>{{ merchandise.name }}</h3>
      <p style="font-size: 13px">{{ merchandise.desc }}</p>
      <div style="font-size: 13px">
        <p>此商品为免运费商品，计算配送金额时将不计入配送费用</p>
        <p>市场价&nbsp;&nbsp;&nbsp;<span style="background-color: green; color: beige">￥{{ merchandise.market_price }}元</span></p>
        <p>促销价&nbsp;&nbsp;&nbsp;<span style="font-size: 20px; color:red">￥{{ merchandise.sale_price }}元</span></p>
        <p>销&nbsp;&nbsp;&nbsp;&nbsp;量&nbsp;&nbsp;&nbsp;<span style="font-size: 16px; color:red">{{ merchandise.sales_numm }}</span></p>
        <div>
          数&nbsp;&nbsp;&nbsp;&nbsp;量
          <el-input-number style="margin: 0 30px" :min="1" :max="10" v-model="num"></el-input-number>
        </div>
        <div style="margin: 20px">
          <el-button type="success" @click="add_cart()" icon="el-icon-circle-plus">加入购物车</el-button>
          <el-button icon="el-icon-star-off">收藏</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import primary from "@/api/primary"

  export default {
    data(){
      return {
        num: 1
      }
    },
    props: ["merchandise"],
    methods: {
      add_cart(){
        var self = this
        primary.post("shopingcard", {num: self.num, merchandise: self.merchandise.id}).then(function (response){
          // self.$message("添加成功")
        })
      }
    }
  }

</script>

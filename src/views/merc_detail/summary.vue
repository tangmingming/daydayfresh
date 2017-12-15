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
      <h3>田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛</h3>
      <p style="font-size: 13px">前腿+后腿+羊排共8斤，原生态大山放牧羊羔，曾经的皇室贡品，央视推荐，2005年北京招待全球财金首脑。五层专用包装箱+真空包装+冰袋+保鲜箱+顺丰冷链发货，路途保质期8天</p>
      <div style="font-size: 13px">
        <p>此商品为免运费商品，计算配送金额时将不计入配送费用</p>
        <p>市场价&nbsp;&nbsp;&nbsp;<span style="background-color: green; color: beige">￥106元</span></p>
        <p>促销价&nbsp;&nbsp;&nbsp;<span style="font-size: 20px; color:red">￥106元</span></p>
        <p>销&nbsp;&nbsp;&nbsp;&nbsp;量&nbsp;&nbsp;&nbsp;<span style="font-size: 16px; color:red">xx</span></p>
        <div>
          数&nbsp;&nbsp;&nbsp;&nbsp;量
          <el-input-number style="margin: 0 30px" :min="1" :max="10" label="描述文字"></el-input-number>
        </div>
        <div style="margin: 20px">
          <el-button type="success" icon="el-icon-circle-plus">加入购物车</el-button>
          <el-button icon="el-icon-star-off">收藏</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

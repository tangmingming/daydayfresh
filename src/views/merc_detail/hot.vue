<template>
  <div style="background-color: blueviolet">
    <el-card class="box-card">
      <div style="text-align: center" slot="header" class="clearfix">
        <span>热卖商品</span>
      </div>
      <div v-for="n in 3">
                  <el-card :body-style="{ padding: '0px' }">
              <img style="width: 100%" src="../../static/images/merchandise/30_P_1448948663450.jpg">
              <div style="padding: 14px;">
                <span style="color:red">￥2000</span>
                <a style="font-size: 12px">电脑都觉得男方家拿到今年非觉得呢动脑筋</a>
              </div>
            </el-card>
        </div>
    </el-card>
  </div>
</template>

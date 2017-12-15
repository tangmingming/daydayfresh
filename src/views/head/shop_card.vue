<template>
  <el-badge :value="12" class="item"><el-dropdown>
    <el-button>
      查看购物车<i class="el-icon-arrow-down el-icon--right"></i>
    </el-button>
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item v-for="i in 4" :key="i">
        <img style="float: left; width: 50px" src="../../static/images/merchandise/30_P_1448948663450.jpg" />
        <div style="float: left">
          <p style="margin: 0; font-size: 12px; line-height: 12px">某某某商品某某某商品某某某商品某某某商品</p>
          <p style="margin: 0; font-size: 10px; color:red; clear: both">￥xx元 x 1</p>
        </div>
      </el-dropdown-item>
    </el-dropdown-menu>
  </el-dropdown>
  </el-badge>
</template>

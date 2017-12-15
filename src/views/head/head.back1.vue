<template>
  <div>
    <div style="height:34px; background-color: #f5f5f5; border-bottom: 1px solid #e5e5e5">
      <div style="margin-top: 10px; margin-left: 40px; width:120px; margin-right: 0px;">
        <router-link to="login">登录</router-link>
        <a>|</a>
        <router-link to="registry">注册</router-link>
      </div>
      <div style="float: right">
        <el-dropdown>
          <span class="el-dropdown-link">
            下拉菜单<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>黄金糕</el-dropdown-item>
            <el-dropdown-item>狮子头</el-dropdown-item>
            <el-dropdown-item>螺蛳粉</el-dropdown-item>
            <el-dropdown-item disabled>双皮奶</el-dropdown-item>
            <el-dropdown-item divided>蚵仔煎</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

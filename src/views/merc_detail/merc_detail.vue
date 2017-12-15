<template>
  <div style="width: 1200px; margin: 0 auto">
    <el-breadcrumb separator="/" style="margin: 20px">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>活动管理</el-breadcrumb-item>
      <el-breadcrumb-item>活动列表</el-breadcrumb-item>
      <el-breadcrumb-item>活动详情</el-breadcrumb-item>
    </el-breadcrumb>
    <summary_2></summary_2>
    <particulars v-for="i in 4" :key="i" style="width: 940px; float: left"></particulars>
    <hot style="width: 260px; float: left"></hot>
  </div>
</template>

<script>
  import summary_2 from "./summary.vue"
  import particulars from "./particulars.vue"
  import hot from "./hot.vue"

  export default {
    components: {
      summary_2,
      particulars,
      hot
    }
  }
</script>

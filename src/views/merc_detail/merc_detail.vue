<template>
  <div style="width: 1200px; margin: 0 auto">
    <el-breadcrumb separator="/" style="margin: 20px">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>活动管理</el-breadcrumb-item>
      <el-breadcrumb-item>活动列表</el-breadcrumb-item>
      <el-breadcrumb-item>活动详情</el-breadcrumb-item>
    </el-breadcrumb>
    <summary_2 :merchandise="merchandise"></summary_2>
    <particulars style="width: 940px; float: left" :merchandise="merchandise"></particulars>
    <hot style="width: 260px; float: left"></hot>
  </div>
</template>

<script>
  import summary_2 from "./summary.vue"
  import particulars from "./particulars.vue"
  import hot from "./hot.vue"

  import primary from "@/api/primary"

  export default {
    data(){
      return {
        merchandise: {},
        id: null
      }
    },
    components: {
      summary_2,
      particulars,
      hot,
    },
    mounted(){
      var self = this
      var id = this.$route.query.id
      if(!id){
        this.$message({
          type: "error",
          message: "url没有指定商品ID"
        })
        this.id = id
        return
      }
      primary.get(`merchandise/${id}`).then(function (response) {
        self.merchandise = response.data
        console.log("merchandise")
      })
    }
  }
</script>

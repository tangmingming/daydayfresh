<template>
  <div class="bg-box" style="height: 500px">
    <div style="width: 900px; margin: 0 auto">
      <div style="width: 400px; height: 500px; float: right">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
  import top from "./top.vue"
  import footer_2 from "../footer/footer.vue"

  export default {
    components: {
      top: top,
      footer_2: footer_2
    }
  }
</script>

<style scoped>
  .bg-box{
    background:url(../../static/images/login/loginBg1.jpg) no-repeat center center;
  }
</style>

<template>
  <el-card style="height: 100%">
    <div style="width: 80%; height: 100%; margin: 0 auto">
      <h2>账号登录</h2>
      <hr />
      <el-input style="margin: 24px 0" placeholder="请输入内容" v-model="username">
        <template slot="prepend">用户名</template>
      </el-input>
      <el-input style="margin: 24px 0" type="password" placeholder="请输入内容" v-model="password">
        <template slot="prepend">密&nbsp;&nbsp;&nbsp;&nbsp;码</template>
      </el-input>
      <el-button style="width: 100%; margin: 24px 0" @click="login()" type="success">登&nbsp;&nbsp;&nbsp;&nbsp;录</el-button>
      <p style="font-size: 13px; margin: 24px 0">没有账号？<router-link to="/app/main/registry">[立即注册]</router-link></p>
    </div>
  </el-card>
</template>

<script>
  import api from "../../api"
  export default {
    data: ()=>{
      return {
        username: "",
        password: ""
      }
    },
    methods: {
      login(){
        var self = this
        var username = this.username
        api.primary.login({
          username: this.username,
          password: this.password
        }).then(function (response){
          self.$store.commit("login", {username, token: response.data.token})

          if(self.$route.query.next){
            self.$router.push({path: self.$route.query.next})
            return
          }
          self.$router.push({"name": "index"})
        }).catch( function(error){
          self.$message.warning("用户名或密码错误")
        })
      }
    },
  }
</script>

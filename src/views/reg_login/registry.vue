<template>
  <el-card style="height: 100%">
    <div style="width: 80%; height: 100%; margin: 0 auto">
      <h2>用户注册</h2>
      <hr />
      <label style="color:red; font-size: 14px; float: right">&nbsp;{{ error_msgs["username"] }}</label>
      <el-input style="margin-bottom: 5px" v-model="form_datas['username']">
        <template slot="prepend">用户名</template>
      </el-input>
      <label style="color:red; font-size: 14px; float: right">&nbsp;{{ error_msgs["mobile"] }}</label>
      <el-input style="margin: 12px 0" prefix="1111"  v-model="form_datas['mobile']" label="lllll" suffix="sssss">
        <template slot="prepend">手机号</template>
      </el-input>
      <label style="color:red; font-size: 14px; float: right">&nbsp;{{ error_msgs["code"] }}</label>
      <div style="margin: 12px 0">
        <el-input style="width: 160px; float: left" prefix="1111" v-model="form_datas['code']" placeholder="请输入内容" >
          <template slot="prepend">验证码</template>
        </el-input>
        <el-button style="float: right;" type="primary" @click="send_verify_code()"  :disabled="send_btn_dis" plain>{{ send_btn_text }}</el-button>
      </div>
      <label style="color:red; font-size: 14px; float: right">&nbsp;{{ error_msgs["password"] }}</label>
      <el-input style="margin: 12px 0" type="password" v-model="form_datas['password']" placeholder="请输入内容" >
        <template slot="prepend">密&nbsp;&nbsp;&nbsp;&nbsp;码</template>
      </el-input>
      <el-button style="width: 100%; margin: 12px 0" @click="registry" type="success">注&nbsp;&nbsp;&nbsp;&nbsp;册</el-button>
      <p style="font-size: 13px; margin: 12px 0">已有账号？<router-link :to="{name: 'login'}">[立即登录]</router-link></p>
    </div>
  </el-card>
</template>


<script>
  import router from "../../router"
  import api from "../../api/index"
  import primary from "../../api/primary"
  export default {
    data(){
      return {
        error_msgs:{
          username:"",
          mobile:"",
          code:"",
          password:""
        },
        form_datas:{
          username:"",
          mobile:"",
          code:"",
          password:""
        },
        send_btn_text: "发送验证码",
        send_btn_dis: false
      }
    },
    methods:{
      registry(){
        var self = this
        primary.post("shopuser", this.form_datas).then(()=>{
          primary.post("api-token-auth", {username: self.form_datas.username, password: self.form_datas.password}).then( response => {
            self.$store.commit("login", {username: self.form_datas.username, token: response.data.token})
            self.$router.push({"name": "index"})
            self.$message.success("注册成功")
          }).catch( error => {
            self.$message.warning("注册成功,但登录失败,请尝试手动登录")
            self.$router.push({name: "login"})
          })
        }).catch(error => {
          self.$message.warning("error:"+error.response.data)
        })
      },
      send_verify_code(){
        var self = this
        primary.post("verifycode", {mobile: this.form_datas.mobile}).then( response => {
          this.send_btn_dis = true
          function run_count(t){
            self.send_btn_text = `重新发送(${t})`
            if(t>0){
              t -= 1
              setTimeout(function () {
                run_count(t)
              }, 1000)
            }else{
              self.send_btn_dis = false
              self.send_btn_text = "重新发送"
            }
          }
          run_count(60)
        }).catch(error => {
          self.$message.warning("error:"+error.response.data.detail)
        })
      }
    },
    mounted: ()=>{
      console.log("registry")
//      console.log(this.$store.state)
    },
    computed: {
      test: function () {
        return this.$store.state
      }
    }
  }
</script>

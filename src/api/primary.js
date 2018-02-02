
import axios from "axios"
import router from "../router"
import store from "@/store"

import app from "@/main"

const server = "http://127.0.0.1:8000"

var primary = axios.create({
  baseURL: "http://daydayfresh.mingmingt.xyz/api/v1/",
  timeout: 5000,
})

primary.interceptors.request.use(config => {
  console.log("primary.interceptors.request.use")
  if(store.state.is_logged){
    console.log("add authoriztion:", store.state.token)
    config.headers.Authorization = store.state.token
  }
  return config
}, error => {
  console.log("request error")
  return Promise.reject(error)
})

primary.interceptors.response.use( response => {
  return response
}, error => {
  console.log("interceptors:")
  console.log(error.response)
  if (error.response) {
    if(error.response.status == 400){
      return Promise.reject(error)
    }else if(error.response.status == 401){
      app.$confirm('是否前往登录', '尚未登录', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'info',
        center: true
      }).then(() => {
        console.log("app.$router.path")
        console.log(app.$route.path)
        app.$router.push({name: "login", query: {next: app.$route.fullPath}})
      })
      return
    }else if(error.response.status == 403){
      if(error.response.data.detail == "Signature has expired." || "Error decoding signature." == error.response.data.detail ){
        app.$confirm('是否前往登录', '登录过期', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'info',
          center: true
        }).then(() => {
          app.$router.push({name: "login", params: {next: app.$router.path}})
        })
        return
      }
      app.$message({
        message: "没有权限",
        type: "warning"
      })
      return
    }else{
      app.$message.error("后台错误:"+error.response.status)
      console.log(error.response.status, ":", error.response.data)
      return
    }
  } else {
    console.log('Error', error.message);
  }
  console.log(error.config);
  app.$message.warning("未知错误")
})

export const login = parameters => {
  return primary.post("api-token-auth", parameters)
}

export const get_address = parameters => {
  return primary.get("address", parameters)
}

export const get_person = parameters => {
  return primary.get("person", parameters)
}

export const add_person = parameters => {
  return primary.post("person", parameters)
}

export const patch_person = parameters => {
  return primary.patch("person", parameters)
}

export const delete_person = parameters => {
  return primary.delete("person", parameters)
}

export const send_verify_code = parameters => {
  return primary.post("verifycode", parameters)
}

export const registry = parameters => {
  return primary.post("shopuser", parameters)
}

export const get_merchandise = parameters => {
  return primary.post("merchandise", parameters)
}

export const post_shopingcard = parameters => {
  return primary.post("shopingcard", parameters)
}

export const get_shopingcard = parameters => {
  return primary.post("shopingcard", parameters)
}

export default primary

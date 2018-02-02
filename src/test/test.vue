<template>
  <div>
    <input :value="test_model">
    <button @click="test_model = 'wangwu'">change test model</button>
    <button v-on:mouseleave="mouse()" @click="get_person()">get_person</button><br>
    <button @click="add_person()">add_person</button><br>
    <button @click="patch_person()">patch_person</button><br>
    <button @click="delete_person()">delete_person</button><br>
    <el-input label="错误。。。。" suffix="sssss"></el-input>
    <ul id="example-1">
      <li v-for="item in items">
        {{ item }}
      </li>
    </ul>
  <router-link :to="{name: 'index', query:{age: 12}}">jump</router-link>
    <div v-for="item in data" >
    <el-checkbox :checked="is_checkeds[item.id]"></el-checkbox>
      </div>
  </div>
</template>

<script>
  import api from "../api"
  export default {
    data: () => {
      return {
        test_model: "zhangsan",
        name: "abc",
        items: [1, 2],
        is_checkeds: {
          11: true,
          12: false,
          13: true
        },
        data: [
          {id: 11},
          {id: 12},
          {id: 13},
        ]
      }
    },
    methods: {
      change_test_model(){
        this.test_model = "lisi"
        console.log(this.test_model)
      },
      get_person(){
        api.primary.get_person()
      },
      add_person(){
        api.primary.add_person({
          name: this.name,
          age: 13
        }).catch(error => {
          console.log("add_person error")
        })
        this.name += "d"
      },
      patch_person(){
        api.primary.patch_person()
      },
      delete_person(){
        this.items.push(4)
      },
      mouse(){
        console.log("mouse")
      }
    }
  }
</script>

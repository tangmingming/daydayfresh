<template>
  <div>
    <p v-for="(n, key, index) in items" :key="index">
      n:{{n}} key {{ key }} index: {{ index}}
    </p>
    <c_comp v-for="i in 3" :key="i"></c_comp>
  </div>
</template>

<script>
  import c_comp from "./c_comp.vue"

  export default {
    data(){
      return {
        items: [
          {
            name: "zhangsan",
            age: 12
          },
          {
            name: "lisi",
            age: 13
          },
          {
            name: "wangwu",
            age: 14
          },

        ]
      }
    },
    components: {
      c_comp: c_comp
    }
  }
</script>

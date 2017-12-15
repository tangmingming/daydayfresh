<template>
  <div>
    <p>{{ index }}</p>
    <button @click="add">+1吧</button>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        index: 12
      }
    },
    methods: {
      add(){
        this.index += 1
      }
    },
    created: function () {
      console.log("create")
    },
    updated: function () {
      console.log("update")
    }
  }
</script>


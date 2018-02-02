<template>
  <div v-html="merchandise.particulars">

  </div>
</template>

<script>
  export default {
    data(){
      return {
      }
    },
    props: ["merchandise"]
  }
</script>

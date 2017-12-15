<template>
  <div>
    <banner></banner>
    <new_product></new_product>
  </div>
</template>

<script>
  import banner from "./banner.vue"
  import new_product from "./new_product.vue"
  export default {
    components: {
      banner: banner,
      new_product: new_product,
    }
  }
</script>

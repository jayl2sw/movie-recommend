<template>
  <div>
    <collection-detail></collection-detail>
  </div>
</template>

<script>
import CollectionDetail from '@/components/collections/CollectionDetail'

export default {
  name: "CollectionDetailView",
  components: {
    CollectionDetail
  }
}
</script>

<style scoped>
div {
  width:100%;
  height: 300px;
}
</style>
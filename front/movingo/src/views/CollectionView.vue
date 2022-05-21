<template>
  <div class="row">
    <main-carousel></main-carousel>
    <div v-for="collection in collections" :key='collection.pk' class="col-3 mx-0 my-3">
      <collection-card :collection="collection"></collection-card>
    </div>
  </div>
</template>

<script>
import MainCarousel from '@/components/MainCarousel'
import CollectionCard from '@/components/collections/CollectionCard'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MainView',
  components: {
    MainCarousel,
    CollectionCard,
  },
  computed: {
    ...mapGetters(['collections'])
  },
  methods: {
    ...mapActions(['fetchCollections'])
  },
  created() {
    this.fetchCollections()
  },
}
</script>
<style scoped>
h1{
  color:whilte;
}
li {
  color:black;
}
</style>

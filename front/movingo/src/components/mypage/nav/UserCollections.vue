<template>
  <div id="user-collections" class="mx-1 my-3">
    <div v-for="collection in collections" :key="collection.pk" class="user-collection">
      <h3>{{ collection.title }}</h3>
      <div v-if="collection.movies">
        <movies-list :movies="collection.movies"></movies-list>
      </div>
    </div>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList'
export default {
  name:'UserCollections',
  props: {
    collections:Array,
  },
  components:{
    MoviesList
  },
}
</script>

<style scoped>
.user-collection > div {
  width: 100%;
  border-radius: 10px;
  background: #B5ACAC;
}
.empty_collection {
  width: 100%;
  border-radius: 10px;
  background: #B5ACAC;
}

</style>
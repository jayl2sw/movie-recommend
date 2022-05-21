<template>
  <div class="my-3 mx-1">
    <h3>{{ username }} 님의 위시리스트</h3>
    <div id="wish-list" class="my-3">
      <movies-list :movies="movies"></movies-list>
    </div>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList'
export default {
  name:'WishList',
  props: {
    movies:Array,
    username:String,
  },
  components:{
    MoviesList
  }

}
</script>

<style scoped>
#wish-list {
  width: 100%;
  border-radius: 10px;  
  background: #B5ACAC;
}

</style>
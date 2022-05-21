<template>
  <div>    
    <h3 class="mx-3 my-3">{{ movielisttitle }}</h3>
    <carousel :perPage=6 :scrollPerPage="false" :navigationEnabled="true" :paginationEnabled="false" >
      <slide class="card label mx-0" v-for="movie in movies" :key="movie.id">      
        <img style="height:20rem;" :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" alt="...">
      </slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';
export default {
  name: 'MoviesList',
  props: {
    movies: Array,
    movielisttitle: String,
  },
  components:{
    Carousel, Slide
  },
  computed: {
  },
  methods: {
  },
}
</script>

<style scoped>
  h3{
    color:white;
  }
  li {
    color:black;
  }

  .VueCarousel-navigation-button[data-v-453ad8cd] {
    color:white;
  }
  .movie-poster:hover {
    cursor: pointer;
    filter: brightness(0.3);
    
  }
</style>

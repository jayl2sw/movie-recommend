<template>
  <div>    
    <h3 class="mx-3 my-3">{{ movielisttitle }}</h3>
    <carousel :perPage=6 :scrollPerPage="false" :navigationEnabled="true" :paginationEnabled="false" :NavigationNextLabel="nextLabel" :NavigationPrevLabel="rightLabel">
      <slide class="label mx-0" v-for="mv in movies" :key="mv.id">   
        <img @click="[fetchMovie(mv.id), fetchTrailerURI(mv.original_title)]" type="button" data-bs-toggle="modal" data-bs-target="#movieDetail" class="movie-list-poster" style="height:20rem;" :src="`https://image.tmdb.org/t/p/original/${ mv.poster_path }`" alt="...">        
      </slide>
    </carousel>
    <movie-detail></movie-detail>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import { mapActions} from 'vuex'
import MovieDetail from '@/components/detail/MovieDetail'


export default {
  name: 'MoviesList',
  data () {
    return {
        nextLabel: "<img src='/assets/right-arrow.png' />",
        prevLabel: "<img src='/assets/left-arrow.png' />"
    }
  },
  props: {
    movies: Array,
    movielisttitle: String,
  },
  components:{
    Carousel, Slide,
    MovieDetail,
  },
  computed: {
  },
  methods: {
    ...mapActions(['fetchMovie', 'fetchTrailerURI']),
  },
}
</script>

<style scoped>
  .movie-list-poster{
    border-radius: 10px;
    padding:5px;
  }
  h3{
    color:white;
  }
  .movie-list-poster{
    width:100%;
  }

  .VueCarousel-navigation-button {
    color:white;
  }
  .movie-poster:hover {
    cursor: pointer;
    filter: brightness(0.3);
  }
  button {
    color:white;
    height:50px;
  }
</style>

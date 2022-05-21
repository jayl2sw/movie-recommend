<template>
  <div id="movie-list-frame">    
    <h3 id="movie-list-title">{{ movielisttitle }}</h3>
    <carousel id="mlc" :perPage=6 :scrollPerPage="false" :navigationEnabled="true" :paginationEnabled="false" :NavigationNextLabel="nextLabel" :NavigationPrevLabel="prevLabel">
      <slide id="movie-list-slide" class="label mx-0" v-for="mv in movies" :key="mv.id">   
        <div class="img-box">
          <img @click="[fetchMovie(mv.id), fetchTrailerURI(mv.original_title)]" type="button" data-bs-toggle="modal" data-bs-target="#movieDetail" class="movie-list-poster" style="height:20rem;" :src="`https://image.tmdb.org/t/p/original/${ mv.poster_path }`" alt="...">        
        </div>
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
  #mlc {
    overflow: visible;
  }

  #mlc:hover{
    filter:brightness(0.5);
  }

  .movie-list-poster{
    border-radius: 10px;
    width:100%;
    padding:5px; 
    cursor: pointer;
    
  }
  #movie-list-title{
    color:white;
    font-weight: bold;
    margin:10px;
  }
  
  .movie-list-poster:hover { 
    transform: translateY(-10px);
    transform: scale(1.03);
    opacity: 5;
    overflow: visible;
    
  }

  .VueCarousel-navigation-button {
    color:white;
  }

  button {
    color:white;
    height:50px;
  }
  #movie-list-slide:hover {
    overflow: visible;
  }
  .img-box {
    padding-top:0.15rem;
  }
  #movie-list-frame {
    margin-bottom:50px;
  }
</style>

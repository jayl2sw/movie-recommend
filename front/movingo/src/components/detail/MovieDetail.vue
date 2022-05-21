<template>
  <div class="modal fade " id="movieDetail" tabindex="-1" aria-labelledby="movieDetail" aria-hidden="true">
    <div class="modal-dialog modal-xl modal-dialog-centered">
      <div class="modal-content">
        <div id="modal-header">
          <button type="button" class="btn-close mx-2 my-2" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div id="modal-body" v-if="movie" class="row">          
          <div id="poster-box" class="mx-4 col-5">
            <img id="poster" :src="poster" alt="">
          </div>
          <div class="col-6">
            <movie-info id="movie-info" :movie="movie"></movie-info>
            <movie-nav id="movie-nav"></movie-nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MovieInfo from './MovieInfo.vue'
import MovieNav from './MovieNav.vue'
export default {
  name: 'MovieDetail',
  computed: {
    ...mapGetters(['movie']),
    poster() {
      return this.movie.poster_path ? `https://image.tmdb.org/t/p/original/${ this.movie.poster_path }` : '..'
    },
  },
  components:{
    MovieInfo,
    MovieNav,
  },
}
</script>

<style scoped>
#modal-header {
  text-align: right;
}
.modal-content {
  background: #7A7373;
  border:solid 1px black;
  border-radius: 10px;
}
#modal-body {
  height:700px;
}
#poster-box {
  width:480px;
  height: 670px;
  
}
#poster {
  width: 100%;
  height: 100%;
  border-radius: 10px;
}
#movie-info{
  height: 305px;
}
</style>
<template>
  <div id="movie-info" class="my-2">
    <h2>{{ movie.title }}</h2>
    <p>개봉일: {{ movie.release_date }}</p>
    <p>평점: {{ movie.vote_average }}</p>
    <p>장르: <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }}, </span></p>
    <div>{{ overview }}...</div>
    <div id="movie-info-buttons" class="d-flex">
      <div v-if="wished" class="movie-wish text-center">
        <button @click="wishMovie(movie.pk)" class="movie-detail-button"><i class="movie-like bi bi-suit-heart-fill"></i></button>
        <p class="movie-wish-cnt mx-2">{{ wish_cnt }}</p>
      </div>
      <div v-if="!wished" class="movie-wish text-center">
        <button @click="wishMovie(movie.pk)" class="movie-detail-button"><i class="movie-like bi bi-suit-heart"></i></button>
        <p class="movie-wish-cnt">{{ wish_cnt }}</p>
      </div> 
      <div>
         <button class="movie-detail-button"><i class="movie-add bi bi-plus-lg"></i></button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieInfo',
  props: {
    movie:Object,
  },
  computed: {
    ...mapGetters(['currentUser']),
    overview() {
      return String(this.movie.overview).substr(0, 200)
    },
    wished() {
    return this.movie.wish_users ? this.movie.wish_users.filter(element => {
      return element.pk == this.currentUser.pk
      }).length : false
    },
    wish_cnt() {
      return this.movie.wish_count
    }
  },
  methods: {
    ...mapActions(['wishMovie']),

  }
}
</script>

<style scoped>
#movie-info{ 
  color:white;
}
#movie-info-buttons{
  margin-top:8px;
}
.movie-wish {
  width: 25px;
}
.movie-like {
  color:#932323;
  font-size: 25px;
}
.movie-detail-button {
  background: #7A7373;
}
.movie-wish-cnt {
  font-size:13px;
}
.movie-add{
  color:#FFFFFF;
  margin-left: 6px;
  font-weight: bold;
  font-size: 25px;
}
</style>
<template>
  <div id="movie-info" class="my-2">
    <h2>{{ movie.title }}</h2>
    <p>개봉일: {{ movie.release_date }}</p>
    <p>평점: {{ movie.vote_average }}</p>
    <p>장르: <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }}, </span></p>
    <div>{{ overview }}...</div>

  </div>
</template>

<script>
export default {
  name: 'MovieInfo',
  props: {
    movie:Object,
  },
  computed: {
    overview() {
      return String(this.movie.overview).substr(0, 200)
    }
  }
}
</script>

<style scoped>
#movie-info{ 
  color:white;
}
</style>
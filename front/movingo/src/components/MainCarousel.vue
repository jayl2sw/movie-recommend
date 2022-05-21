<template>
  <div>
    <carousel :perPage=1 :autoplay="true" :paginationEnabled="false" >
      <slide>
        <img src="https://image.tmdb.org/t/p/original/AbgEQO2mneCSOc8CSnOMa8pBS8I.jpg" class="d-block w-100" alt="...">
      </slide>
      <slide>
        <img src="https://image.tmdb.org/t/p/original/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg" class="d-block w-100" alt="...">
      </slide>
      <slide>
        <img src="https://image.tmdb.org/t/p/original/zqkmTXzjkAgXmEWLRsY4UpTWCeo.jpg" class="d-block w-100" alt="...">
      </slide>
      
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';

export default {
  name: 'MainCarousel',
  components:{
    Carousel, Slide
  },
  computed: {
  },
  methods: {
  },
}
</script>

<style>
</style>

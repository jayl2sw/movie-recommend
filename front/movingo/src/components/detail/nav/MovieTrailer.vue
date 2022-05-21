<template>
  <div>
    <div class="video-container">
      <iframe :src="trailerURI" frameborder="0"></iframe>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
// import axios from 'axios'
export default {
  name: "MovieTrailer",
  props:{
  },
  computed: {
    ...mapGetters(['trailerURI'])
  }
}

</script>

<style scoped>
  .video-container {
    height:300px;
    border-radius: 10px;
  }
  .video-container > iframe {
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 10px;
  }
</style>
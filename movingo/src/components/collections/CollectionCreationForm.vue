<template>
  <div class="modal fade" id="createcollection" tabindex="-1" aria-labelledby="createcollectionLabel" aria-hidden="true">
    <div class="modal-dialog modal-xl modal-dialog-centered">
      <div class="modal-content">
        <div id="modal-header">
          <button type="button" class="btn-close mx-2 my-2" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <input type="text" placeholder="컬렉션 제목을 입력해주세요">
        <input type="text" placeholder="컬렉션 소개를 입력해주세요">        
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'MovieDetail',
  data(){
    return {
    new_collection_title: "",
    new_collection_description: "",
    }
  },
  computed: {
    ...mapGetters(['movie']),
    poster() {
      return this.movie.poster_path ? `https://image.tmdb.org/t/p/original/${ this.movie.poster_path }` : '..'
    },
  },
  components:{
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

#movie-info{
  height: 305px;
}
</style>
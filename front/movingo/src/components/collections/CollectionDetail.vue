<template>
  <div id="collection-detail">
    <div class="d-flex align-items-center">
      <h2 id="collection-title">{{ collection.title }}</h2>
      <span id="collection-maker" v-if="collection.user.username">by {{ collection.user.username }}</span>
    </div>
    <div class="row my-4">
      <div class="col-6 px-3">
        <div id="collection-img-background">
          <!-- <img id="collection-img" src="" alt=""> -->
        </div>
      </div>
      <div class="col-6">
        <div>
          <h4>소개글</h4>
          <p id="description">{{ collection.description }}</p>
        </div>
        <div id="buttons">
          <div>
          <div v-if="liked">
            <button><i class="ilike bi bi-suit-heart-fill"></i></button>
            <span class="mx-2">{{ like_cnt }}</span>
          </div>
          <div v-if="!liked">
            <button><i class="ilike bi bi-suit-heart"></i></button>
            <span class="mx-2">{{ like_cnt }}</span>
          </div>
        </div>
        </div>
      </div>
    </div>
    <div id="movies-list-background">
      <movies-list :movies="collection.movies"></movies-list>
    </div>
    

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MoviesList from '@/components/MoviesList'
export default {
  name: "CollectionDetail",
  data() {
    return {
      collectionPk: this.$route.params.collectionPk,
    }
  },
  components: {
    MoviesList
  },
  computed: {
    ...mapGetters(['collection','currentUser']),

    like_cnt() {
      return this.collection.like_cnt
    },
    liked() {
      return this.collection.like_users.filter(element => {
        return element.id == this.currentUser.pk
      }).length
    },
    description() {
      return String(this.collection.description).substr(0, 30)
    }
  },
  methods: {
    ...mapActions(['fetchCollection'])
    
  },
  created() {
    this.fetchCollection(this.collectionPk)
  }
}
</script>

<style scpoed>
#collection-detail{
  margin:50px;
  color: white;
}
#collection-title{
  font-weight:600;
  font-size:30px;
  line-height:36px;
}
#collection-maker{
  margin-left: 10px;
}
#collection-img-background{
  width:100%;
  height:400px;
  border-radius: 10px;
  background:#7A7373;
}
#collection-img{
  width: 100%;
  height: 100%;
  border:none;
  border-radius: 10px;
}
h4{
  font-size:24px;
}
#description{
  font-size:20px;
}
button {
  background: black;
  border:none;
  padding:0;
}
.ilike {
  color:#932323;
  font-size: 25px;
}
#movies-list-background{
  background:#7A7373;
    width:100%;
    height:320px;
    border-radius: 10px;
}

</style>
<template>
  <router-link class="collection-card-router" :to="{ name: 'collection_detail', params: { collectionPk : collection.pk } }">
    <div id="collection-card">
      <div id="collection-background">
        <div id="collection-user-profile"></div>
      </div>
      <div id="collection-card-info">
        <h5 id="collection-card-title">{{ collection.title }}</h5>
        <div class="d-flex justify-content-between">
          <p id="collection-user">by {{ collection.user.username }}</p>
          <div>
            <p class="collection-tag">#HashTags</p>
          </div>
        </div>
        <div>
          <div v-if="liked">
            <button><i class="collectioncardlike bi bi-suit-heart-fill"></i></button>
            <span class="mx-2">{{ like_cnt }}</span>
          </div>
          <div v-if="!liked">
            <button><i class="collectioncardlike bi bi-suit-heart"></i></button>
            <span class="mx-2">{{ like_cnt }}</span>
          </div>
        </div>
        <div id="collection-description">{{ description }}</div>
      
      </div>
    </div>
  </router-link>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'CollectionCard',
  props: {
    collection:Object
  },

  components: {
  },
  computed: {
    ...mapGetters(['currentUser']),
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
}
</script>

<style scoped>

.collection-card-router {
  text-decoration: none;
}

#collection-card {
  font-family: 'Pretendard';
  width:100%;
  height: 400px;
  border:solid 1px ;
  border-radius: 10px;
  color: black; 
}
#collection-background {
  position:relative;
  background: #7A7373;
  width: 100%;
  height: 12rem;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
#collection-user-profile {
  border:  3px solid #B5ACAC;
  position: absolute;
  background: #7A7373;
  top: 157px;
  left: 36.7%;
  width: 80px;
  height: 80px;
  border-radius: 100%;
  box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.25);
}
#collection-user {
  font-weight:500;
  color: #7A7373;
}
#collection-card-info {
  padding-top:60px;
  padding-left:20px;
  padding-right:20px;
  background: #B5ACAC;
  height: 208px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}
#collection-title {
  margin:0px;
  font-size:20px;
  font-weight: 700;
}
.collection-tag {
  padding:1px;
  padding-left:3px;
  padding-right:3px;
  border-radius:3px;
  
  background:#7A7373;
  font-size: 10px;
  color:#FFFFFF;
}
#collection-card-description{
  margin-top:8px;
}
button {
  background: #B5ACAC;
  border:none;
  padding:0;
}
.collectioncardlike {
  color:#932323;
}

</style>

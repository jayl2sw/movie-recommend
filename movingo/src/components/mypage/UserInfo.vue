<template>
  <div id="userinfo">
    <div :class="{ hide: isMe }">
      <div v-if="followed" class="text-center">
        <button @click="followUser(profile.pk)" class="follow-button"><i class="movie-like bi bi-suit-heart-fill"></i></button>
      </div>
      <div v-if="!followed" class="text-center">
        <button @click="followUser(profile.pk)" class="follow-button"><i class="movie-like bi bi-suit-heart"></i></button>
      </div>      
    </div>
    <div id="infos">
      <div>
        <p>{{ profile.followings_cnt ? profile.followings_cnt: 0 }} </p>
        <p>팔로잉</p>
      </div>
      <div>
        <p>{{ profile.followers_cnt ? profile.followers_cnt : 0 }}</p>
        <p>팔로워</p>
      </div>
      <div>
        <p>{{ profile.collections_cnt ? profile.collections_cnt : 0 }}</p>
        <p>컬렉션</p>
      </div>
      <div>
        <p>{{ profile.reviews_cnt ? profile.reviews_cnt : 0 }}</p>
        <p>리뷰</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'UserInfo',
  props:{
    profile:Object,
    isMe:Boolean,
  },
  computed: {
    ...mapGetters(['currentUser']),
    followed() {
      return this.profile.followers ? this.profile.followers.filter(element => {
      return element.pk == this.currentUser.pk
      }).length : false
    },
  },
  methods: {
    ...mapActions(['followUser'])
  }

}
</script>

<style scoped>
#userinfo{
  display: flex;
  flex-direction: column;
  align-items: center;
}

#infos {
  text-align: center;
  display: flex;
  color:white;
  width:350px;
  justify-content: space-between;
}

.follow-button {
  background:black;
}
.bi {
  color: white;
  font-size:25px;
}

</style>
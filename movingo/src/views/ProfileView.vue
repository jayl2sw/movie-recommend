<template>
  <div>
    <mypage-header :username="profile.username"></mypage-header>
    <user-info :profile="profile" class="my-3" :isMe="isMe"></user-info>
    <mypage-nav :profile="profile"></mypage-nav>
  </div>
</template>

<script>
import MypageHeader from '@/components/mypage/MypageHeader'
import UserInfo from '@/components/mypage/UserInfo'
import MypageNav from '@/components/mypage/MypageNav'

import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components:{
    MypageHeader,
    UserInfo,
    MypageNav,
  },
  computed: {
    ...mapGetters(['profile', 'isMe']),
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
<style scoped>
</style>  

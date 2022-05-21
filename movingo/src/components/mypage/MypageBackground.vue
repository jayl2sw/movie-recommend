<template>
  <div>
    <user-header :username="profile.username"></user-header>
    <user-info :profile="profile" class="my-3"></user-info>
  </div>
</template>

<script>
import UserHeader from '@/components/mypage/upside/MypageHeader'
import UserInfo from '@/components/mypage/upside/UserInfo'


export default {
  name: 'ProfileView',
  props: {
    profile:Object,
  },
  components:{
    UserHeader,
    UserInfo
  },
  computed: {
  },
  methods: {
  },
  created() {
  },
}
</script>

<style scoped>

</style>

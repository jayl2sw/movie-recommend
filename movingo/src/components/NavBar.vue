<template>
  <nav class="d-flex justify-content-between align-items-center text-light my-4">
    <div style="width:32rem;" class="nav-left">
      <ul class="d-flex justify-content-between align-items-center my-0" >
        <li>
          <img src="../assets/logo.png" alt="로고" style="width:160px;">
        </li>
        <li id="home">
          <router-link :to="{ name: 'main' }" class="left-nav-item">HOME</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'collections' }" class="left-nav-item">컬렉션</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'community' }" class="left-nav-item">커뮤니티</router-link>
        </li>
      </ul>
    </div>
    <div class="nav-right" style="width:18rem;">
      <ul class="d-flex justify-content-end align-items-center my-0">
        <li v-if="!isLoggedIn" class="mx-3">
          <router-link :to="{ name: 'login' }" class="left-nav-item">Login</router-link>
        </li>
        <li v-if="!isLoggedIn" class="mx-1">
          <router-link :to="{ name: 'signup' }" class="left-nav-item">Signup</router-link>
        </li>

        <li id="for-loggedin" v-if="isLoggedIn" class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="color:white">
            {{ username }} 님
          </a>  
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <li>
              <router-link class="dropdown-item nav-item" :to="{ name: 'profile', params: { username } }">마이 페이지</router-link>
            </li>
            <li>
              <router-link class="dropdown-item nav-item" :to="{ name: 'edit_profile' , params: { username } }">회원정보 수정</router-link>
            </li>
            <li>
              <router-link class="dropdown-item nav-item" :to="{ name: 'logout' }">Logout</router-link>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style scoped>
a {
    color: white;
    text-decoration: none;
    font-size:20px;
    font-weight: 400;
}
ul {
  list-style:none;
}

.left-nav-item:hover {
  color: #B5ACAC;
  font-weight: bolder;
}
 .router-link-exact-active{
   color: #B5ACAC;
   font-weight: bold;
   text-decoration: underline;
 }
 .dropdown-item {
   color:black;
 }
 
</style>

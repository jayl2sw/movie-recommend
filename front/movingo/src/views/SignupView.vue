<template>
  <div class="d-flex justify-content-center align-items-center" style="height:1000px;">
    
    <div id="login-box" class="d-flex justify-content-center align-items-center">
      <account-error-list v-if="authError"></account-error-list>
      <form @submit.prevent="signup(credentials)">
        <div id="login-div">
          <!-- <div class="login-comp">
            <p class="label"><label for="profile_img">프로필 사진</label></p>
            <input class="input-box" type="file" id="profile_img" required />
          </div> -->
          <div class="login-comp">
            <p class="label"><label for="username">아이디 </label></p>
             <input  v-model="credentials.username" class="input-box" type="text" id="username" required/>
          </div>
          <div class="login-comp">
            <p class="label"><label for="password1">비밀번호 </label></p>
            <input v-model="credentials.password1" class="input-box" type="password" id="password1" required />
          </div>
          <div class="login-comp">
            <p class="label"><label for="password2">비밀번호 확인</label></p>
            <input v-model="credentials.password2" class="input-box" type="password" id="password2" required />
          </div>
          <div class="login-comp">
            <p class="label"><label for="nickname">닉네임</label></p>
            <input v-model="credentials.nickname" class="input-box" type="text" id="nickname" required />
          </div>  
        </div>
        <button id="login-btn" class="my-3">회원가입</button>
      </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          profile_img: null,
          username: '',
          password1: '',
          password2: '',
          nickname: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>


<style scope>

#login-box{  
  width: 566px;
  height: 748px;
  background-color: #7A7373;
  border: #7A7373;
  border-radius: 10px;
}

/* Rectangle 55 */
.input-box{
  width: 472px;
  height: 60px;

  background: #B5ACAC;
  border: #7A7373;
  border-radius: 7px;
}

#login-btn{
  /* Rectangle 56 */
  width: 474px;
  height: 60px;


  /* logo */
  border: #7A7373;
  background: #E11616;
  border-radius: 7px;

}


.login-comp {
  display: inline;
}
.Oauth-btn{
  width: 294px;
  height: 51px;
  border: #7A7373;
  border-radius: 7px;
}

.label {
  color:white;
  margin-left:0rem;
  text-align: start !important;
}

p {
  margin:0;
}

</style>





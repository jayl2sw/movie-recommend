<template>
  <div class="d-flex justify-content-center align-items-center" style="height:1000px;">
    
    <div id="login-box" class="d-flex justify-content-center align-items-center">

      <account-error-list v-if="authError"></account-error-list>
      
      <form @submit.prevent="login(credentials)" class="text-center">
        <div id="login-div" >
          <div class="login-comp">
            <p class="label"><label for="username"> 아이디 </label></p>
            <input v-model="credentials.username" class="input-box" type="text" id="username" required />
          </div>
          <div class="login-comp my-3">
            <p class="label"><label for="password">비밀번호</label></p>
            <input v-model="credentials.password" class="input-box" type="password" id="password" required />
          </div>
          <div class="login-comp">
            <button id="login-btn" class="my-3">Login</button>
          </div>
        </div>
        
        <div class="d-flex justify-content-end mx-5">
          <a href=""><p>아이디 찾기</p></a>
          <p class="mx-2" style="color:white">|</p>
          <a href=""><p>비밀번호 재설정</p></a>
        </div>
        <br><br><br>
        <div id="auth-div">
          <ul>  
            <li>
              <router-link class="Oauth-btn my-1 btn" style="background: #EA4335; color:white; text-decoration:none;" :to="{ name: '' }"><p class="my-2">Google로 시작하기</p></router-link>
            </li>
            <li>
              <router-link class="Oauth-btn my-1 btn" style="background:yellow; color:black; text-decoration:none;" :to="{ name: '' }"><p class="my-2">카카오로 시작하기</p></router-link>
            </li>
            <li>
              <router-link class="Oauth-btn my-1 btn" style="background: #2DB400; color:black; text-decoration:none;" :to="{ name: '' }"><p class="my-2">네이버로 시작하기</p></router-link>
            </li>
            <li>
              <router-link class="Oauth-btn my-1 btn" style="background: #B5ACAC; color:white; text-decoration:none;" :to="{ name: 'signup' }"><p class="my-2">회원가입</p></router-link>
            </li>
          </ul>


        </div>
      </form>
    
    </div>
  </div>
</template>



<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>
ul {
 list-style: none; 
}
a {
    color: white;
    text-decoration: none;
    
}
#login-box{  
  width: 566px;
  height: 748px;
  background-color: #7A7373;
  border: #7A7373;
  border-radius: 10px;
}
#username{
  margin-bottom: 10px;
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
  margin-top:5px;
  height: 90px;
}
.Oauth-btn{
  width: 294px;
  height: 51px;
  border: #7A7373;
  border-radius: 7px;
}

.label {
  color:white;
  margin-left:3rem !important;
  text-align: start !important;
}

p {
  margin:0;
}

</style>








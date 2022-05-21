<template>
  <div id="userinfo">
    <div id="background"></div>
    <div id="user-profile-image">
      <img src="" alt="">
    </div>
    <div style="height:85px;"></div>
    <h2>{{ username }}</h2>    
  </div>
</template>

<script>
export default {
  name: 'MypageHeader',
  props:{
    username:String
  }
}
</script>

<style scoped>
#userinfo {
  position:relative;
}

#background {
  background-color: #B5ACAC;
  width:100%;
  height: 300px;
}

#user-profile-image {
  border: solid 3px black;
  position: absolute;
  background: #B5ACAC;
  top: 225px;
  left: 44.212%;
  width:150px;
  height: 150px;
  border-radius: 100%;
}

h2 {
  text-align: center;
  font-weight: bold;
  color:white;
}

</style>
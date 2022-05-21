<template>
  <div id="mypagenav">
    <nav>
      <div class="nav nav-tabs d-flex justify-content-center" id="nav-tab" role="tablist">
        <button class="nav-link active" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button" role="tab" aria-controls="nav-home" aria-selected="true">프로필</button>
        <button class="nav-link" id="nav-wishlist-tab" data-bs-toggle="tab" data-bs-target="#nav-wishlist" type="button" role="tab" aria-controls="nav-profile" aria-selected="false">위시리스트</button>
        <button class="nav-link" id="nav-collections-tab" data-bs-toggle="tab" data-bs-target="#nav-collections" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">컬렉션</button>
        <button class="nav-link" id="nav-reviews-tab" data-bs-toggle="tab" data-bs-target="#nav-reviews" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">리뷰</button>
        <button class="nav-link" id="nav-bingo-tab" data-bs-toggle="tab" data-bs-target="#nav-bingo" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">빙고</button>
      </div>
    </nav>
    <div class="tab-content" id="nav-tabContent">
      <div class="tab-pane fade show active" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
        <profile-overview :profile="profile"></profile-overview>
      </div>
      <div class="tab-pane fade active" id="nav-wishlist" role="tabpanel" aria-labelledby="nav-wishlist-tab">
        <wish-list :movies="profile.wish_movies" :username="profile.username"></wish-list>
      </div>
      <div class="tab-pane fade active" id="nav-collections" role="tabpanel" aria-labelledby="nav-collections-tab">
        <user-collections :collections="ordered_collections"></user-collections>
      </div>
      <div class="tab-pane fade active" id="nav-reviews" role="tabpanel" aria-labelledby="nav-reviews-tab">
        Reviews
      </div>
      <div class="tab-pane fade active" id="nav-bingo" role="tabpanel" aria-labelledby="nav-bingo-tab">
        Bingos
      </div>
    </div>
  </div>
  
</template>

<script>
import ProfileOverview from './nav/ProfileOverview'
import WishList from './nav/WishList'
import UserCollections from './nav/UserCollections'

export default {
  name: 'MypageNav',
  props:{
    profile:Object,
  },
  components:{
    ProfileOverview,
    WishList,
    UserCollections,
  },
  computed: {
    ordered_collections() {
      return [...this.profile.collections].sort(function(a, b) {
        return a.like_users_cnt > b.like_users_cnt ? -1 : a.like_users_cnt < b.like_users_cnt ? 1 : 0;
      }) 
    }
  },
}
</script>

<style scoped>
  #mypagenav{
    margin-left:auto;
    margin-right:auto;
    margin:50px;
  }
  #nav-list{
    width:800px;

  }
  .nav-link {
    color:white;
    border: black;
    margin-left:15px;
    margin-right:15px;
  }
  .nav-link:hover {
    font-weight: bold;
    border: none;
  }

  .tab-pane {
    color:white
  } 
 
</style>
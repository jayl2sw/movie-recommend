<template>
  <div>
    <div id="reviews">
      <review-creation-form></review-creation-form>
    </div>
  </div>
</template>

<script>
// import { mapGetters } from 'vuex'
// import axios from 'axios'
import ReviewCreationForm from './ReviewCreationForm'
export default {
  name: "MovieReview",
  components:{
    ReviewCreationForm,
  },
  props:{
  },
  computed: {
  }
}

</script>

<style scoped>

  
</style>
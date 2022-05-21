<template>
  <div id="review-creation-form">  
    <form @submit.prevent="onSubmit" class="row">
      <div class="col-2">
        <select class="form-select" aria-label="Default select example">
          <option value="1"></option>
          <option value="5"><i class="bi bi-alarm"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i></option>
          <option value=4.5><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star"></i></option>
          <option value=4><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star"></i></option>
          <option value=3.5><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-half"></i><i class="bi bi-star"></i></option>
          <option value=3><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star"></i><i class="bi bi-star"></i></option>
          <option value=2.5><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-half"></i><i class="bi bi-star"></i><i class="bi bi-star"></i></option>
          <option value=2><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star"></i><i class="bi bi-star"></i><i class="bi bi-star"></i></option>
          <option value=1.5>aa<i class="bi bi-star-fill"></i><i class="bi bi-star-half"></i><i class="bi bi-star"></i><i class="bi bi-star"></i><i class="bi bi-star"></i></option>
          <option value=1><i class="bi bi-star-fill"></i><i class="bi bi-star"></i><i class="bi bi-star"></i><i class="bi bi-star"></i><i class="bi bi-star"></i></option>
        </select>
      </div>
      <div class="col-8">
        <input type="text" class="form-control" v-model="review.content" id="content" />
      </div>
      <div class="col-2">
        <button class="btn">작성</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "ReviewCreationForm",
  data(){
    return {
      review:{
        rate: 0,
        content:'',
      }
    }
  },
  props:{
  },
  computed: {
  }
}

</script>

<style scoped>
option {
  color:black;

}
  
</style>
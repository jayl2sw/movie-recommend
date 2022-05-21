<template>
  <div class="container">
    <div class="row">
      <div id="overview_bingo" class="col mx-1 my-3">
      </div>
      <div class="col my-3">
        <div class="row">
          <div id="overview_analysis" class="col mx-1 px-3">
            준비중입니다.
          </div>  
          <div id="overview_recent_review" class="col mx-1 px-3">
            <div v-for="collection in profile.like_collections" :key="collection.pk">
              {{ collection.pk }}
            </div>
          </div>
        </div>
        <div class="row">
          <div id="overview_collections" class="col mx-1 my-2">
            <div v-for="collection in profile.collections" :key="collection.pk">
              {{ collection.pk }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name:'ProfileOverview',
  props: {
    profile:Object,
  },
}
</script>

<style scoped>
#overview_bingo { 
  width: 38rem;
  height: 38rem;
  border-radius: 10px;
  background: #B5ACAC;
}
#overview_analysis { 
  width: 25rem;
  height: 18.65rem;
  border-radius: 10px;
  background: #B5ACAC;
}
#overview_recent_review { 
  width: 25rem;
  height: 18.65rem;
  border-radius: 10px;
  background: #B5ACAC;
}
#overview_collections{
  width: 25rem;
  height: 18.65rem;
  border-radius: 10px;
  background: #B5ACAC;
}
</style>


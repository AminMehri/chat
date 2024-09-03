<template>
  <div class="home">
    <div class="container-fluid">
      <div class="row">
        <div class="col-3">
          <Conversations />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Conversations from '@/components/Conversations.vue'

export default {
  name: 'HomeView',
  components: {
    Conversations
  }
}
</script>

<style scoped>

</style>
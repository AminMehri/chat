<template>
  <div class="home">
    <div class="container-fluid">
      <div class="row">
        <div class="col-3">
          <router-link to="/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="">Amin</span>
              <p>hello kay kay how are you doing today?</p>
            </div>
          </router-link>
          <router-link to="/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="">Amin</span>
              <p>hello kay kay how are you doing today?</p>
            </div>
          </router-link>
          <router-link to="/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="">Amin</span>
              <p>hello kay kay how are you doing today?</p>
            </div>
          </router-link>
          <router-link to="/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="">Amin</span>
              <p>hello kay kay how are you doing today?</p>
            </div>
          </router-link>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>

<style scoped>
.profile-img{
  height: 75px;
  width: 75px;
}
.open-chat:hover{
  background-color: rgb(170, 170, 170);
  transition-duration: 0.2s;
}

a {
  text-decoration: none;
  color: black;
}

.host-message {
  background-color: aqua;
  width: 25%;
}

.guest-message {
  background-color: rgb(224, 241, 122);
  width: 25%;
}
</style>
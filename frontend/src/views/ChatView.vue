<template>
    <div class="home">
      <div class="container-fluid">
        <div class="row">
          <div class="col-3">
            <router-link to="/chat/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="d-block">Amin</span>
              <p class="d-inline">hello kay kay how are you doing today?</p>
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-check float-end" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg>
            </div>
          </router-link>
          <router-link to="/chat/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="d-block">Amin</span>
              <p class="d-inline">hello kay kay how are you doing today?</p>
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-check-all float-end" viewBox="0 0 16 16">
                <path d="M8.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L2.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093L8.95 4.992a.252.252 0 0 1 .02-.022zm-.92 5.14.92.92a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 1 0-1.091-1.028L9.477 9.417l-.485-.486-.943 1.179z"/>
              </svg>
            </div>
          </router-link>
          <router-link to="/chat/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="">Amin</span>
              <p>hello kay kay how are you doing today?</p>
            </div>
          </router-link>
          <router-link to="/chat/aminmehri" class="row g-0 open-chat">
            <div class="col-3">
              <img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
            </div>
            <div class="col-9">
              <span class="">Amin</span>
              <p>hello kay kay how are you doing today?</p>
            </div>
          </router-link>
          </div>
          <div class="col-9">
            <p class="host-message rounded py-1 px-2">hello asd ASD asd asd asd asd asd asd asd S ASd asd asd asd ASd asd as aS dasd A Sdasd a da s</p>
            <p class="guest-message me-0 ms-auto text-end rounded py-1 px-2 ">hiii</p>
            <p class="host-message rounded py-1 px-2">hello asd ASD asd asd asd asd asd asd asd S ASd asd asd asd ASd asd as aS dasd A Sdasd a da s</p>
            <p class="guest-message me-0 ms-auto text-end rounded py-1 px-2">hiii</p>
            <p class="host-message rounded py-1 px-2">hello asd ASD asd asd asd asd asd asd asd S ASd asd asd asd ASd asd as aS dasd A Sdasd a da s</p>
            <p class="guest-message me-0 ms-auto text-end rounded py-1 px-2">hiii</p>
            <p class="guest-message me-0 ms-auto text-end rounded py-1 px-2">hiii</p>
            <p class="guest-message me-0 ms-auto text-end rounded py-1 px-2">hiii</p>

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
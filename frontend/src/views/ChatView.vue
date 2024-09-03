<template>
  <div class="home">
    <div class="container-fluid">
      <div class="row">
        <div class="col-3">
          <Conversations />
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
          
          <input type="text" class="w-75" placeholder="message">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send mx-2 pointer-cursor" viewBox="0 0 16 16">
            <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576 6.636 10.07Zm6.787-8.201L1.591 6.602l4.339 2.76 7.494-7.493Z"/>
          </svg>

        </div>          
      </div>
    </div>
  </div>
</template>
  
<script>
import Conversations from '@/components/Conversations.vue'

export default {
  name: 'ChatView',
  components: {
    Conversations
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

  .pointer-cursor{
    cursor: pointer;
  }
  </style>
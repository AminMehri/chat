<template>
	<router-link v-for="conv in convers" :to="`/chat/${conv.id}`" class="row g-0 open-chat">
		<div class="col-3">
			<img src="../assets/groot-moraba.jpg" class="img-thumbnail rounded-circle profile-img">
		</div>
		<div class="col-9">
			<span class="d-block">{{conv.contact}}</span>
			<p class="d-inline">{{conv.last_message}}</p>
			<svg v-if="!conv.is_seen" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-circle-fill text-danger" viewBox="0 0 16 16">
				<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/>
			</svg>
			<svg v-if="conv.last_by_me == true & conv.contact_seen == false" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-check float-end" viewBox="0 0 16 16">
				<path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
			</svg>
			<svg v-if="conv.last_by_me == true & conv.contact_seen == true" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-check-all float-end" viewBox="0 0 16 16">
				<path d="M8.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L2.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093L8.95 4.992a.252.252 0 0 1 .02-.022zm-.92 5.14.92.92a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 1 0-1.091-1.028L9.477 9.417l-.485-.486-.943 1.179z"/>
			</svg>
		</div>
	</router-link>
</template>

<script>
import { ref ,watch } from "vue";
import axios from 'axios'

export default {
	setup() {
		let convers = ref('')
		axios
		.get('chat/Conversation/')
		.then(response =>{
			convers.value = response.data
		})
		.catch(error => {
			console.log(error.response.data);
		})

		return {
			convers,
		}
	},
	
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
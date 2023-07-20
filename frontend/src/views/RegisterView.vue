<template>
    <div class="register">
  
      <div v-if="fullScreenLoading" class="fullscreen-loading">Loading&#8230;</div>
  
      <div class="container">
        <p class="text-danger">Welcome to the city of lie!</p>
        <div class="card mx-auto" style="width: 25rem;">
          <img src="@/assets/groot.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <!-- register form -->
            <form @submit.prevent="doRegister()">
              <div class="form-floating mb-3" lang="en">
                <input 
                  v-model="username" 
                  type="text" 
                  class="form-control" 
                  id="floatingUsername" 
                  placeholder="نام کاربری"
                  :class="{'is-invalid':usernameE===true, 'is-valid':usernameE===false}"
                >
  
                <label for="floatingUsername">Username</label>
                <div class="invalid-feedback">
                  {{ usernameEM }}
                </div>
              </div>

              <div class="form-floating mb-3" lang="en">
                <input 
                  v-model="email" 
                  type="text" 
                  class="form-control" 
                  id="floatingEmail" 
                  placeholder="email"
                  :class="{'is-invalid':emailE===true, 'is-valid':emailE===false}"
                >
  
                <label for="floatingEmail">Email</label>
                <div class="invalid-feedback">
                  {{ emailEM }}
                </div>
              </div>
  
              <div class="form-floating mb-3" lang="en">
                <input 
                  v-model="password" 
                  type="password" 
                  class="form-control" 
                  id="floatingPassword1" 
                  placeholder="رمز عبور"
                  :class="{'is-invalid':passwordE===true, 'is-valid':passwordE===false}"
                >
  
                <button type="button" @click="showPassword('floatingPassword1')" class="btn position-absolute top-50 end-0 translate-middle-y"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16"><path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/><path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/></svg></button>
  
                <label for="floatingPassword1">Password</label>
                <div class="invalid-feedback">
                  {{ passwordEM }}
                </div>
              </div>
  
              <div class="form-floating position-relative" lang="en">
                <input 
                  v-model="passwordConfirm" 
                  type="password" 
                  class="form-control" 
                  id="floatingPassword2" 
                  placeholder="رمز عبور"
                  :class="{'is-invalid':passwordConfirmE===true, 'is-valid':passwordConfirmE===false}"
                >
  
                <button type="button" @click="showPassword('floatingPassword2')" class="btn position-absolute top-50 end-0 translate-middle-y"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16"><path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/><path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/></svg></button>
  
                <label for="floatingPassword2">Password confirm</label>
                <div class="invalid-feedback">
                  {{ passwordConfirmEM }}
                </div>
              </div>

              <button type="submit" class="btn btn-outline-dark mt-2 mb-4">Register</button>
  
            </form>
            <!-- end register form -->
  
            <div class="d-flex justify-content-between">
  
              <router-link to="/login" class="text-dark hover-underline">Login</router-link>
  
            </div>
  
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import { useStore } from 'vuex'
  import { useRouter } from 'vue-router'
  import Swal from 'sweetalert2'
  import axios from 'axios'
  
  export default {
    name: 'HomeView',
    setup() {
      const store = useStore()
      const router = useRouter()
  
      let username = ref('')
      let password = ref('')
      let passwordConfirm = ref('')
      let email = ref('')
      let usernameE = ref()
      let passwordE = ref()
      let passwordConfirmE = ref()
      let emailE = ref()
      let usernameEM = ref('')
      let passwordEM = ref('')
      let passwordConfirmEM = ref('')
      let emailEM = ref('')
  
      let fullScreenLoading = ref(false)
  
      // function isAuthenticated(){
      //   if(store.state.isAuthenticated){
      //     router.push('/about')
      //   }
      // }
      // isAuthenticated()

      function ValidateEmail(mail) 
      {
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail))
          {
            return (true)
          }
          return (false)
      }
  
      function doRegister() {
        let access = true
        if(username.value.length < 5){
            usernameE.value = true
            access = false
            if(username.value.length == 0){
                usernameEM.value = 'username is required'
            } else {
                usernameEM.value = 'username length must be at least 5 character'
            }
        } else {
            usernameE.value = false
            usernameEM.value = ''
        }

        if(!ValidateEmail(email.value)){
          emailE.value = true
          access = false
          if(email.value.length == 0){
            emailEM.value = 'email is required'
          } else {
            emailEM.value = 'please enter a valid email'
          }
        } else{
          emailE.value = false
          emailEM.value = ''
        }
  
        if(password.value.length < 8){
            passwordE.value = true
            access = false
            if(password.value.length == 0){
                passwordEM.value = 'password is required'
            } else {
                passwordEM.value = 'passsword must be at least 8 character'
            }
        } else {
            passwordE.value = false
            passwordEM.value = ''
        }
        
        if(password.value != passwordConfirm.value){
            access = false
            passwordE.value = true
            passwordConfirmE.value = true
            passwordEM.value = 'password and password confirm are not match'
        } else {
            if(!passwordE.value && passwordConfirmE.value) {
                access = true
            }
        }

        if(access){
          fullScreenLoading.value = true
          axios
          .post('account/signup/', {
              username: username.value,
              password: password.value,
              email: email.value,
          })
          .then(response => {
            fullScreenLoading.value = false
            Swal.fire({
                icon: 'success',
                title: 'register successfully',
                text: 'please check your email',
            })
            router.push('/login')
          })
          .catch(error => {
            fullScreenLoading.value = false
            console.log(error.response);
            usernameE.value = true
            passwordE.value = true
          })
  
        }
      }   
      
    function showPassword(id) {
      let x = document.querySelector(`#${id}`);
      if (x.type === "password") {
          x.type = "text";
      } else {
          x.type = "password";
      }
    }
  
      return{
        username,
        password,
        passwordConfirm,
        email,
        usernameE,
        passwordE,
        passwordConfirmE,
        emailE,
        usernameEM,
        passwordEM,
        passwordConfirmEM,
        emailEM,
        fullScreenLoading,
        doRegister,
        showPassword,
      }
    }
  }
  </script>
  
  
  <style scoped>
  *{
    text-align: center;
  }
  a{
    text-decoration: none;
  }
  </style>
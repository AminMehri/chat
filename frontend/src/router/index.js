import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ConfirmEmailView from '../views/ConfirmEmailView.vue'
import ChatView from '../views/ChatView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { loginRequired: true }
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    meta: { loginRequired: true }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { loginRedirect: true }
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    meta: { loginRedirect: true }
  },
  {
    path: '/confirmEmail/:token/:id',
    name: 'confirm_email',
    component: ConfirmEmailView,
  },
  {
    path: '/chat/:id',
    name: 'chat_view',
    component: ChatView,
    meta: { loginRequired: true }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.loginRequired)) {
    if (store.state.isAuthenticated) {
      next()
    } else {
      next("/login")
    }
  }else if (to.matched.some(record => record.meta.loginRedirect)) {
    if (store.state.isAuthenticated) {
      next("/")
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
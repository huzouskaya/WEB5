import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import Diary from '../components/Diary.vue'
// import Register from '../components/Register.vue';
// import Login from '../components/Login.vue';
import { defineStore } from 'pinia'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // { path: '/register', component: Register },
    // { path: '/login', component: Login },
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    { path: '/login',
      name: 'login',
      component: LoginView,
    },
    { path: '/register',
      name: 'register',
      component: RegisterView,
    },
    {
      path: '/diary',
      name: 'Diary',
      component: Diary,
    },
  ],
})

export default router;

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null as string | null,
  }),
  actions: {
    setToken(token: string) {
      this.token = token;
    },
  },
});
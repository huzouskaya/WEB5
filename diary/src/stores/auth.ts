import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null as string | null, 
    username: null as string | null,
    avatar: null as string | null,
    isAuthenticated: false,
  }),
  actions: {
    setToken(token: string) {
      this.token = token;
      this.isAuthenticated = !!token;
    },
    setUser (username: string, avatar: string) {
      this.username = username;
      this.avatar = avatar;
    },
    logout() {
      this.token = null;
      this.username = null;
      this.avatar = null;
      this.isAuthenticated = false;
    },
  },
});
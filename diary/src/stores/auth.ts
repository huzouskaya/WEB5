import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null as string | null, 
    username: null as string | null,
    avatar: null as string | null,
  }),
  actions: {
    setToken(token: string) {
      this.token = token;
    },
    setUser (username: string, avatar: string) {
      this.username = username;
      this.avatar = avatar;
    },
    logout() {
      this.token = null;
      this.username = null;
      this.avatar = null;
    },
  },
});
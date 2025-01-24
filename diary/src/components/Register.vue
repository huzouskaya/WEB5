<!-- src/components/Register.vue -->
<template>
    <form @submit.prevent="register">
        <input v-model="username" placeholder="Username" required />
        <input v-model="email" type="email" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Register</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            username: '',
            email: '',
            password: ''
        };
    },
    methods: {
        async register() {
            try {
                const response = await axios.post('http://localhost:8000/register/', {
                    username: this.username,
                    email: this.email,
                    password: this.password
                });
                console.log('User  registered:', response.data);
            } catch (error) {
                console.error('Registration error:', error.response.data);
            }
        }
    }
};
</script>
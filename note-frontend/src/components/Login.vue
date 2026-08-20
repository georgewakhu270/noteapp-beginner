<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'

const username = ref('')
const password = ref('')
const error = ref(null)
const loading = ref(false)

const router = useRouter()

const handleLogin = async () => {
    error.value = null
    loading.value = true
    try {
        // Django needs a CSRF cookie set before it will accept the POST
        await api.getCsrfToken()
        const response = await api.login(username.value, password.value)
        console.log('Logged in as', response.data.username)
        router.push({ name: 'notes' })   // adjust to your route name
    } catch (err) {
        if (err.response?.status === 400) {
            error.value = 'Invalid username or password'
        } else {
            error.value = 'Something went wrong. Please try again.'
        }
        console.error('Login error:', err)
    } finally {
        loading.value = false
    }
}
</script>

<template>
    <div class="login-page">
        <h1>Log In</h1>

        <form @submit.prevent="handleLogin">
            <div>
                <label for="username">Username</label>
                <input id="username" v-model="username" type="text" required />
            </div>

            <div>
                <label for="password">Password</label>
                <input id="password" v-model="password" type="password" required />
            </div>

            <div v-if="error" class="error">{{ error }}</div>

            <button type="submit" :disabled="loading">
                {{ loading ? 'Logging in...' : 'Log In' }}
            </button>
        </form>
    </div>
</template>

<style scoped>
.error {
    color: red;
    margin: 0.5rem 0;
}
</style>
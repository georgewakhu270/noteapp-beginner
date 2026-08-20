import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import AllNotes from "../components/AllNotes.vue";
import api from "../services/api.js";

const routes = [
    {path: '/login', name: 'login',  component: Login},
    {path: '/notes', name: 'notes', component: AllNotes, meta: { requiresAuth: true }},
    {path: '/', redirect: '/login'},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach(async (to) => {
    if (!to.meta.requiresAuth) return true

    try {
        const response = await api.getCurrentUser()
        if (response.data.username) {
            return true
        }
        return {name: 'login'}
    } catch(err) {
        return {name: 'login'}
    }
})

export default router;

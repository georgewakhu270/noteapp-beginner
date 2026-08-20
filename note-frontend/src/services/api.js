import axios from 'axios'

const API = axios.create({
    baseURL: 'http://localhost:8000/api/',
    withCredentials: true,
})

function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'))
    return match ? match[2] : null
}

API.interceptors.request.use((config) => {
    const csrfToken = getCookie('csrftoken')
    if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken
    }
    return config
})

export default {
    getCsrfToken() {
        return API.get('csrf/')
    },
    login(username, password) {
        return API.post('login/', { username, password })
    },
    logout() {
        return API.post('logout/')
    },
    getCurrentUser() {
        return API.get('user/')
    },
    getNotes() {
        console.log('url entered')
        return API.get('notes/')
    },
    createNote(noteData) {
        return API.post('notes/', noteData)
    },
    deleteNote(id) {
        return API.delete(`notes/${id}`)
    }
}

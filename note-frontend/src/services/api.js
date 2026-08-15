import axios from 'axios'

const API = axios.create({
    baseURL: 'http://localhost:8000/api/',
    withCredentials: true,
})

export default {
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
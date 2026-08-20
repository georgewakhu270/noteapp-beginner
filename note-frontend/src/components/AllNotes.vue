<script setup>
import {ref, onMounted} from 'vue'
import api from '../services/api'

const notes = ref([])
const loading = ref(true)
const err = ref(null)

const fetchNotes = async () => {
    loading.value = true
    err.value = null
    try {
        const response = await api.getNotes()
        notes.value = response.data
    } catch (err) {
        console.error('Error fetching notes:', err)
        err.value = 'Failed to load notes. Make sure you are logged in'
    } finally {
        loading.value = false
    }
}

const deleteNote = async (noteId) => {
    try {
        await api.deleteNote(noteId)
        notes.value = notes.value.filter(note => note.id !== noteId)
    } catch (err) {
        console.error('Error deleting note:', err)
        err.value = 'Failed to delete note. Make sure you are logged in'
    }
}

onMounted(() => {
    fetchNotes()
})
</script>

<template>
    <h1>Notes</h1>
    <div v-if="loading">Loading notes...</div>
    <div v-if="err" class="alert alert-danger">{{ err }}</div>

    <div v-if="notes.length === 0">No notes found</div>
    <div v-for="note in notes" :key="note.id">
        <h3>{{ note.title }}</h3>
        <p>{{ note.body }}</p>
        <small>By: <strong>{{ note.author?.username || 'Unknown' }}</strong> | {{ new Date(note.created_at).toLocaleString() }}</small>
        <br>
        <button @click="() => deleteNote(note.id)">delete</button>
    </div>
</template>

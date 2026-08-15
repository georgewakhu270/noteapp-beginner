<script setup>
import {ref, onMounted} from 'vue'
import api from '../services/api'
const notes = ref([])

const fetchNotes = async () => {
    try {
        const response = await api.getNotes()
        notes.value = response.data
    } catch (err) {
        console.error('Error fetching notes:', err)
        err.value = 'Failed to load notes. Make sure you are logged in'
    }
}
</script>

<template>
    <h1>Notes</h1>
    <div v-if="notes.length === 0">No notes found</div>
    <div v-for="note in notes" :key="note.id">
        <h3>{{ note.title }}</h3>
        <p>{{ note.body }}</p>
        <small>By: <strong>{{ note.author?.username || 'Unknown' }}</strong> | {{ new Date(note.created_at).toLocaleString() }}</small>
        <br>
        <button @click="">delete</button>
    </div>
</template>

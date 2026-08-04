from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.utils.timezone import datetime
from django.urls import reverse_lazy

from .models import Note

# Create your views here.

class NoteView(ListView):
    model = Note
    template_name = 'mynote/view.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'mynote/detail.html'

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'mynote/update.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.updated_at = datetime.isoformat(datetime.now())
        return super().form_valid(form)


class NoteCreateView(CreateView):
    model = Note
    template_name = 'mynote/new.html'
    fields = ['title', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_at = form.instance.updated_at = datetime.isoformat(datetime.now())
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'mynote/delete.html'
    success_url = reverse_lazy('note_view')

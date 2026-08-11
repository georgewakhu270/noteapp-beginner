from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.timezone import datetime
from django.urls import reverse_lazy

from .models import Note

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class AboutPage(TemplateView):
    template_name = 'about.html'
    
class NoteView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'mynote/view.html'

    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'mynote/detail.html'

    login_url = reverse_lazy('login')

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'mynote/update.html'
    fields = ['title', 'body']

    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.updated_at = datetime.isoformat(datetime.now())
        messages.success(self.request, 'Updated your note')
        return super().form_valid(form)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'mynote/new.html'
    fields = ['title', 'body']

    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_at = form.instance.updated_at = datetime.isoformat(datetime.now())
        messages.success(self.request, "Created a new note")
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'mynote/delete.html'
    success_url = reverse_lazy('note_view')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Your note was successfully deleted')
        return super().form_valid(form)

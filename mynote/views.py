# the django
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.timezone import datetime
from django.urls import reverse_lazy

# for django-rest
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics

from .serializers import NoteSerializer

# models
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
        messages.success(self.request, 'Updated your note')
        return super().form_valid(form)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'mynote/new.html'
    fields = ['title', 'body']

    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
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


# the views of api
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the currently authenticated user
        serializer.save(author=self.request.user)
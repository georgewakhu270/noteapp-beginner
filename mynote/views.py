# the django
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.middleware.csrf import get_token

from django.utils.timezone import datetime
from django.urls import reverse_lazy

# for django-rest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

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
class CSRFTokenView(APIView):
    """Vue calls this first to get the CSRF token and set it in the cookies"""
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'csrfToken': get_token(request)})

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return Response({'message': 'Login successful' , 'username': user.username})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Logged out'})

class CurrentUserView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user.is_authenticated:
            return Response({'username': request.user.username})
        else:
            return Response({'username': None})

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the currently authenticated user
        serializer.save(author=self.request.user)

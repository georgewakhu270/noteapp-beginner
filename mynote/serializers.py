from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class NoteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at']
        read_only = ['created_at','updated_at']

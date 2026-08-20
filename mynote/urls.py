from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note_api')

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('notes/', NoteView.as_view(), name='note_view'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('notes/new/', NoteCreateView.as_view(), name='note_new'),
    path('notes/<int:pk>/delete', NoteDeleteView.as_view(), name='note_delete'),

    # path('api/notes', NoteListSerializerView.as_view(), name='api_get')
    path('api/', include(router.urls)),
    path('api/csrf/', CSRFTokenView.as_view(), name='api_csrf'),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/user/', CurrentUserView.as_view(), name='api_user'),

]

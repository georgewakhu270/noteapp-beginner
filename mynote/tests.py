from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.timezone import datetime
from django.urls import reverse

from .models import Note

# Create your tests here.

class NoteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.now = datetime.isoformat(datetime.now())
        cls.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com', password='secret'
        )
        cls.note = Note.objects.create(
            title='my title',
            body='my body',
            author=cls.user,
            created_at=cls.now,
            updated_at=cls.now
        )

    def test_post_mode(self):
        self.assertEqual(self.note.title, 'my title')
        self.assertEqual(self.note.created_at, self.now)

    def test_create_mode(self):
        pass

    def test_update_mode(self):
        pass

    def test_read_mode(self):
        request = self.client.get(reverse('note_view'))
        self.assertEqual(request.status_code, 200)

    def test_delete_mode(self):
        pass


from django.db import models
from django.urls import reverse

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'pk': self.pk})

    def reduce_body(self):
        return self.body[:100]

    @property
    def short_body(self):
        if len(self.body) > 100:
            return f"{self.body[:100]}"
        return self.body

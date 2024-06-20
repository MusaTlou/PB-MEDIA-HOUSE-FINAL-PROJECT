# contact/models.py
from django.db import models

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

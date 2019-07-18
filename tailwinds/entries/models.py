import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    entry = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'entries'

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User





class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content

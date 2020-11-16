from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=4000)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

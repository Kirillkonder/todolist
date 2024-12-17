from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=255)


class Todo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):  
        return self.title






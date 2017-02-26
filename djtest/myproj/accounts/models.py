from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255)


class FakeUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        


from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CreateUser(AbstractUser):

    ACCOUNT = (
        ('basic', 'basic'),
        ('premium', 'premium'),
        ('diamond', 'diamond')
    )


    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=ACCOUNT, default='basic')

def __str__(self):
    return self.username


from django.db import models

from django.contrib.auth.models import User
from .models import Profile

# Create your models here.

class UpdateUser(models.ModelForm):
    username = models.CharField(max_length=100, required=False, widget=models.TextInput(attrs={'class': 'form-control'}))
    email = models.EmailField(required=True, widget=models.TextInput(attrs={'class': 'form-contorl'}))

    class Meta:
        model = User
        fields = ['name', 'email']


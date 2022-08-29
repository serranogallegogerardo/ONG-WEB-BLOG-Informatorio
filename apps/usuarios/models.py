from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuario',default='usuario/user_default.png')

    def get_absolute_url(self):
        return reverse('index')
from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class User(AbstractUser):
    permissions = None
    groups = None
    first_name = None
    last_name = None
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.username
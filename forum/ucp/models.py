from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.username
    
class Players(models.Model):
    nameuser = models.CharField(max_length=100)
    emailuser = models.EmailField(max_length=100)
    password_one = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nameuser
    

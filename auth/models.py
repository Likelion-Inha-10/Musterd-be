from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False)
    profile_image = models.ImageField(blank=False)
    username = models.CharField(blank=False)
    univ = models.CharField(blank=False)

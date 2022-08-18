from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, username , univ , **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            username = username,
            univ = univ
             
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, email=None, password=None,univ=None,**extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
            username=username,
            univ=univ,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(('email address'), unique=True,null = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    password = models.CharField(max_length=30,blank=False)
    profile_image = models.ImageField(blank=True)
    username = models.CharField(max_length=30,null=True)
    univ = models.CharField(max_length=30,null=True)
    point = models.IntegerField(null=True)


    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    def is_staff(self):
        return True
    

    
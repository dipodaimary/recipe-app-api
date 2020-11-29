from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fileds):
        """Creates and saves new user"""
        if not email:
            raise ValueError('Users must have an email addresss')
        user = self.model(email=self.normalize_email(email), **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Creates and save new users"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
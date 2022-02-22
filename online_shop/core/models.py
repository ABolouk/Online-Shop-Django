from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class MyUserManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):
        self.username = extra_fields["phone"]
        return super()._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields["phone"]
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = MyUserManager()

    phone = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "phone"

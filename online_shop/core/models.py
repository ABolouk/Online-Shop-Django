from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields["phone"]
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = MyUserManager()

    phone = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "phone"


class BaseManager(models.Manager):

    def full_archive(self):
        return super().get_queryset()

    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_delete = models.BooleanField(default=False, editable=False, db_index=True)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save(using=using)

    def restore(self):
        self.is_delete = False
        self.save()

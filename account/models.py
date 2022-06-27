from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(max_length=128, verbose_name="e-мэйл", unique=True)


    def save(self, *args, **kwargs):
        self.email = self.username
        super(User, self).save(*args, **kwargs)
        
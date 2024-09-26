from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="student")
    group_number = models.CharField(max_length="25")


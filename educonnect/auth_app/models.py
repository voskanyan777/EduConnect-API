from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="student")
    group_number = models.CharField(max_length=25)

    # Переопределение строки
    email = models.EmailField(blank=True, unique=True)

    # Добавляем related_name для полей groups и user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True
    )

    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

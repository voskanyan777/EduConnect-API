from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="student")
    group_number = models.CharField(max_length=25)

    # Добавляем related_name для полей groups и user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Уникальное имя для обратной связи
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Уникальное имя для обратной связи
        blank=True
    )

    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Course(models.Model):
    name = models.CharField(max_length=90, null=False)
    description = models.CharField(max_length=350)
    available_groups = models.JSONField()
    created_by_teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'Courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Task(models.Model):
    name = models.CharField(max_length=90, null=False)
    description = models.CharField(max_length=350, null=False)
    for_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    created_by_teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Group(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    group_number = models.CharField(max_length=25, null=False)
    students_count = models.IntegerField()

    class Meta:
        db_table = 'Groups'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

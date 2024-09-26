from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="student")
    group_number = models.CharField(max_length="25")


class Course(models.Model):
    name = models.CharField(max_length=90, null=False)
    description = models.CharField(max_length=350)
    available_groups = models.JSONField()
    created_by_teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Task(models.Model):
    name = models.CharField(max_length=90, null=False)
    description = models.CharField(max_length=350, null=False)
    for_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    created_by_teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Group(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    group_number = models.CharField(max_length=25, null=False)
    students_count = models.IntegerField()

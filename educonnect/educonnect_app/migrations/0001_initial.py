# Generated by Django 5.1.1 on 2024-09-26 14:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=350)),
                ('available_groups', models.JSONField()),
                ('created_by_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'db_table': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.CharField(max_length=25)),
                ('students_count', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=350)),
                ('created_by_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('for_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educonnect_app.course')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'Tasks',
            },
        ),
    ]

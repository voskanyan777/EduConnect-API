# Generated by Django 5.1.1 on 2024-10-31 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educonnect_app', '0005_groupnumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupnumber',
            options={'verbose_name': 'Group Number', 'verbose_name_plural': 'Group Numbers'},
        ),
        migrations.AlterModelTable(
            name='groupnumber',
            table='GroupNumbers',
        ),
    ]

# Generated by Django 5.2 on 2025-05-06 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dochazka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]

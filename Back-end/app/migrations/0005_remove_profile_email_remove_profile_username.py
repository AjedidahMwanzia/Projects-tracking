# Generated by Django 4.0.5 on 2022-07-03 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-02 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='app.project'),
        ),
    ]

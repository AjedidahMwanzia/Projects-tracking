
# Generated by Django 4.0.5 on 2022-07-02 08:44


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('admission_date', models.DateTimeField(auto_now_add=True)),
                ('graduation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('project_link', models.URLField(max_length=20000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.TextField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField(max_length=12)),
                ('facebookLinks', models.CharField(max_length=1000, null=True)),
                ('TwitterLinks', models.CharField(max_length=10000, null=True)),
                ('GithubLinks', models.CharField(max_length=1000, null=True)),
                ('InstagramLinks', models.CharField(max_length=1000, null=True)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='app.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

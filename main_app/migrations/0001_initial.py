# Generated by Django 2.2.3 on 2019-09-13 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_link', models.CharField(max_length=100)),
                ('github_link', models.CharField(max_length=100)),
                ('about_me', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('technologies', models.TextField(max_length=200)),
                ('deployed_link', models.CharField(max_length=100)),
                ('project_link', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('portfolio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Portfolio')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Project')),
            ],
        ),
    ]

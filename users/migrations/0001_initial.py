# Generated by Django 4.2.3 on 2023-08-12 08:01

import admin.utils
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=admin.utils.get_timestamp_path)),
                ('phone', models.CharField(max_length=19, validators=[django.core.validators.MaxLengthValidator(19), django.core.validators.MinLengthValidator(19), django.core.validators.ProhibitNullCharactersValidator(), django.core.validators.RegexValidator('^\\+38 \\(\\d{3}\\) \\d{3}-?\\d{2}-?\\d{2}$', message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')])),
                ('builder', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'custom_user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_first_name', models.CharField(max_length=100)),
                ('agent_last_name', models.CharField(max_length=100)),
                ('agent_email', models.EmailField(max_length=255)),
                ('agent_phone', models.CharField(max_length=19, validators=[django.core.validators.MaxLengthValidator(19), django.core.validators.MaxLengthValidator(19), django.core.validators.MinLengthValidator(19), django.core.validators.ProhibitNullCharactersValidator(), django.core.validators.RegexValidator('^\\+38 \\(\\d{3}\\) \\d{3}-?\\d{2}-?\\d{2}$', message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')])),
                ('redirect_notifications_to_agent', models.BooleanField(default=False)),
                ('notification_type', models.CharField(choices=[('Мне', 'Мне'), ('Мне и агенту', 'Мне и агенту'), ('Агенту', 'Агенту'), ('Отключить', 'Отключить')], max_length=100)),
                ('favorite_adverts', models.ManyToManyField(related_name='favorite_adverts_set', to='client.advert')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-14 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_favorite_adverts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_type',
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, default='не указано', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, default='не указано', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='не указано', max_length=19),
        ),
    ]
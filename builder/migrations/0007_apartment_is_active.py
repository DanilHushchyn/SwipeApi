# Generated by Django 4.2.3 on 2023-08-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_chessboardaddingrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

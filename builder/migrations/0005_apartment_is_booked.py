# Generated by Django 4.2.3 on 2023-08-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_alter_apartment_price_alter_apartment_square'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0021_alter_promotion_big_advert_alter_promotion_highlight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
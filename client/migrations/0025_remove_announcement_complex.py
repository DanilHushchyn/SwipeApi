# Generated by Django 4.2.3 on 2023-08-26 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0024_remove_announcement_gallery_galleryannouncement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='complex',
        ),
    ]

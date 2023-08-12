# Generated by Django 4.2.3 on 2023-08-12 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('builder', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='complex',
            name='builder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complex',
            name='doc_kit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.dockit'),
        ),
        migrations.AddField(
            model_name='complex',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.gallery'),
        ),
    ]

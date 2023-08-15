# Generated by Django 4.2.3 on 2023-08-15 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_alter_complex_address_alter_complex_builder_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complex',
            old_name='benefit',
            new_name='benefits',
        ),
        migrations.RemoveField(
            model_name='sewer',
            name='complex',
        ),
        migrations.AddField(
            model_name='sewer',
            name='corp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='builder.corp'),
        ),
        migrations.AlterField(
            model_name='complex',
            name='ceiling_height_m',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='complex',
            name='sea_destination_m',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='corp',
            name='complex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='builder.complex'),
        ),
        migrations.AlterField(
            model_name='news',
            name='complex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='builder.complex'),
        ),
    ]
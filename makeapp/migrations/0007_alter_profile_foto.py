# Generated by Django 5.1.5 on 2025-01-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeapp', '0006_alter_profile_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, default='user/default_image.webp', null=True, upload_to='user'),
        ),
    ]

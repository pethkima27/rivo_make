# Generated by Django 5.1.5 on 2025-01-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeapp', '0005_remove_produto_user_profile_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, default='https://static.vecteezy.com/system/resources/thumbnails/048/334/475/small_2x/a-person-icon-on-a-transparent-background-png.png', null=True, upload_to='user'),
        ),
    ]

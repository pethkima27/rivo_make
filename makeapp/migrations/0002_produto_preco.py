# Generated by Django 5.1.5 on 2025-01-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]

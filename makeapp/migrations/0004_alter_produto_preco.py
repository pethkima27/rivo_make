# Generated by Django 5.1.5 on 2025-01-28 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeapp', '0003_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]

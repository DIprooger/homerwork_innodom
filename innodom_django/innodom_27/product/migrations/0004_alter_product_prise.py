# Generated by Django 5.0.1 on 2024-01-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_prise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prise',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spelsberg', '0002_product_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(max_length=30, verbose_name='Количество'),
        ),
    ]
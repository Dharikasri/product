# Generated by Django 5.0.6 on 2024-06-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Addproduct', '0002_addproduct_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='product_id',
            field=models.IntegerField(default=True, unique=True),
        ),
    ]

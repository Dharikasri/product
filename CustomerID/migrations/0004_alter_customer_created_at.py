# Generated by Django 5.0.6 on 2024-06-04 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerID', '0003_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

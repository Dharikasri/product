# Generated by Django 5.0.6 on 2024-05-31 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Addproduct', '0001_initial'),
        ('CustomerID', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=100, unique=True)),
                ('order_date', models.DateField()),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerID.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Addproduct.addproduct')),
            ],
        ),
    ]

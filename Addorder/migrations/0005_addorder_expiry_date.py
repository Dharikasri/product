# Generated by Django 5.0.6 on 2024-06-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Addorder', '0004_remove_addorder_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='addorder',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
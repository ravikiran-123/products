# Generated by Django 4.0 on 2022-01-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='Cost_per_item',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='Stock_quantity',
            field=models.BigIntegerField(null=True),
        ),
    ]

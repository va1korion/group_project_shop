# Generated by Django 3.2.3 on 2021-05-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210517_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=300, max_digits=100),
        ),
    ]

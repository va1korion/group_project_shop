# Generated by Django 3.2.3 on 2021-05-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myuser_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='cart',
            field=models.JSONField(default=list),
        ),
    ]

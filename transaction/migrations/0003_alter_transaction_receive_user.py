# Generated by Django 3.2.12 on 2023-04-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20230429_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='receive_user',
            field=models.CharField(max_length=60),
        ),
    ]

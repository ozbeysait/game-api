# Generated by Django 3.1.1 on 2020-10-03 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20201003_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='date_created',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2021-09-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalcode', '0043_auto_20210927_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalcode',
            name='code',
            field=models.CharField(max_length=100),
        ),
    ]

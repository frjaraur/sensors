# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-14 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_auto_20180814_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='update',
            field=models.DateTimeField(),
        ),
    ]
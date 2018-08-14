# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-14 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='humidity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='temperature',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='update',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

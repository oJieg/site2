# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_choice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(default='ananimys', max_length=200),
        ),
    ]

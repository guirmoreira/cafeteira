# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20170627_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='material',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
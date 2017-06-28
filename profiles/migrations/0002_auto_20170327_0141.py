# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='no_email', max_length=255),
        ),
    ]
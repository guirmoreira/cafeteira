# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='code',
            new_name='name',
        ),
    ]
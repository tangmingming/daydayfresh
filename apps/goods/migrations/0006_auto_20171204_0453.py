# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 04:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20171204_0448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchandise',
            old_name='activity_prise',
            new_name='sale_prise',
        ),
    ]

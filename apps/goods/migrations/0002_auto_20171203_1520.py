# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='code',
            field=models.CharField(default='', max_length=30, unique=True, verbose_name='唯一编码'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classification',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='描述'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20171203_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='desc',
            field=models.TextField(max_length=100, verbose_name='商品描述'),
        ),
    ]
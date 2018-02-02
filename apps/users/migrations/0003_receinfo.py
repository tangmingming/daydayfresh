# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180103_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=20, verbose_name='电话')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货信息',
                'verbose_name_plural': '收货信息',
            },
        ),
    ]
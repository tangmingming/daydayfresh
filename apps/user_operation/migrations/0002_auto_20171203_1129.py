# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 11:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recevingaddress',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='collect',
            name='merchandise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Merchandise', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='collect',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]

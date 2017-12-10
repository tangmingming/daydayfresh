# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 11:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0002_auto_20171203_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_type', models.SmallIntegerField(choices=[(0, '留言'), (1, '投诉'), (2, '咨询'), (3, '售后'), (3, '求购'), (10, '其它')], verbose_name='留言类型')),
                ('subject', models.CharField(max_length=30, verbose_name='主题')),
                ('msg', models.TextField(blank=True, default='', verbose_name='留言内容')),
                ('file', models.FileField(null=True, upload_to='', verbose_name='文件')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Revert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(verbose_name='内容')),
                ('file', models.FileField(null=True, upload_to='', verbose_name='文件')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_operation.Message', verbose_name='留言')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
    ]
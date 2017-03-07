# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0043_auto_20170219_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectHostConfigFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('file_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='配置路径')),
                ('file_content', models.TextField(blank=True, null=True, verbose_name='配置内容')),
                ('project_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.ProjectHost', verbose_name='业务')),
            ],
            options={
                'verbose_name': '配置内容',
                'verbose_name_plural': '配置内容',
            },
        ),
    ]

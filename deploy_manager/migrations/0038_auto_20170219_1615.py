# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0037_auto_20170219_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_config_path',
            field=models.ManyToManyField(blank=True, to='deploy_manager.ProjectConfigPath', verbose_name='业务配置文件'),
        ),
    ]

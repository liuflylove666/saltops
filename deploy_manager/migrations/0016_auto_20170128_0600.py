# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0015_auto_20170128_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecthost',
            name='job_script_type',
        ),
        migrations.AddField(
            model_name='project',
            name='job_script_type',
            field=models.IntegerField(choices=[(0, 'salt sls'), (1, 'shell')], default=0, verbose_name='脚本语言'),
        ),
    ]

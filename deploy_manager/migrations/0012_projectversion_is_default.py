# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0011_auto_20170122_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectversion',
            name='is_default',
            field=models.BooleanField(default=True, verbose_name='\u9ed8\u8ba4\u7248\u672c'),
        ),
    ]

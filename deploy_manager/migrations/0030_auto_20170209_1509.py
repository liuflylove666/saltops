# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0029_auto_20170209_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectversion',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='doc/script/', verbose_name='版本'),
        ),
    ]

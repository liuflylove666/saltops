# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0026_auto_20170217_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.IDC', verbose_name='机房'),
        ),
        migrations.AlterField(
            model_name='rack',
            name='cabinet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Cabinet', verbose_name='机柜'),
        ),
    ]

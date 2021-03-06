# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools_manager', '0005_auto_20170128_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=255, verbose_name='参数名称')),
                ('tool_value', models.CharField(max_length=255, verbose_name='参数值')),
            ],
            options={
                'verbose_name_plural': '工具参数',
                'verbose_name': '工具参数',
            },
        ),
        migrations.AlterField(
            model_name='toolsscript',
            name='tools_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsTypes', verbose_name='工具类型'),
        ),
        migrations.AddField(
            model_name='toolsparam',
            name='tool_script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsScript', verbose_name='工具'),
        ),
    ]

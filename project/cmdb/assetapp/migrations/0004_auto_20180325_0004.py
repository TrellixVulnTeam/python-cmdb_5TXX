# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0003_auto_20180325_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkdevice',
            name='asset',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assetapp.Asset'),
        ),
    ]

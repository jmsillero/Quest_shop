# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 17:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20171128_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 12, 7, 46, 570768)),
        ),
    ]

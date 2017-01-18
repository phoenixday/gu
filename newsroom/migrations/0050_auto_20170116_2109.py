# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 19:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0049_auto_20170106_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_tweeted',
            field=models.DateTimeField(default=datetime.datetime(1999, 12, 31, 22, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 20:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170109_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 17, 20, 0, 37, 602865)),
        ),
    ]

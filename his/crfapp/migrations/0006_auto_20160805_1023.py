# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-05 02:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crfapp', '0005_auto_20160805_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='p_dob',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 8, 5, 10, 23, 23, 913000)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_marriage',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-03 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='reg_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

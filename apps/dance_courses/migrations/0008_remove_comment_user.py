# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dance_courses', '0007_auto_20170322_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]

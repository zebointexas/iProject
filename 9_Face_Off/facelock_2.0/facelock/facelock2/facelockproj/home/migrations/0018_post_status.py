# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-01 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]

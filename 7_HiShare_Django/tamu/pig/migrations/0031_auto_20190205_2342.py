# Generated by Django 2.0 on 2019-02-06 05:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0030_auto_20190205_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='Add_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 5, 42, 1, 366755, tzinfo=utc)),
        ),
    ]

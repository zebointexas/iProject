# Generated by Django 2.0 on 2019-01-16 02:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0025_auto_20190115_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='Add_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 2, 55, 10, 998929, tzinfo=utc)),
        ),
    ]

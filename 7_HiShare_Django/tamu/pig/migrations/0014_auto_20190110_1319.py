# Generated by Django 2.0 on 2019-01-10 19:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0013_auto_20190110_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 19, 19, 9, 805354, tzinfo=utc)),
        ),
    ]

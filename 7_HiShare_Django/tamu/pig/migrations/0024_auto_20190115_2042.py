# Generated by Django 2.0 on 2019-01-16 02:42

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0023_auto_20190110_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskRide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Add_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Depart_Date', models.DateTimeField(default='1997-07-01')),
                ('From', models.CharField(max_length=200)),
                ('To', models.CharField(max_length=200)),
                ('Seats_Needed', models.IntegerField(default=3)),
                ('Mobile', models.IntegerField(default=1737888888)),
                ('WeChat', models.CharField(max_length=200)),
                ('Student_Or_Not', models.BooleanField(default=False)),
                ('Gas_Return', django_mysql.models.EnumField(choices=[('1 Gallon Gas', '1 Gallon Gas'), ('3 Gallon Gas', '3 Gallon Gas'), ('5 Gallon Gas', '5 Gallon Gas'), ('7 Gallon Gas', '7 Gallon Gas'), ('10 Gallon Gas', '10 Gallon Gas'), ('15 Gallon Gas', '15 Gallon Gas'), ('25 Gallon Gas', '25 Gallon Gas')], default='1 Gallon Gas')),
            ],
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='depart_date',
            new_name='Depart_Date',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='end_point',
            new_name='From',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='contact_number',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='isStudent',
            new_name='Student_Or_Not',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='start_point',
            new_name='To',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='total_seats',
            new_name='Total_Seats_Available',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='wechat',
            new_name='WeChat',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='add_date',
        ),
        migrations.AddField(
            model_name='ride',
            name='Add_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 2, 42, 4, 325119, tzinfo=utc)),
        ),
    ]

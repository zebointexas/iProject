# Generated by Django 2.0 on 2019-01-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0008_auto_20190110_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='contact_number',
            field=models.IntegerField(default=1737888888),
        ),
        migrations.AddField(
            model_name='ride',
            name='total_seats',
            field=models.IntegerField(default=1),
        ),
    ]
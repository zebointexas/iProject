# Generated by Django 2.0 on 2019-01-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0006_auto_20190105_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='liuyi',
            name='test_filed',
            field=models.IntegerField(default=0),
        ),
    ]
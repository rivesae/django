# Generated by Django 3.2.13 on 2023-06-29 04:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20230627_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 4, 46, 52, 412029, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 4, 46, 52, 412029, tzinfo=utc)),
        ),
    ]

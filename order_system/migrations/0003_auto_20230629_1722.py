# Generated by Django 3.2.19 on 2023-06-29 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0002_auto_20230629_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='title',
        ),
        migrations.AddField(
            model_name='booking',
            name='day',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

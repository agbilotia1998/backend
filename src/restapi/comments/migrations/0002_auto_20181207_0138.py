# Generated by Django 2.1.1 on 2018-12-06 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 1, 38, 37, 715144)),
        ),
        migrations.AlterField(
            model_name='replies',
            name='replied_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 1, 38, 37, 716065)),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-08 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='approvedDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-31 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 5, 54, 22, 763720)),
        ),
    ]

# Generated by Django 2.2 on 2020-04-23 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surpreapp', '0005_auto_20200422_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='changedate',
            field=models.DateField(db_column='changedate', default=datetime.date.today),
        ),
    ]

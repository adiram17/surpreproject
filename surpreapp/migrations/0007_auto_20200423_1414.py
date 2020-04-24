# Generated by Django 2.2 on 2020-04-23 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surpreapp', '0006_score_changedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='changedate',
        ),
        migrations.AddField(
            model_name='score',
            name='predictdate',
            field=models.DateField(db_column='predictdate', default=datetime.date.today),
        ),
    ]
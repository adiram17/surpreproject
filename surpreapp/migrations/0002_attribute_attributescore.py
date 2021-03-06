# Generated by Django 2.2 on 2020-04-21 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surpreapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='name', max_length=500)),
                ('attributetype', models.CharField(db_column='attributetype', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Attribute',
                'verbose_name_plural': 'Attributes',
                'db_table': 'attribute',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AttributeScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='name', max_length=500)),
                ('value', models.IntegerField(db_column='value', default=0)),
                ('attributetype', models.CharField(db_column='attributetype', max_length=100, null=True)),
                ('score', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='surpreapp.Score')),
            ],
            options={
                'verbose_name': 'Attribute Score',
                'verbose_name_plural': 'Attribute Scores',
                'db_table': 'attributescore',
                'ordering': ['name'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('title', models.TextField(blank=True, null=True)),
                ('speaker', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField()),
                ('place', models.TextField(blank=True, null=True)),
                ('university', models.TextField(blank=True, null=True)),
                ('updata_time', models.DateField()),
                ('link', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'lecture',
                'managed': False,
            },
        ),
    ]
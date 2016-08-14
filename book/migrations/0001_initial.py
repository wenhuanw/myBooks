# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField()),
                ('publisher', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('link', models.URLField(max_length=300)),
                ('cover', models.URLField(max_length=300)),
            ],
        ),
    ]

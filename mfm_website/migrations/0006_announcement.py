# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-21 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfm_website', '0005_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcer', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
    ]

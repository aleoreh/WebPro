# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_persons_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='User',
            field=models.CharField(blank=True, max_length=2048),
        ),
    ]

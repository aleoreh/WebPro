# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_keywords_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='User',
            field=models.ForeignKey(blank=True, db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
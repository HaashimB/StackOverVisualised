# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='creationdate',
        ),
        migrations.RemoveField(
            model_name='post',
            name='viewcount',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
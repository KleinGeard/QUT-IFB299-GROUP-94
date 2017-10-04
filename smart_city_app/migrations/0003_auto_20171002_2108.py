# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 11:08
from __future__ import unicode_literals
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('smart_city_app', '0002_auto_20170903_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='map_item',
            name='map_item_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='map_item',
            name='map_item_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='map_item',
            name='map_item_phone',
            field=models.CharField(max_length=32),
        ),
    ]

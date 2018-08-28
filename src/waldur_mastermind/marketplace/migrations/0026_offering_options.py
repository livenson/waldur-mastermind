# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-24 08:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0025_private_offering'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='options',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict,
                                                                 help_text='Fields describing Offering request form.'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0012_expertprovider_enable_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertcontract',
            name='_file',
            field=models.TextField(blank=True, editable=False),
        ),
    ]

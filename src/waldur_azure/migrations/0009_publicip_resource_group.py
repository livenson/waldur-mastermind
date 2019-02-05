# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-01 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_azure', '0008_networkinterface_public_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicip',
            name='resource_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.ResourceGroup'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-10 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openstack_tenant', '0037_internal_ip_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internalip',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings'),
        ),
    ]

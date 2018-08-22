# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-22 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('marketplace', '0022_section_is_standalone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offering',
            name='is_active',
        ),
        migrations.AddField(
            model_name='offering',
            name='state',
            field=django_fsm.FSMIntegerField(choices=[(1, 'Draft'), (2, 'Active'), (3, 'Paused'), (4, 'Archived')], default=1),
        ),
        migrations.AddField(
            model_name='offering',
            name='type',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='plan',
            name='archived',
            field=models.BooleanField(default=False, help_text='Forbids creation of new resources.'),
        ),
        migrations.AddField(
            model_name='plan',
            name='article_code',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='plan',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='plan',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='product_code',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
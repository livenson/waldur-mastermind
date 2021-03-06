# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 07:41
from __future__ import unicode_literals

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models

import waldur_core.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_category_offering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('boolean', b'boolean'), ('string', b'string'), ('text', b'text'), ('integer', b'integer'), ('choice', b'choice'), ('list', b'list')], max_length=255)),
                ('available_values', waldur_core.core.fields.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='marketplace.Section'),
        ),
        migrations.AddField(
            model_name='section',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='marketplace.Category'),
        ),
    ]

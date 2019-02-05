# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 16:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import waldur_azure.validators


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_azure', '0009_publicip_resource_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sqldatabase',
            name='resource_group',
        ),
        migrations.AddField(
            model_name='sqlserver',
            name='fqdn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='name',
            field=models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, underscore, period and hyphens.', regex=re.compile(b'^[a-zA-Z][a-zA-Z0-9._-]+$'))]),
        ),
        migrations.AlterField(
            model_name='networkinterface',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, underscore, period and hyphens.', regex=re.compile(b'^[a-zA-Z][a-zA-Z0-9._-]+$'))]),
        ),
        migrations.AlterField(
            model_name='publicip',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, underscore, period and hyphens.', regex=re.compile(b'^[a-zA-Z][a-zA-Z0-9._-]+$'))]),
        ),
        migrations.AlterField(
            model_name='sqldatabase',
            name='charset',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sqldatabase',
            name='collation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sqldatabase',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AlterField(
            model_name='sqlserver',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='The name can only be made up of lowercase letters "a"-"z", the numbers 0-9 and the hyphen. The hyphen may not lead or trail in the name.', regex=re.compile(b'^[a-z0-9][a-z0-9-]+[a-z0-9]$'))]),
        ),
        migrations.AlterField(
            model_name='sqlserver',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(128), waldur_azure.validators.validate_password]),
        ),
        migrations.AlterField(
            model_name='sqlserver',
            name='service_project_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waldur_azure.AzureServiceProjectLink'),
        ),
        migrations.AlterField(
            model_name='sqlserver',
            name='storage_mb',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(5120), django.core.validators.MaxValueValidator(4194304)]),
        ),
        migrations.AlterField(
            model_name='sqlserver',
            name='username',
            field=models.CharField(max_length=50, validators=[waldur_azure.validators.SQLServerUsernameValidator]),
        ),
        migrations.AlterField(
            model_name='storageaccount',
            name='name',
            field=models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='The name can contain only letters and numbers.', regex=re.compile(b'^[a-z][a-z0-9]{2,23}$'))]),
        ),
        migrations.AlterField(
            model_name='subnet',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, underscore, period and hyphens.', regex=re.compile(b'^[a-zA-Z][a-zA-Z0-9._-]+$'))]),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='name',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='The name can contain only letters, numbers, and hyphens. The name must be shorter than 15 characters and start with a letter and must end with a letter or a number.', regex=re.compile(b'^[a-zA-Z][a-zA-Z0-9-]{0,13}[a-zA-Z0-9]$'))]),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='password',
            field=models.CharField(max_length=72, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(72), waldur_azure.validators.validate_password, waldur_azure.validators.VirtualMachinePasswordValidator]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-07 18:47
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack_tenant', '0029_add_unique_constraint_for_properties'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_user_token_lifetime'),
        ('playbook_jobs', '0003_playbook_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='project',
        ),
        migrations.AddField(
            model_name='job',
            name='service_project_link',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='openstack_tenant.OpenStackTenantServiceProjectLink'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='ssh_public_key',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.SshPublicKey'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='subnet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='openstack_tenant.SubNet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

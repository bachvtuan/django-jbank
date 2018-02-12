# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jacc', '0005_auto_20171030_1958'),
        ('jbank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencepaymentbatch',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='referencepaymentbatch',
            name='id',
        ),
        migrations.RemoveField(
            model_name='referencepaymentrecord',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='referencepaymentrecord',
            name='id',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='id',
        ),
        migrations.RemoveField(
            model_name='statementrecord',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='statementrecord',
            name='id',
        ),
        migrations.AddField(
            model_name='referencepaymentbatch',
            name='accountentrysourcefile_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jacc.AccountEntrySourceFile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='referencepaymentrecord',
            name='accountentry_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jacc.AccountEntry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statement',
            name='accountentrysourcefile_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jacc.AccountEntrySourceFile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statementrecord',
            name='accountentry_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jacc.AccountEntry'),
            preserve_default=False,
        ),
    ]

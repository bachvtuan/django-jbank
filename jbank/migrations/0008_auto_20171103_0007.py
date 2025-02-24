# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-03 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0007_auto_20171102_2351"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReferencePaymentBatchFile",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, verbose_name="created"),
                ),
                ("file", models.FileField(upload_to="uploads", verbose_name="file")),
                ("errors", models.TextField(blank=True, default="", max_length=4086, verbose_name="errors")),
            ],
            options={
                "verbose_name": "reference payment batch file",
                "verbose_name_plural": "reference payment batch files",
            },
        ),
        migrations.RenameField(
            model_name="statement",
            old_name="statement_file",
            new_name="file",
        ),
        migrations.AddField(
            model_name="referencepaymentbatch",
            name="file",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jbank.ReferencePaymentBatchFile",
            ),
        ),
    ]

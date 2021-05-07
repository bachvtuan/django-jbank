# Generated by Django 3.2 on 2021-05-07 21:22

from django.db import migrations
import jutil.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0006_auto_20210318_2130"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="delivery_method",
            field=jutil.modelfields.SafeCharField(
                choices=[("", ""), ("A", "From Customer"), ("K", "From Bank Clerk"), ("J", "From Bank System")],
                db_index=True,
                max_length=1,
                verbose_name="delivery method",
            ),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="delivery_method",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[("", ""), ("A", "From Customer"), ("K", "From Bank Clerk"), ("J", "From Bank System")],
                db_index=True,
                max_length=1,
                verbose_name="delivery method",
            ),
        ),
    ]

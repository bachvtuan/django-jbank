# Generated by Django 3.2.6 on 2021-09-13 23:59

from django.db import migrations, models
import django.utils.timezone
import jutil.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0012_alter_referencepaymentrecord_delivery_method"),
    ]

    operations = [
        migrations.CreateModel(
            name="EuriborRate",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("record_date", models.DateField(db_index=True, verbose_name="record date")),
                ("name", jutil.modelfields.SafeCharField(db_index=True, max_length=64, verbose_name="interest rate name")),
                ("rate", models.DecimalField(db_index=True, decimal_places=4, max_digits=10, verbose_name="interest rate %")),
                ("created", models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, editable=False, verbose_name="created")),
            ],
            options={
                "verbose_name": "euribor rate",
                "verbose_name_plural": "euribor rates",
            },
        ),
    ]

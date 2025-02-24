# Generated by Django 2.0 on 2018-02-08 07:24

from django.db import migrations, models
import django.db.models.deletion
import jutil.validators


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0015_auto_20180208_0643"),
    ]

    operations = [
        migrations.CreateModel(
            name="PayoutParty",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(db_index=True, max_length=128, verbose_name="name")),
                (
                    "account_number",
                    models.CharField(
                        db_index=True,
                        max_length=35,
                        validators=[jutil.validators.iban_validator],
                        verbose_name="account number",
                    ),
                ),
                ("bic", models.CharField(blank=True, db_index=True, max_length=16, verbose_name="BIC")),
                (
                    "org_id",
                    models.CharField(blank=True, db_index=True, default="", max_length=32, verbose_name="organization id"),
                ),
                ("address", models.TextField(blank=True, default="", verbose_name="address")),
                (
                    "country_code",
                    models.CharField(blank=True, db_index=True, default="FI", max_length=2, verbose_name="country code"),
                ),
            ],
            options={
                "verbose_name_plural": "payout parties",
                "verbose_name": "payout party",
            },
        ),
        migrations.AlterModelOptions(
            name="payoutstatus",
            options={"verbose_name": "payout status", "verbose_name_plural": "payout statuses"},
        ),
        migrations.RemoveField(
            model_name="payout",
            name="recipient_account_number",
        ),
        migrations.AlterField(
            model_name="payout",
            name="state",
            field=models.CharField(
                blank=True,
                choices=[("W", "waiting"), ("P", "paid"), ("C", "canceled"), ("E", "error")],
                db_index=True,
                default="W",
                max_length=1,
                verbose_name="state",
            ),
        ),
        migrations.AddField(
            model_name="payout",
            name="payer",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="jbank.PayoutParty",
                verbose_name="payer",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="payout",
            name="recipient",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="jbank.PayoutParty",
                verbose_name="recipient",
            ),
            preserve_default=False,
        ),
    ]

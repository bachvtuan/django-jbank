# Generated by Django 2.0 on 2018-02-08 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jbank', '0017_payoutparty_payouts_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payoutparty',
            name='payouts_account',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='jacc.Account', verbose_name='payouts account'),
        ),
    ]

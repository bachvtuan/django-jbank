# Generated by Django 2.0 on 2018-02-08 06:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jutil.validators


class Migration(migrations.Migration):

    dependencies = [
        ('jacc', '0010_auto_20180201_0734'),
        ('jbank', '0013_auto_20180126_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('accountentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jacc.AccountEntry')),
                ('recipient_account_number', models.CharField(db_index=True, max_length=35, validators=[jutil.validators.iban_validator], verbose_name='recipient account number')),
                ('messages', models.TextField(blank=True, verbose_name='recipient messages')),
                ('msg_id', models.CharField(blank=True, db_index=True, editable=False, max_length=64, verbose_name='message id')),
                ('file_name', models.CharField(blank=True, db_index=True, editable=False, max_length=255, verbose_name='file name')),
                ('paid_date', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='paid date')),
                ('state', models.CharField(blank=True, choices=[('W', 'waiting'), ('P', 'paid'), ('C', 'canceled')], db_index=True, default='W', max_length=1, verbose_name='state')),
            ],
            options={
                'verbose_name_plural': 'payouts',
                'verbose_name': 'payout',
            },
            bases=('jacc.accountentry',),
        ),
        migrations.CreateModel(
            name='PayoutStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('file_name', models.CharField(blank=True, db_index=True, editable=False, max_length=255, verbose_name='file name')),
                ('msg_id', models.CharField(db_index=True, max_length=64, verbose_name='message id')),
                ('original_msg_id', models.CharField(db_index=True, max_length=64, verbose_name='original message id')),
                ('group_status', models.CharField(blank=True, db_index=True, max_length=8, verbose_name='group status')),
                ('status_reason', models.CharField(blank=True, max_length=255, verbose_name='status reason')),
                ('payout', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='jbank.Payout', verbose_name='payout')),
            ],
        ),
    ]

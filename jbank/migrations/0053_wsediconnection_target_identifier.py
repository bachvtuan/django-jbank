# Generated by Django 2.2.3 on 2019-11-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbank', '0052_auto_20191130_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='wsediconnection',
            name='target_identifier',
            field=models.CharField(default=1, max_length=32, verbose_name='target identifier'),
            preserve_default=False,
        ),
    ]

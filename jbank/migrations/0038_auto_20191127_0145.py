# Generated by Django 2.2.3 on 2019-11-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbank', '0037_auto_20191127_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wsediconnection',
            name='signing_cert',
            field=models.FileField(blank=True, upload_to='certs', verbose_name='signing cert'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_plant1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant1',
            name='kvitnutie_do',
            field=models.IntegerField(blank=True, null=True, verbose_name='Kvitnutie do'),
        ),
        migrations.AlterField(
            model_name='plant1',
            name='kvitnutie_od',
            field=models.IntegerField(blank=True, null=True, verbose_name='Kvitnutie od'),
        ),
    ]
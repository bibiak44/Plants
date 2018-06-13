# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180611_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rod_lat', models.CharField(max_length=30, verbose_name='Rod latinsky')),
                ('druh_lat', models.CharField(blank=True, max_length=30, verbose_name='Druh latinsky')),
                ('kultivar', models.CharField(blank=True, max_length=30, verbose_name='Kultivar')),
                ('rod_sk', models.CharField(blank=True, default='neuvedene', max_length=30, verbose_name='Rod slovensky')),
                ('druh_sk', models.CharField(blank=True, default='neuvedene', max_length=30, verbose_name='Druh slovensky')),
                ('typ', models.CharField(blank=True, max_length=30, null=True, verbose_name='Typ')),
                ('vyska', models.FloatField(blank=True, null=True, verbose_name='Vyska [m]')),
                ('rozpon', models.IntegerField(blank=True, null=True, verbose_name='Rozpon')),
                ('farba', models.CharField(blank=True, max_length=30, null=True, verbose_name='Farba')),
                ('pouzitie', models.CharField(blank=True, max_length=30, null=True, verbose_name='Pouzitie')),
                ('kvitnutie_od', models.CharField(blank=True, max_length=30, null=True, verbose_name='Kvitnutie od')),
                ('kvitnutie_do', models.CharField(blank=True, max_length=30, null=True, verbose_name='Kvitnutie do')),
                ('stanovisko', models.CharField(blank=True, max_length=30, null=True, verbose_name='Stanovisko')),
                ('slnko', models.CharField(blank=True, max_length=30, null=True, verbose_name='Slnko')),
                ('vlaha', models.CharField(blank=True, max_length=30, null=True, verbose_name='Vlaha')),
                ('fotka', models.ImageField(blank=True, null=True, upload_to='')),
                ('poznamka', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

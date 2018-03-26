# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(help_text='service name', max_length=30)),
                ('version', models.CharField(help_text='service version', max_length=10)),
                ('status', models.CharField(choices=[('created', 'created'), ('updated', 'updated'), ('changed', 'changed')], default='created', max_length=15)),
            ],
        ),
    ]

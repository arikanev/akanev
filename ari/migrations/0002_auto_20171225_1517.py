# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ari', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ari.Image'),
        ),
    ]
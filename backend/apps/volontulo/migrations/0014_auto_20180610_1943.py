# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-10 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volontulo', '0013_auto_20180603_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergallery',
            name='userprofile',
        ),
        migrations.DeleteModel(
            name='UserGallery',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import pets.models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0023_auto_20170909_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_image',
            field=models.ImageField(blank=True, null=True, storage=pets.models.OverwriteStorage(), upload_to=pets.models.file_upload_location),
        ),
    ]
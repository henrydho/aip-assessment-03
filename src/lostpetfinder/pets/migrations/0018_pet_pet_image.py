# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0017_auto_20170908_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_image',
            field=models.FileField(null=True, upload_to='pets/'),
        ),
    ]
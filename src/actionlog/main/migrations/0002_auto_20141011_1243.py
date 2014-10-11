# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='title',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]

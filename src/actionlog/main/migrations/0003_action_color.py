# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141011_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='color',
            field=models.CharField(default=b'fa66fe', max_length=6),
            preserve_default=True,
        ),
    ]

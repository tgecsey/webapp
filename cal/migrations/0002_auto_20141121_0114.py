# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='snippet',
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]

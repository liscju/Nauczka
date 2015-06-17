# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='course',
            field=models.ForeignKey(default=None, to='home.Course'),
        ),
        migrations.AddField(
            model_name='note',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='note',
            name='time_spent',
            field=models.IntegerField(default=0),
        ),
    ]

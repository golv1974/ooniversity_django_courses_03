# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='email',
            field=models.EmailField(default=b'example@com.ua', max_length=75),
            preserve_default=True,
        ),
    ]

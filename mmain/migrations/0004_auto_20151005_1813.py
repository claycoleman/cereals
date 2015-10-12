# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmain', '0003_auto_20151005_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='cereal_type',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]

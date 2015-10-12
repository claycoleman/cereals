# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(blank=True, to='mmain.Manufacturer', null=True),
        ),
    ]

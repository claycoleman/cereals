# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmain', '0002_auto_20151005_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='carbs',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='dietary_fiber',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='display_shelf',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='fat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='potassium',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='protein',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='sodium',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='sugars',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='vitamins_and_minerals',
            field=models.FloatField(null=True, blank=True),
        ),
    ]

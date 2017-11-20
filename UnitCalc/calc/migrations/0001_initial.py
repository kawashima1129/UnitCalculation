# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_category', models.CharField(max_length=200)),
                ('number_unit', models.IntegerField(default=2)),
            ],
        ),
    ]

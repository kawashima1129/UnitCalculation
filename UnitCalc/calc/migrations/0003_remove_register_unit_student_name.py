# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_register_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_unit',
            name='student_name',
        ),
    ]

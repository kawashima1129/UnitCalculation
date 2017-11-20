# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_remove_register_unit_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('compulsory_unit', models.IntegerField()),
                ('select_unit', models.IntegerField()),
                ('free_unit', models.IntegerField()),
                ('core_unit', models.IntegerField()),
            ],
        ),
    ]

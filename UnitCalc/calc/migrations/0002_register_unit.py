# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('student_name', models.CharField(max_length=200)),
                ('Register_obj', models.ForeignKey(to='calc.Unit')),
            ],
        ),
    ]

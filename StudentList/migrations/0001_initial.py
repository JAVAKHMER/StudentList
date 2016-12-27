# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(default=b'Male', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('birthday', models.DateField()),
                ('register_date', models.DateField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]

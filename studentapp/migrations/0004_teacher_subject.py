# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-04 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_student_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='studentapp.Subject'),
            preserve_default=False,
        ),
    ]

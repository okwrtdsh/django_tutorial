# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('enabled', models.BooleanField(default=True, verbose_name='有効')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('order', models.PositiveIntegerField(verbose_name='表示順')),
            ],
            options={
                'verbose_name': 'カテゴリー',
                'ordering': ['order'],
                'verbose_name_plural': 'カテゴリー',
            },
        ),
    ]

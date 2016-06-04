# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('enabled', models.BooleanField(default=True, verbose_name='有効')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('deadline', models.DateTimeField(verbose_name='締め切り')),
                ('completed', models.DateTimeField(blank=True, null=True, verbose_name='完了日時')),
                ('priority', models.PositiveIntegerField(verbose_name='優先度', choices=[(1, '高'), (2, '中'), (3, '低')])),
                ('note', models.TextField(verbose_name='備考', blank=True)),
                ('categories', models.ManyToManyField(to='master.Category', verbose_name='カテゴリー')),
            ],
            options={
                'verbose_name': 'ToDo',
                'verbose_name_plural': 'ToDo',
            },
        ),
        migrations.CreateModel(
            name='ToDoUser',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('handle_name', models.CharField(max_length=255, verbose_name='表示名')),
            ],
            options={
                'verbose_name_plural': 'ToDoUser',
                'ordering': ['-date_joined'],
                'verbose_name': 'ToDoUser'
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(to='todo.ToDoUser', verbose_name='ユーザー'),
        ),
    ]

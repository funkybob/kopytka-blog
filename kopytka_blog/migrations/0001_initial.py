# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 02:18
from __future__ import unicode_literals

import array_tags.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('live_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Post goes live at')),
                ('kill_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Post expires at')),
                ('is_published', models.BooleanField(db_index=True, default=False, verbose_name='Is Published?')),
                ('tags', array_tags.fields.TagField(base_field=models.CharField(max_length=50), lower=True, size=None)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]

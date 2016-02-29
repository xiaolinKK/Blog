# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u4f5c\u8005', 'verbose_name_plural': '\u4f5c\u8005'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_time'], 'verbose_name': '\u535a\u5ba2', 'verbose_name_plural': '\u535a\u5ba2'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(blank=True, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='caption',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(blank=True, max_length=20, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]

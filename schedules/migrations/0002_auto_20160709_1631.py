# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-09 20:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0002_remove_window_pi'),
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Window',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.PositiveIntegerField()),
                ('pi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pis.Pi')),
            ],
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='schedule_date',
            new_name='schedule_start_date',
        ),
        migrations.AddField(
            model_name='schedule',
            name='schedule_end_date',
            field=models.DateField(default=datetime.date(2016, 7, 9)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduleitem',
            name='play_order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='window',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.Window'),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('schedule_start_date', 'window')]),
        ),
        migrations.RemoveField(
            model_name='scheduleitem',
            name='start_time',
        ),
        migrations.AlterUniqueTogether(
            name='scheduleitem',
            unique_together=set([('schedule', 'play_order')]),
        ),
    ]

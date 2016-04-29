# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asim', '0002_auto_20160321_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='CHUHousekeeping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('swmode', models.FloatField(verbose_name='SW mode')),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentHousekeeping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('swmode', models.FloatField(verbose_name='SW mode')),
                ('errors', models.FloatField(verbose_name='Errors/Warnings ')),
                ('temp1', models.FloatField(verbose_name='Temperature 1')),
                ('tmcnt', models.FloatField(verbose_name='TM count ')),
                ('tccnt', models.FloatField(verbose_name='TC count ')),
                ('inston', models.FloatField(verbose_name='Inst ON/OFF')),
                ('hvolt', models.FloatField(verbose_name='Hvolt')),
                ('daylight', models.FloatField(verbose_name='Day light sensor')),
                ('triggers', models.FloatField(verbose_name='Triggers/Priority')),
            ],
        ),
        migrations.CreateModel(
            name='Mmia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('obsid', models.IntegerField(verbose_name='ObservationId')),
                ('date', models.DateTimeField(verbose_name='Date Observed')),
                ('trig', models.CharField(max_length=200)),
                ('inst', models.CharField(max_length=200)),
                ('lev0', models.CharField(max_length=200)),
                ('lev1', models.CharField(max_length=200)),
                ('prev', models.CharField(max_length=200)),
                ('chu1prev', models.CharField(max_length=200)),
                ('chu2prev', models.CharField(max_length=200)),
                ('phot1prev', models.CharField(max_length=200)),
                ('phot2prev', models.CharField(max_length=200)),
                ('phot3prev', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MonitoredHousekeeping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('alivecnt', models.FloatField(verbose_name='Alive Counter')),
                ('bootstat', models.FloatField(verbose_name='Boot status')),
                ('swmode', models.FloatField(verbose_name='SW mode')),
                ('errors', models.FloatField(verbose_name='Errors/Warnings ')),
                ('temper', models.FloatField(verbose_name='Temperature 1')),
                ('tmcnt', models.FloatField(verbose_name='TM count ')),
                ('tccnt', models.FloatField(verbose_name='TC count ')),
            ],
        ),
        migrations.CreateModel(
            name='PHOTHousekeeping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('swmode', models.FloatField(verbose_name='SW mode')),
            ],
        ),
        migrations.AlterField(
            model_name='sciencedata',
            name='date',
            field=models.DateTimeField(verbose_name='Date Observed'),
        ),
        migrations.AlterField(
            model_name='sciencedata',
            name='lat',
            field=models.FloatField(verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='sciencedata',
            name='lon',
            field=models.FloatField(verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='sciencedata',
            name='obsid',
            field=models.IntegerField(verbose_name='ObservationId'),
        ),
    ]

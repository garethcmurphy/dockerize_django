from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin



class MXGSCZTDAUSummaryHousekeepingTM(models.Model):
    packet_length                   = models.IntegerField('Packet length')
    utc_year                        = models.IntegerField('UTC year')
    utc_msec                        = models.IntegerField('UTC msec')
    utc_seconds                     = models.IntegerField('UTC seconds')
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    grey_mode_data_reduc_factor     = models.IntegerField()
    dau_czt_1_ratemeter_count       = models.IntegerField()
    dau_czt_1_tmon_channel_1        = models.IntegerField()
    dau_czt_1_tmon_channel_2        = models.IntegerField()
    dau_czt_1_high_voltage_mon      = models.IntegerField()
    dau_czt_1_xa_asic_cfg_4_fail    = models.BooleanField()
    dau_czt_1_xa_asic_cfg_4_pass    = models.BooleanField()
    dau_czt_1_xa_asic_cfg_3_fail    = models.BooleanField()
    dau_czt_1_xa_asic_cfg_3_pass    = models.BooleanField()
    dau_czt_1_xa_asic_cfg_2_fail    = models.BooleanField()
    dau_czt_1_xa_asic_cfg_2_pass    = models.BooleanField()
    dau_czt_1_xa_asic_cfg_1_fail    = models.BooleanField()
    dau_czt_1_xa_asic_cfg_1_pass    = models.BooleanField()
    dau_czt_2_ratemeter_count       = models.IntegerField()
    dau_czt_2_tmon_channel_1        = models.IntegerField()
    dau_czt_2_tmon_channel_2        = models.IntegerField()
    dau_czt_2_high_voltage_mon      = models.IntegerField()
    dau_czt_2_xa_asic_cfg_4_fail    = models.BooleanField()
    dau_czt_2_xa_asic_cfg_4_pass    = models.BooleanField()
    dau_czt_2_xa_asic_cfg_3_fail    = models.BooleanField()
    dau_czt_2_xa_asic_cfg_3_pass    = models.BooleanField()
    dau_czt_2_xa_asic_cfg_2_fail    = models.BooleanField()
    dau_czt_2_xa_asic_cfg_2_pass    = models.BooleanField()
    dau_czt_2_xa_asic_cfg_1_fail    = models.BooleanField()
    dau_czt_2_xa_asic_cfg_1_pass    = models.BooleanField()
    dau_czt_3_ratemeter_count       = models.IntegerField()
    dau_czt_3_tmon_channel_1        = models.IntegerField()
    dau_czt_3_tmon_channel_2        = models.IntegerField()
    dau_czt_3_high_voltage_mon      = models.IntegerField()
    dau_czt_3_xa_asic_cfg_4_fail    = models.BooleanField()
    dau_czt_3_xa_asic_cfg_4_pass    = models.BooleanField()
    dau_czt_3_xa_asic_cfg_3_fail    = models.BooleanField()
    dau_czt_3_xa_asic_cfg_3_pass    = models.BooleanField()
    dau_czt_3_xa_asic_cfg_2_fail    = models.BooleanField()
    dau_czt_3_xa_asic_cfg_2_pass    = models.BooleanField()
    dau_czt_3_xa_asic_cfg_1_fail    = models.BooleanField()
    dau_czt_3_xa_asic_cfg_1_pass    = models.BooleanField()
    dau_czt_4_ratemeter_count       = models.IntegerField()
    dau_czt_4_tmon_channel_1        = models.IntegerField()
    dau_czt_4_tmon_channel_2        = models.IntegerField()
    dau_czt_4_high_voltage_mon      = models.IntegerField()
    dau_czt_4_xa_asic_cfg_4_fail    = models.BooleanField()
    dau_czt_4_xa_asic_cfg_4_pass    = models.BooleanField()
    dau_czt_4_xa_asic_cfg_3_fail    = models.BooleanField()
    dau_czt_4_xa_asic_cfg_3_pass    = models.BooleanField()
    dau_czt_4_xa_asic_cfg_2_fail    = models.BooleanField()
    dau_czt_4_xa_asic_cfg_2_pass    = models.BooleanField()
    dau_czt_4_xa_asic_cfg_1_fail    = models.BooleanField()
    dau_czt_4_xa_asic_cfg_1_pass    = models.BooleanField()


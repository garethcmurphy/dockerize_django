from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSAuroralCaptureObservation(models.Model):
    utc_year                        =models.IntegerField('UTC year')
    utc_msec                        =models.IntegerField('UTC msec')
    utc_seconds                     =models.IntegerField('UTC seconds')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan4  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan4  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan4  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan4  =models.IntegerField()
    led_bin0_lr_boundary            =models.IntegerField()
    led_bin1_lr_boundary            =models.IntegerField()
    led_bin2_lr_boundary            =models.IntegerField()
    led_bin3_lr_boundary            =models.IntegerField()
    led_bin4_lr_boundary            =models.IntegerField()
    led_bin5_lr_boundary            =models.IntegerField()
    led_bin6_lr_boundary            =models.IntegerField()
    led_bin7_lr_boundary            =models.IntegerField()
    led_bin8_lr_boundary            =models.IntegerField()
    led_bin9_lr_boundary            =models.IntegerField()
    led_bin9_upr_boundary           =models.IntegerField()
    hed_bin0_lr_boundary            =models.IntegerField()
    hed_bin1_lr_boundary            =models.IntegerField()
    hed_bin2_lr_boundary            =models.IntegerField()
    hed_bin3_lr_boundary            =models.IntegerField()
    hed_bin4_lr_boundary            =models.IntegerField()
    hed_bin5_lr_boundary            =models.IntegerField()
    hed_bin6_lr_boundary            =models.IntegerField()
    hed_bin7_lr_boundary            =models.IntegerField()
    hed_bin8_lr_boundary            =models.IntegerField()
    led_temporal_bin_size           =models.IntegerField()
    hed_temporal_bin_size           =models.IntegerField()
    auroral_capture_thresh          =models.IntegerField()
    auroral_capture_dur             =models.IntegerField()
    led_binned_vals                 =models.IntegerField()
    hed_binned_vals                 =models.IntegerField()
    led_bin_vals                    =models.FileField()
    hed_bin_vals                    =models.FileField()
    end_dau_bgo_1_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_1_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_1_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_1_int_tmon_chan4    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan4    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan4    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan4    =models.IntegerField()



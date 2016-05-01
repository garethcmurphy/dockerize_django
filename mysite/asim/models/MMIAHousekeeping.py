from django.db import models

class Mmia_hk_monitored(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()
    alive_counter = models.IntegerField()
    boot_status_completed_with_errors = models.BooleanField()
    boot_status_completed_no_errors = models.BooleanField()
    boot_status_asw_load_ok = models.BooleanField()
    boot_status_system_memory_test_ok = models.BooleanField()
    BOOTMODE = "BO"
    CONFMODE = "CF"
    OPMODE = "OP"
    SW_MODE_CHOICES = (
        (BOOTMODE, "Boot mode"),
        (CONFMODE, "Configuration mode"),
        (OPMODE, "Operational mode")
    )
    sw_mode = models.CharField(max_length=2,
                               choices=SW_MODE_CHOICES,
                               default=OPMODE)
    UNDEFINED = "UN"
    TRIGGERED = "TR"
    TIMED = "TI"
    DATAPROCESS = "DA"
    SW_SUBMODE_CHOICES = (
        (UNDEFINED, "Undefined"),
        (TRIGGERED, "Triggered data collection"),
        (TIMED, "Timed data collection"),
        (DATAPROCESS, "Data processing")
    )
    sw_submode = models.CharField(max_length=2,
                                  choices=SW_SUBMODE_CHOICES,
                                  default=TRIGGERED)
    err_war_invalid_startcycle = models.BooleanField()  # No valid or more than one valid Start Cycle Request TC packet is received by MMIA before the next TCP.
    err_war_nonscience_tm_discarded = models.BooleanField()  # Non-science downlink buffer is full
    err_war_comm_protocol = models.BooleanField()  # Communication protocol error detected, will attempt to resynchonize protocol.
    err_war_invalid_EDLF_frame = models.BooleanField() # Invalid EDLF frame received.
    err_war_task_deadline_missed = models.BooleanField() # Task deadline missed or task queue full.
    err_war_software_exception = models.BooleanField() # Software exception occured in Boot Software.
    err_war_nvm_powered_on = models.BooleanField()
    err_war_daylight_detected = models.BooleanField() # Daylight detected by daylight sensor
    err_war_daylight_sensor_disabled = models.BooleanField()
    pow_internal_temp = models.IntegerField()
    dpu_internal_temp0 = models.IntegerField()
    dpu_internal_temp1 = models.IntegerField()
    phot1_temp = models.IntegerField()
    phot2_temp = models.IntegerField()
    phot3_temp = models.IntegerField()
    chu1_temp = models.IntegerField()
    chu2_temp = models.IntegerField()

class Mmia_hk_instrument(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()
    tcp_count_internal = models.IntegerField()
    acquisition_start_time = models.IntegerField() # Current value (in msecs). The counter is reset to 0 by TCP and couts up to ~10^6 before next TCP. Value range 0-(2^32)-1
    err_war_invalid_startcycle = models.BooleanField()  # No valid or more than one valid Start Cycle Request TC packet is received by MMIA before the next TCP.
    err_war_nonscience_tm_discarded = models.BooleanField()  # Non-science downlink buffer is full
    err_war_comm_protocol = models.BooleanField()  # Communication protocol error detected, will attempt to resynchonize protocol.
    err_war_invalid_EDLF_frame = models.BooleanField() # Invalid EDLF frame received.
    err_war_task_deadline_missed = models.BooleanField() # Task deadline missed or task queue full.
    err_war_software_exception = models.BooleanField() # Software exception occured in Boot Software.
    err_war_nvm_powered_on = models.BooleanField()
    err_war_daylight_detected = models.BooleanField() # Daylight detected by daylight sensor
    err_war_daylight_sensor_disabled = models.BooleanField()
    UNDEFINED = "UN"
    CONFMODE = "CF"
    OPMODE = "OP"
    SW_MODE_CHOICES = (
        (UNDEFINED, "Boot mode"),
        (CONFMODE, "Configuration mode"),
        (OPMODE, "Operational mode")
    )
    sw_mode = models.CharField(max_length=2,
                               choices=SW_MODE_CHOICES,
                               default=OPMODE)
    UNDEFINED = "UN"
    TRIGGERED = "TR"
    TIMED = "TI"
    DATAPROCESS = "DA"
    SW_SUBMODE_CHOICES = (
        (UNDEFINED, "Undefined"),
        (TRIGGERED, "Triggered data collection"),
        (TIMED, "Timed data collection"),
        (DATAPROCESS, "Data processing")
    )
    sw_submode = models.CharField(max_length=2,
                                  choices=SW_SUBMODE_CHOICES,
                                  default=TRIGGERED)
    nonscience_tm_discard_count = models.IntegerField()
    tcp_count = models.IntegerField()
    dpu_timer_preset_value = models.IntegerField()
    received_tc_count = models.IntegerField()
    discarded_tc_count = models.IntegerField()
    enabled_instrument_hk = models.BooleanField()
    enabled_startup_hk = models.BooleanField()
    enabled_buffer_resource_hk = models.BooleanField
    enabled_dpu_hk = models.BooleanField()
    enabled_chu_hk = models.BooleanField()
    enabled_phot_hk = models.BooleanField()
    enabled_event_30000 = models.BooleanField()
    enabled_event_30010 = models.BooleanField()
    enabled_event_30050 = models.BooleanField()
    enabled_event_30060 = models.BooleanField()
    enabled_event_30070 = models.BooleanField()
    enabled_event_30080 = models.BooleanField()
    enabled_event_30090 = models.BooleanField()
    enabled_event_30100 = models.BooleanField()
    enabled_event_30110 = models.BooleanField()
    enabled_event_30120 = models.BooleanField()
    enabled_event_30130 = models.BooleanField()
    enabled_event_30140 = models.BooleanField()
    enabled_event_30160 = models.BooleanField()
    enabled_event_40000 = models.BooleanField()
    enabled_event_40010 = models.BooleanField()
    enabled_event_40020 = models.BooleanField()
    enabled_event_40030 = models.BooleanField()
    enabled_event_40040 = models.BooleanField()
    enabled_event_40050 = models.BooleanField()
    enabled_event_40100 = models.BooleanField()
    enabled_event_40110 = models.BooleanField()
    enabled_event_40220 = models.BooleanField()
    enabled_event_40230 = models.BooleanField()
    enabled_event_40240 = models.BooleanField()
    enabled_event_40250 = models.BooleanField()
    phot1_voltage_on = models.BooleanField()
    phot2_voltage_on = models.BooleanField()
    phot3_voltage_on = models.BooleanField()
    chu1_voltage_on = models.BooleanField()
    chu2_voltage_on = models.BooleanField()
    DAYLIGHT_NOT_DETECTED = "DN"
    DAYLIGHT_DETECTED = "DD"
    DAYLIGHT_DETECTED_CHOICES = (
        (DAYLIGHT_DETECTED, "Daylight detected"),
        (DAYLIGHT_NOT_DETECTED, "Daylight not detected")
    )
    daylight_detected = models.CharField(max_length=2,
                                         choices=DAYLIGHT_DETECTED_CHOICES,
                                         default=DAYLIGHT_DETECTED)
    mmia_internal_triggers = models.IntegerField() # Count of frames containing CHU or PHOT trigger(s). The counter resets to 0 at SW boot or when Triggered Data Collection Submode is entered.
    mxgs_triggers_sent = models.IntegerField()
    mxgs_triggers_received = models.IntegerField()
    priority1_observations = models.IntegerField()
    priority2_observations = models.IntegerField()
    priority3_observations = models.IntegerField()
    priority1_observation_downlinks = models.IntegerField() # Observations sucessfully transferred to downlink buffer.
    priority2_observation_downlinks = models.IntegerField() # Observations sucessfully transferred to downlink buffer.
    priority3_observation_downlinks = models.IntegerField() # Observations sucessfully transferred to downlink buffer.
    phot1_temp = models.IntegerField()
    phot2_temp = models.IntegerField()
    phot3_temp = models.IntegerField()
    chu1_temp = models.IntegerField()
    chu2_temp = models.IntegerField()
    dpu_1v_current = models.IntegerField()
    dpu_25v_current = models.IntegerField() # 2.5volt
    dpu_33v_current = models.IntegerField() # 3.3volt
    dpu_internal_temp0 = models.IntegerField()
    dpu_internal_temp1 = models.IntegerField()
    pow_5v_neg = models.IntegerField()
    pow_5v = models.IntegerField()
    pow_12v = models.IntegerField()
    pow_36v = models.IntegerField()
    pow_48v = models.IntegerField()
    pow_drain_volt_chu1 = models.IntegerField()
    pow_drain_volt_chu2 = models.IntegerField()
    pow_20v_to_45v_chu1 = models.IntegerField()
    pow_20v_to_45v_chu2 = models.IntegerField()
    pow_7v_neg = models.IntegerField()
    pow_5v_neg_primary = models.IntegerField()
    pow_5v_primary = models.IntegerField()
    pow_12v_primary = models.IntegerField()
    pow_36v_primary = models.IntegerField()
    pow_48v_primary = models.IntegerField()
    pow_internal_tmon = models.IntegerField()

class Mmia_hk_startup(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()
    tcp_count_internal = models.IntegerField()
    acquisition_start_time = models.IntegerField() # Current value (in msecs). The counter is reset to 0 by TCP and couts up to ~10^6 before next TCP. Value range 0-(2^32)-1
    boot_status_completed_with_errors = models.BooleanField()
    boot_status_completed_no_errors = models.BooleanField()
    boot_status_asw_load_ok = models.BooleanField()
    boot_status_system_memory_test_ok = models.BooleanField()
    boot_software_version_major = models.BooleanField()
    boot_software_version_minor = models.BooleanField()
    application_software_version_major = models.IntegerField()
    application_software_version_minor = models.IntegerField()
    application_software_version_patch = models.IntegerField()

class Mmia_hk_buffer_resource(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()
    tcp_count_internal = models.IntegerField()
    acquisition_start_time = models.IntegerField() # Current value (in msecs). The counter is reset to 0 by TCP and couts up to ~10^6 before next TCP. Value range 0-(2^32)-1
    nonscience_downlink_buffer_usage = models.IntegerField() # In percentage
    science_downlink_buffer_usage = models.IntegerField()
    priority1_data_buffer_usage = models.IntegerField()
    priority2_data_buffer_usage = models.IntegerField()
    priority3_data_buffer_usage = models.IntegerField()
    discarded_tc_packets = models.IntegerField()
    discarded_tm_nonscience_packets = models.IntegerField()
    discarded_priority3_observations = models.IntegerField()
    discarded_priority2_observations = models.IntegerField()
    discarded_priority1_observations = models.IntegerField()

class Mmia_hk_dpu(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()
    tcp_count_internal = models.IntegerField()
    acquisition_start_time = models.IntegerField() # Current value (in msecs). The counter is reset to 0 by TCP and couts up to ~10^6 before next TCP. Value range 0-(2^32)-1
    voltage_supply_1v = models.IntegerField()
    voltage_supply_25v = models.IntegerField() # 2.5v
    voltage_supply_33v = models.IntegerField() # 3.3v
    current_supply_1v = models.IntegerField()
    current_supply_25v = models.IntegerField() # 2.5v
    current_supply_33v = models.IntegerField() # 3.3v
    dpu_internal_tmon0 = models.IntegerField()
    dpu_internal_tmon1 = models.IntegerField()
    daylight_sensor_signal = models.IntegerField()
    DAYLIGHT_NOT_DETECTED = "DN"
    DAYLIGHT_DETECTED = "DD"
    DAYLIGHT_DETECTED_CHOICES = (
        (DAYLIGHT_DETECTED, "Daylight detected"),
        (DAYLIGHT_NOT_DETECTED, "Daylight not detected")
    )
    daylight_detected = models.CharField(max_length=2,
                                         choices=DAYLIGHT_DETECTED_CHOICES,
                                         default=DAYLIGHT_DETECTED)
    phot1_voltage_on = models.BooleanField()
    phot2_voltage_on = models.BooleanField()
    phot3_voltage_on = models.BooleanField()
    chu1_voltage_on = models.BooleanField()
    chu2_voltage_on = models.BooleanField()
    pow_5v_neg_primary_current = models.IntegerField()
    pow_5v_primary_current = models.IntegerField()
    pow_12v_primary_current = models.IntegerField()
    pow_36v_primary_current = models.IntegerField()
    pow_48v_primary_current = models.IntegerField()
    pow_5v_neg = models.IntegerField()
    pow_5v = models.IntegerField()
    pow_12v = models.IntegerField()
    pow_36v = models.IntegerField()
    pow_48v = models.IntegerField()
    pow_32v_chu1 = models.IntegerField()
    pow_32v_chu2 = models.IntegerField()
    pow_20v_to_45v_chu1 = models.IntegerField()
    pow_20v_to_45v_chu2 = models.IntegerField()
    pow_7v_neg = models.IntegerField()
    pow_internal_tmon_channel1 = models.IntegerField()
    dpu_internal_temp_channel5 = models.IntegerField()
    dpu_internal_temp_channel6 = models.IntegerField()

class Mmia_hk_chu(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()
    tcp_count_internal = models.IntegerField()
    acquisition_start_time = models.IntegerField() # Current value (in msecs). The counter is reset to 0 by TCP and couts up to ~10^6 before next TCP. Value range 0-(2^32)-1
    temp_ccd_chu1 = models.IntegerField()
    temp_ccd_chu2 = models.IntegerField()
    background_chu1 = models.IntegerField()
    background_chu2 = models.IntegerField()
    background_threshold_chu1 = models.IntegerField()
    background_threshold_chu2 = models.IntegerField()
    pow_20v_to_45v_chu1 = models.IntegerField()
    pow_20v_to_45v_chu2 = models.IntegerField()
    pow_5v_neg = models.IntegerField()
    pow_5v = models.IntegerField()
    pow_5v_neg_primary_current = models.IntegerField()
    pow_5v_primary_current = models.IntegerField()
    pow_12v = models.IntegerField()
    pow_12v_primary_current = models.IntegerField()
    pow_drain_volt_chu1 = models.IntegerField()
    pow_drain_volt_chu2 = models.IntegerField()

class Mmia_hk_phot(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()
    tcp_count_internal = models.IntegerField()
    acquisition_start_time = models.IntegerField() # Current value (in msecs). The counter is reset to 0 by TCP and couts up to ~10^6 before next TCP. Value range 0-(2^32)-1
    phot1_temp = models.IntegerField()
    phot2_temp = models.IntegerField()
    phot3_temp = models.IntegerField()
    background_phot1 = models.IntegerField()
    background_phot2 = models.IntegerField()
    background_phot3 = models.IntegerField()
    background_threshold_phot1 = models.IntegerField()
    background_threshold_phot2 = models.IntegerField()
    background_threshold_phot3 = models.IntegerField()
    pow_5v_neg = models.IntegerField()
    pow_5v = models.IntegerField()
    pow_5v_neg_primary_current = models.IntegerField()
    pow_5v_primary_current = models.IntegerField()

class MMIAEventReport(models.Model):
    private_header = 0 #TODO Make dis!
    packet_length = models.IntegerField()
    INFORMATION = "INF"
    ADVISORY = "ADV"
    CAUTION = "CAU"
    WARNING = "WAR"
    EMERGENCY = "EME"
    EVENT_SEVERITY_CHOICES = (
        (INFORMATION, "Information"),
        (ADVISORY, "Advisory"),
        (CAUTION, "Caution"),
        (WARNING, "Warning"),
        (EMERGENCY, "Emergency")
    )
    event_severity = models.CharField(max_length=3,
                                         choices=EVENT_SEVERITY_CHOICES,
                                         default=INFORMATION)
    EVENT_30000 = "30000"
    EVENT_30010 = "30010"
    EVENT_30050 = "30050"
    EVENT_30060 = "30060"
    EVENT_30070 = "30070"
    EVENT_30080 = "30080"
    EVENT_30090 = "30090"
    EVENT_30100 = "30100"
    EVENT_30110 = "30110"
    EVENT_30120 = "30120"
    EVENT_30130 = "30130"
    EVENT_30140 = "30140"
    EVENT_30160 = "30160"
    EVENT_40000 = "40000"
    EVENT_40010 = "40010"
    EVENT_40020 = "40020"
    EVENT_40030 = "40030"
    EVENT_40040 = "40040"
    EVENT_40050 = "40050"
    EVENT_40100 = "40100"
    EVENT_40110 = "40110"
    EVENT_40220 = "40220"
    EVENT_40230 = "40230"
    EVENT_40240 = "40240"
    EVENT_40250 = "40250"
    EVENT_ID_CHOICES = (
        (EVENT_30000, "Software change, severity 0"),
        (EVENT_30010, "Submode change, severity 0"),
        (EVENT_30050, "Full science data collection buffer, severity 1"),
        (EVENT_30060, "Science data collection buffer has free space after being full, severity 0"),
        (EVENT_30070, "Science observation with priority 3 overwritten by priority 1, severity 1"),
        (EVENT_30080, "Science observation overwrites one or more with priority 3, severity 1"),
        (EVENT_30090, "Science observation with priority 3 discarded due to data collection buffer being full, severity 1"),
        (EVENT_30100, "Science observation with priority 2 discarded due to data collection buffer being full, severity 2"),
        (EVENT_30110, "Science observation with priority 1 discarded due to data collection buffer being full, severity 3"),
        (EVENT_30120, "Science observation transferred from data collection buffer to science downlink buffer, severity 0"),
        (EVENT_30130, "Science downlink buffer full, data transfer function is suspended, severity 1"),
        (EVENT_30140, "Science downlink buffer has free space after being full, data transfer function is resumed, severity 0"),
        (EVENT_30160, "Trigger occured, trigger is sent to MXGS, severity 0"),
        (EVENT_40000, "Validation of parameters of a configuration table failed, severity 3"),
        (EVENT_40010, "Trigger occured, or was received from MXGS, severity 0"),
        (EVENT_40020, "Output from daylight sensor resulted in PHOTs being powered off, severity 3"),
        (EVENT_40030, "Output from daylight sensor resulted in PHOTs being powered on, severity 3"),
        (EVENT_40040, "PHOTs are powered off due to a timeout of the requested power-on duration, severity 2"),
        (EVENT_40050, "Power status of PHOTs changed, severity 1"),
        (EVENT_40100, "Successful transfer of a Triggered Observation to the data collection buffer, severity 0"),
        (EVENT_40110, "Successful transfer of a Timed Observation to the data collection buffer, severity 0"),
        (EVENT_40220, "CHU does not acknowledge a command, severity 3"),
        (EVENT_40230, "Transfer from ring buffer to VMM does not complete, severity 3"),
        (EVENT_40240, "No CHU frames are received, severity 3"),
        (EVENT_40250, "One or more software task scheduling errors are detected, severity 3"),
    )
    event_id = models.CharField(max_length=5,
                                choices=EVENT_SEVERITY_CHOICES,
                                default=EVENT_30000)
    
    utc_year = models.IntegerField()
    utc_msec = models.IntegerField()
    utc_seconds = models.IntegerField()

class MMIAEventID300000(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    BOOTMODE = "BO"
    CONFMODE = "CF"
    OPMODE = "OP"
    MODE_CHOICES = (
        (BOOTMODE, "Boot mode"),
        (CONFMODE, "Configuration mode"),
        (OPMODE, "Operational mode")
    )
    current_mode = models.CharField(max_length=2,
                                    choices=MODE_CHOICES,
                                    default=BOOTMODE)

class MMIAEventID30010(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    UNDEFINED = "UN"
    TRIGGERED = "TR"
    TIMED = "TI"
    DATAPROCESS = "DA"
    SUBMODE_CHOICES = (
        (UNDEFINED, "Undefined"),
        (TRIGGERED, "Triggered data collection"),
        (TIMED, "Timed data collection"),
        (DATAPROCESS, "Data processing")
    )
    submode = models.CharField(max_length=2,
                                  choices=SUBMODE_CHOICES,
                                  default=TRIGGERED)

class MMIAEventID30070(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    priority3_observations_overwritten = models.IntegerField()

class MMIAEventID30080(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    priority3_observations_overwritten = models.IntegerField()

class MMIAEventID30120(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    observation_priority = models.IntegerField()

class MMIAEventID30160(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    tcp_count_internal = models.IntegerField()
    dpu_timer_value = models.IntegerField()

class MMIAEventID40000(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    memory_id = models.IntegerField()
    failed_parameters = models.IntegerField()

class MMIAEventID40000FailedParameterPair(models.Model):
    eventid40000 = models.ForeignKey(MMIAEventID40000, on_delete=models.CASCADE)
    parameter_offset = models.PositiveIntegerField()
    parameter_value = models.PositiveIntegerField()

class MMIAEventID40010(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    trigger_phot1 = models.BooleanField()
    trigger_phot2 = models.BooleanField()
    trigger_phot3 = models.BooleanField()
    trigger_chu1_row = models.BooleanField()
    trigger_chu1_column = models.BooleanField()
    trigger_chu2_row = models.BooleanField()
    trigger_chu2_column = models.BooleanField()
    trigger_from_mxgs_enabled = models.BooleanField()
    trigger_from_mxgs_received = models.BooleanField()
    tcp_count_internal = models.IntegerField()
    dpu_timer_value = models.IntegerField()

class MMIAEventID40050(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    phot1_power = models.BooleanField()
    phot2_power = models.BooleanField()
    phot3_power = models.BooleanField()

class MMIAEventID40100(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    observation_size = models.IntegerField()

class MMIAEventID40110(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    observation_size = models.IntegerField()

class MMIAEventID40220(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    chu_id = models.PositiveSmallIntegerField()
    chu_code = models.IntegerField()
    chu_data = models.IntegerField()

class MMIAEventID40230(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    sensor_id_flag_phot1 = models.BooleanField()
    sensor_id_flag_phot2 = models.BooleanField()
    sensor_id_flag_phot3 = models.BooleanField()
    sensor_id_flag_chu1 = models.BooleanField()
    sensor_id_flag_chu2 = models.BooleanField()

class MMIAEventID40240(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    CHU_FRAME_INDEX_1 = "CF1"
    CHU_FRAME_INDEX_2 = "CF2"
    CHU_METADATA_INDEX_1 = "CM1"
    CHU_METADATA_INDEX_2 = "CM2"
    CHU_FRAME_INDEX_AT_TCP_1 = "CFT1"
    CHU_FRAME_INDEX_AT_TCP_2 = "CFT2"
    CHU_METADATA_INDEX_AT_TCP_1 = "CMT1"
    CHU_METADATA_INDEX_AT_TCP_2 = "CMT2"
    REPORTED_IN_REGISTER_CHOICES = (
        (CHU_FRAME_INDEX_1, "CF1"),
        (CHU_FRAME_INDEX_2, "CF2"),
        (CHU_METADATA_INDEX_1, "CM1"),
        (CHU_METADATA_INDEX_2, "CM2"),
        (CHU_FRAME_INDEX_AT_TCP_1, "CFT1"),
        (CHU_FRAME_INDEX_AT_TCP_2, "CFT2"),
        (CHU_METADATA_INDEX_AT_TCP_1, "CMT1"),
        (CHU_METADATA_INDEX_AT_TCP_2, "CMT2"),
    )
    reported_in_register = models.CharField(max_length=4,
                               choices=REPORTED_IN_REGISTER_CHOICES,
                               default=CHU_FRAME_INDEX_1)

class MMIAEventID40250(models.Model):
    event_report = models.ForeignKey(MMIAEventReport, on_delete=models.CASCADE)
    scheduling_errors = models.IntegerField()

class MMIAEventID40250SchedulingError(models.Model):
    eventid40250 = models.ForeignKey(MMIAEventID40250, on_delete=models.CASCADE)
    task_id = models.IntegerField()
    TASK_QUEUE_FULL = "TQF"
    TASK_MISSED_DEADLINE = "TMD"
    ERROR_TYPE_CHOICES = (
        (TASK_QUEUE_FULL, "Task queue of a sporadic task is full"),
        (TASK_MISSED_DEADLINE, "Task has missed its defined deadline")
    )
    error_type = models.CharField(max_length=3,
                                  choices=ERROR_TYPE_CHOICES,
                                  default=TASK_QUEUE_FULL)
    response_time = models.IntegerField

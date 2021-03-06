from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSPSUFullHousekeepingTM (models.Model):
    packet_length                   = models.IntegerField('Packet length')
    utc_year                        = models.IntegerField('UTC year')
    utc_msec                        = models.IntegerField('UTC msec')
    utc_seconds                     = models.IntegerField('UTC seconds')
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    bgo4_analog_plus2v5_current        =models.IntegerField()
    bgo4_analog_plus2v5_voltage        =models.IntegerField()
    bgo4_analog_plus5v_current        =models.IntegerField()
    bgo4_analog_plus5v_voltage        =models.IntegerField()
    bgo4_analog_minus5v_current        =models.IntegerField()
    bgo4_analog_minus5v_voltage        =models.IntegerField()
    bgo4_fpga_1v5_current        =models.IntegerField()
    bgo4_fpga_1v5_voltage        =models.IntegerField()
    bgo4_fpga_2v5_current        =models.IntegerField()
    bgo4_fpga_2v5_voltage        =models.IntegerField()
    bgo4_fpga_3v3_current        =models.IntegerField()
    bgo4_fpga_3v3_voltage        =models.IntegerField()
    bgo4_hv_supply_5v_current        =models.IntegerField()
    bgo4_hv_supply_5v_voltage        =models.IntegerField()
    bgo4_hv_vmon_voltage        =models.IntegerField()
    bgo4_dcdc_temperature        =models.IntegerField()
    bgo4_ldo_temperature        =models.IntegerField()
    bgo4_hvps_temperature        =models.IntegerField()
    bgo4_temp1_temperature        =models.IntegerField()
    bgo4_temp2_temperature        =models.IntegerField()
    czt4_asic_plus1v5_current        =models.IntegerField()
    czt4_asic_plus1v5_voltage        =models.IntegerField()
    czt4_asic_minus2v_current        =models.IntegerField()
    czt4_asic_minus2v_voltage        =models.IntegerField()
    czt4_analog_plus2v5_current        =models.IntegerField()
    czt4_analog_plus2v5_voltage        =models.IntegerField()
    czt4_analog_plus5v_current        =models.IntegerField()
    czt4_analog_plus5v_voltage        =models.IntegerField()
    czt4_analog_minus5v_current        =models.IntegerField()
    czt4_analog_minus5v_voltage        =models.IntegerField()
    czt4_fpga_1v5_current        =models.IntegerField()
    czt4_fpga_1v5_voltage        =models.IntegerField()
    czt4_fpga_2v5_current        =models.IntegerField()
    czt4_fpga_2v5_voltage        =models.IntegerField()
    czt4_fpga_3v3_current        =models.IntegerField()
    czt4_fpga_3v3_voltage        =models.IntegerField()
    czt4_fpga_5v_current        =models.IntegerField()
    czt4_fpga_5v_voltage        =models.IntegerField()
    czt4_hv_supply_5v_current        =models.IntegerField()
    czt4_hv_supply_5v_voltage        =models.IntegerField()
    czt4_hv_vmon_voltage        =models.IntegerField()
    czt4_dcdc_temperature        =models.IntegerField()
    czt4_ldo_temperature        =models.IntegerField()
    czt4_hvps_temperature        =models.IntegerField()
    czt4_temp1_temperature        =models.IntegerField()
    czt4_temp2_temperature        =models.IntegerField()
    bgo3_analog_plus2v5_current        =models.IntegerField()
    bgo3_analog_plus2v5_voltage        =models.IntegerField()
    bgo3_analog_plus5v_current        =models.IntegerField()
    bgo3_analog_plus5v_voltage        =models.IntegerField()
    bgo3_analog_minus5v_current        =models.IntegerField()
    bgo3_analog_minus5v_voltage        =models.IntegerField()
    bgo3_fpga_1v5_current        =models.IntegerField()
    bgo3_fpga_1v5_voltage        =models.IntegerField()
    bgo3_fpga_2v5_current        =models.IntegerField()
    bgo3_fpga_2v5_voltage        =models.IntegerField()
    bgo3_fpga_3v3_current        =models.IntegerField()
    bgo3_fpga_3v3_voltage        =models.IntegerField()
    bgo3_hv_supply_5v_current        =models.IntegerField()
    bgo3_hv_supply_5v_voltage        =models.IntegerField()
    bgo3_hv_vmon_voltage        =models.IntegerField()
    bgo3_dcdc_temperature        =models.IntegerField()
    bgo3_ldo_temperature        =models.IntegerField()
    bgo3_hvps_temperature        =models.IntegerField()
    bgo3_temp1_temperature        =models.IntegerField()
    bgo3_temp2_temperature        =models.IntegerField()
    czt3_asic_plus1v5_current        =models.IntegerField()
    czt3_asic_plus1v5_voltage        =models.IntegerField()
    czt3_asic_minus2v_current        =models.IntegerField()
    czt3_asic_minus2v_voltage        =models.IntegerField()
    czt3_analog_plus2v5_current        =models.IntegerField()
    czt3_analog_plus2v5_voltage        =models.IntegerField()
    czt3_analog_plus5v_current        =models.IntegerField()
    czt3_analog_plus5v_voltage        =models.IntegerField()
    czt3_analog_minus5v_current        =models.IntegerField()
    czt3_analog_minus5v_voltage        =models.IntegerField()
    czt3_fpga_1v5_current        =models.IntegerField()
    czt3_fpga_1v5_voltage        =models.IntegerField()
    czt3_fpga_2v5_current        =models.IntegerField()
    czt3_fpga_2v5_voltage        =models.IntegerField()
    czt3_fpga_3v3_current        =models.IntegerField()
    czt3_fpga_3v3_voltage        =models.IntegerField()
    czt3_fpga_5v_current        =models.IntegerField()
    czt3_fpga_5v_voltage        =models.IntegerField()
    czt3_hv_supply_5v_current        =models.IntegerField()
    czt3_hv_supply_5v_voltage        =models.IntegerField()
    czt3_hv_vmon_voltage        =models.IntegerField()
    czt3_dcdc_temperature        =models.IntegerField()
    czt3_ldo_temperature        =models.IntegerField()
    czt3_hvps_temperature        =models.IntegerField()
    czt3_temp1_temperature        =models.IntegerField()
    czt3_temp2_temperature        =models.IntegerField()
    bgo2_analog_plus2v5_current        =models.IntegerField()
    bgo2_analog_plus2v5_voltage        =models.IntegerField()
    bgo2_analog_plus5v_current        =models.IntegerField()
    bgo2_analog_plus5v_voltage        =models.IntegerField()
    bgo2_analog_minus5v_current        =models.IntegerField()
    bgo2_analog_minus5v_voltage        =models.IntegerField()
    bgo2_fpga_1v5_current        =models.IntegerField()
    bgo2_fpga_1v5_voltage        =models.IntegerField()
    bgo2_fpga_2v5_current        =models.IntegerField()
    bgo2_fpga_2v5_voltage        =models.IntegerField()
    bgo2_fpga_3v3_current        =models.IntegerField()
    bgo2_fpga_3v3_voltage        =models.IntegerField()
    bgo2_hv_supply_5v_current        =models.IntegerField()
    bgo2_hv_supply_5v_voltage        =models.IntegerField()
    bgo2_hv_vmon_voltage        =models.IntegerField()
    bgo2_dcdc_temperature        =models.IntegerField()
    bgo2_ldo_temperature        =models.IntegerField()
    bgo2_hvps_temperature        =models.IntegerField()
    bgo2_temp1_temperature        =models.IntegerField()
    bgo2_temp2_temperature        =models.IntegerField()
    czt2_asic_plus1v5_current        =models.IntegerField()
    czt2_asic_plus1v5_voltage        =models.IntegerField()
    czt2_asic_minus2v_current        =models.IntegerField()
    czt2_asic_minus2v_voltage        =models.IntegerField()
    czt2_analog_plus2v5_current        =models.IntegerField()
    czt2_analog_plus2v5_voltage        =models.IntegerField()
    czt2_analog_plus5v_current        =models.IntegerField()
    czt2_analog_plus5v_voltage        =models.IntegerField()
    czt2_analog_minus5v_current        =models.IntegerField()
    czt2_analog_minus5v_voltage        =models.IntegerField()
    czt2_fpga_1v5_current        =models.IntegerField()
    czt2_fpga_1v5_voltage        =models.IntegerField()
    czt2_fpga_2v5_current        =models.IntegerField()
    czt2_fpga_2v5_voltage        =models.IntegerField()
    czt2_fpga_3v3_current        =models.IntegerField()
    czt2_fpga_3v3_voltage        =models.IntegerField()
    czt2_fpga_5v_current        =models.IntegerField()
    czt2_fpga_5v_voltage        =models.IntegerField()
    czt2_hv_supply_5v_current        =models.IntegerField()
    czt2_hv_supply_5v_voltage        =models.IntegerField()
    czt2_hv_vmon_voltage        =models.IntegerField()
    czt2_dcdc_temperature        =models.IntegerField()
    czt2_ldo_temperature        =models.IntegerField()
    czt2_hvps_temperature        =models.IntegerField()
    czt2_temp1_temperature        =models.IntegerField()
    czt2_temp2_temperature        =models.IntegerField()
    bgo1_analog_plus2v5_current        =models.IntegerField()
    bgo1_analog_plus2v5_voltage        =models.IntegerField()
    bgo1_analog_plus5v_current        =models.IntegerField()
    bgo1_analog_plus5v_voltage        =models.IntegerField()
    bgo1_analog_minus5v_current        =models.IntegerField()
    bgo1_analog_minus5v_voltage        =models.IntegerField()
    bgo1_fpga_1v5_current        =models.IntegerField()
    bgo1_fpga_1v5_voltage        =models.IntegerField()
    bgo1_fpga_2v5_current        =models.IntegerField()
    bgo1_fpga_2v5_voltage        =models.IntegerField()
    bgo1_fpga_3v3_current        =models.IntegerField()
    bgo1_fpga_3v3_voltage        =models.IntegerField()
    bgo1_hv_supply_5v_current        =models.IntegerField()
    bgo1_hv_supply_5v_voltage        =models.IntegerField()
    bgo1_hv_vmon_voltage        =models.IntegerField()
    bgo1_dcdc_temperature        =models.IntegerField()
    bgo1_ldo_temperature        =models.IntegerField()
    bgo1_hvps_temperature        =models.IntegerField()
    bgo1_temp1_temperature        =models.IntegerField()
    bgo1_temp2_temperature        =models.IntegerField()
    czt1_asic_plus1v5_current        =models.IntegerField()
    czt1_asic_plus1v5_voltage        =models.IntegerField()
    czt1_asic_minus2v_current        =models.IntegerField()
    czt1_asic_minus2v_voltage        =models.IntegerField()
    czt1_analog_plus2v5_current        =models.IntegerField()
    czt1_analog_plus2v5_voltage        =models.IntegerField()
    czt1_analog_plus5v_current        =models.IntegerField()
    czt1_analog_plus5v_voltage        =models.IntegerField()
    czt1_analog_minus5v_current        =models.IntegerField()
    czt1_analog_minus5v_voltage        =models.IntegerField()
    czt1_fpga_1v5_current        =models.IntegerField()
    czt1_fpga_1v5_voltage        =models.IntegerField()
    czt1_fpga_2v5_current        =models.IntegerField()
    czt1_fpga_2v5_voltage        =models.IntegerField()
    czt1_fpga_3v3_current        =models.IntegerField()
    czt1_fpga_3v3_voltage        =models.IntegerField()
    czt1_fpga_5v_current        =models.IntegerField()
    czt1_fpga_5v_voltage        =models.IntegerField()
    czt1_hv_supply_5v_current        =models.IntegerField()
    czt1_hv_supply_5v_voltage        =models.IntegerField()
    czt1_hv_vmon_voltage        =models.IntegerField()
    czt1_dcdc_temperature        =models.IntegerField()
    czt1_ldo_temperature        =models.IntegerField()
    czt1_hvps_temperature        =models.IntegerField()
    czt1_temp1_temperature        =models.IntegerField()
    czt1_temp2_temperature        =models.IntegerField()
    psuc_dcdc_temperature        =models.IntegerField()
    psuc_pcb_temperature        =models.IntegerField()
    psuc_fpga_plus1v5_current        =models.IntegerField()
    psuc_fpga_plus1v5_voltage        =models.IntegerField()
    psuc_plus5v_current        =models.IntegerField()
    psuc_plus5v_voltage        =models.IntegerField()
    psuc_plus3v3_current        =models.IntegerField()
    psuc_plus3v3_voltage        =models.IntegerField()
    psuc_analog_plus15v_current        =models.IntegerField()
    psuc_analog_plus15v_voltage        =models.IntegerField()
    psuc_analog_minus15v_current        =models.IntegerField()
    psuc_analog_minus15v_voltage        =models.IntegerField()
    hvps_enable_register        =models.IntegerField()
    lvps_enable_register        =models.IntegerField()
    external_relay_enable_register        =models.IntegerField()
    hv_value_control_register_for_bgo4        =models.IntegerField()
    hv_value_control_register_for_czt4        =models.IntegerField()
    hv_value_control_register_for_bgo3        =models.IntegerField()
    hv_value_control_register_for_czt3        =models.IntegerField()
    hv_value_control_register_for_bgo2        =models.IntegerField()
    hv_value_control_register_for_czt2        =models.IntegerField()
    hv_value_control_register_for_bgo1        =models.IntegerField()
    hv_value_control_register_for_czt1        =models.IntegerField()
    fault_flag_register_for_bgo4        =models.IntegerField()
    fault_flag_register_for_czt4        =models.IntegerField()
    fault_flag_register_for_bgo3        =models.IntegerField()
    fault_flag_register_for_czt3        =models.IntegerField()
    fault_flag_register_for_bgo2        =models.IntegerField()
    fault_flag_register_for_czt2        =models.IntegerField()
    fault_flag_register_for_bgo1        =models.IntegerField()
    fault_flag_register_for_czt1        =models.IntegerField()
    n_adc_channel_used_for_measurements_0_3        =models.IntegerField()
    general_error_register        =models.IntegerField()
    receive_error_count        =models.IntegerField()
    seu_generated_double_error_in_a_byte_detected_count        =models.IntegerField()
    seu_generated_single_error_in_a_byte_corrected_count        =models.IntegerField()
    version_of_psuc_fpga_configuration        =models.IntegerField()
    unlocking_code_register        =models.IntegerField()
    debug_mode_register        =models.IntegerField()
    debug_multiplexor_address        =models.IntegerField()
    scanning_fsm_clock_divider_23_16_deleted        =models.IntegerField()
    scanning_fsm_clock_divider_15_8_deleted        =models.IntegerField()
    scanning_fsm_clock_divider_7_0_deleted        =models.IntegerField()
    clock_divider_for_hv_dac_deleted        =models.IntegerField()
    clock_divider_for_adc_deleted        =models.IntegerField()
    bgo_hv_configuration_maximum_value        =models.IntegerField()
    czt_hv_configuration_maximum_value        =models.IntegerField()
    hv_closed_loop_regulator_enable_register        =models.IntegerField()
    hv_regulator_integration_parameter_for_bgo4        =models.IntegerField()
    hv_regulator_integration_parameter_for_czt4        =models.IntegerField()
    hv_regulator_integration_parameter_for_bgo3        =models.IntegerField()
    hv_regulator_integration_parameter_for_czt3        =models.IntegerField()
    hv_regulator_integration_parameter_for_bgo2        =models.IntegerField()
    hv_regulator_integration_parameter_for_czt2        =models.IntegerField()
    hv_regulator_integration_parameter_for_bgo1        =models.IntegerField()
    hv_regulator_integration_parameter_for_czt1        =models.IntegerField()


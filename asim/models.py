from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime


# Create your models here.



# MXGS TGF Observation
class MXGSTGFObservation(models.Model):
    observation_id                  =models.IntegerField('Observation ID')
    utc_year                        =models.IntegerField('UTC year')
    utc_seconds                     =models.IntegerField('UTC seconds')
    utc_msec                        =models.IntegerField('UTC msec')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    dpu_count                       =models.IntegerField()
    dpu_count_prereset              =models.IntegerField()
    dau_bgo_1_int_tmon_chan1        =models.IntegerField()
    dau_bgo_1_int_tmon_chan2        =models.IntegerField()
    dau_bgo_1_int_tmon_chan3        =models.IntegerField()
    dau_bgo_1_int_tmon_chan4        =models.IntegerField()
    dau_bgo_2_int_tmon_chan1        =models.IntegerField()
    dau_bgo_2_int_tmon_chan2        =models.IntegerField()
    dau_bgo_2_int_tmon_chan3        =models.IntegerField()
    dau_bgo_2_int_tmon_chan4        =models.IntegerField()
    dau_bgo_3_int_tmon_chan1        =models.IntegerField()
    dau_bgo_3_int_tmon_chan2        =models.IntegerField()
    dau_bgo_3_int_tmon_chan3        =models.IntegerField()
    dau_bgo_3_int_tmon_chan4        =models.IntegerField()
    dau_bgo_4_int_tmon_chan1        =models.IntegerField()
    dau_bgo_4_int_tmon_chan2        =models.IntegerField()
    dau_bgo_4_int_tmon_chan3        =models.IntegerField()
    dau_bgo_4_int_tmon_chan4        =models.IntegerField()
    led_short_win_lr_pulse_height   =models.IntegerField()
    led_short_win_upr_pulse_height  =models.IntegerField()
    led_long_win_lr_pulse_height    =models.IntegerField()
    led_long_win_upr_pulse_height   =models.IntegerField()
    hed_short_win_lr_pulse_height   =models.IntegerField()
    hed_short_win_upr_pulse_height  =models.IntegerField()
    hed_long_win_lr_pulse_height    =models.IntegerField()
    hed_long_win_upr_pulse_height   =models.IntegerField()
    led_short_win_anticoin_time     =models.IntegerField()
    led_long_win_anticoin_time      =models.IntegerField()
    hed_short_win_anticoin_time     =models.IntegerField()
    hed_long_win_anticoin_time      =models.IntegerField()
    led_short_win_flag1             =models.BooleanField()
    led_short_win_flag2             =models.BooleanField()
    led_short_win_flag3             =models.BooleanField()
    led_long_win_flag               =models.BooleanField()
    hed_short_win_flag1             =models.BooleanField()
    hed_short_win_flag2             =models.BooleanField()
    hed_short_win_flag3             =models.BooleanField()
    hed_long_win_flag               =models.BooleanField()
    trig_mmia_enabled               =models.BooleanField()
    trig_mmia_recd                  =models.BooleanField()
    led_short_win_dur_1             =models.IntegerField()
    led_short_win_dur_2             =models.IntegerField()
    led_short_win_dur_3             =models.IntegerField()
    led_long_win_dur                =models.IntegerField()
    hed_short_win_dur_1             =models.IntegerField()
    hed_short_win_dur_2             =models.IntegerField()
    hed_short_win_dur_3             =models.IntegerField()
    hed_long_win_dur                =models.IntegerField()
    led_short_win_thresh_1          =models.IntegerField()
    led_short_win_thresh_2          =models.IntegerField()
    led_short_win_thresh_3          =models.IntegerField()
    led_long_win_thresh             =models.IntegerField()
    hed_short_win_thresh_1          =models.IntegerField()
    hed_short_win_thresh_2          =models.IntegerField()
    hed_short_win_thresh_3          =models.IntegerField()
    hed_long_win_thresh             =models.IntegerField()
    mxgs_trig_count                 =models.BigIntegerField()
    mxgs_trig_tcp_count             =models.IntegerField()
    mxgs_trig_dpu_count             =models.IntegerField()
    num_counts                      =models.IntegerField()
    detector_counts                 =models.FileField()
    
 
# Background Observation
class BackgroundObservation(models.Model)
    dau_bgo_1_int_tmon_chan1        =models.IntegerField()
    dau_bgo_1_int_tmon_chan2        =models.IntegerField()
    dau_bgo_1_int_tmon_chan3        =models.IntegerField()
    dau_bgo_1_int_tmon_chan4        =models.IntegerField()
    dau_bgo_2_int_tmon_chan1        =models.IntegerField()
    dau_bgo_2_int_tmon_chan2        =models.IntegerField()
    dau_bgo_2_int_tmon_chan3        =models.IntegerField()
    dau_bgo_2_int_tmon_chan4        =models.IntegerField()
    dau_bgo_3_int_tmon_chan1        =models.IntegerField()
    dau_bgo_3_int_tmon_chan2        =models.IntegerField()
    dau_bgo_3_int_tmon_chan3        =models.IntegerField()
    dau_bgo_3_int_tmon_chan4        =models.IntegerField()
    dau_bgo_4_int_tmon_chan1        =models.IntegerField()
    dau_bgo_4_int_tmon_chan2        =models.IntegerField()
    dau_bgo_4_int_tmon_chan3        =models.IntegerField()
    dau_bgo_4_int_tmon_chan4        =models.IntegerField()
    led_short_win_lr_pulse_height   =models.IntegerField()
    led_short_win_upr_pulse_height  =models.IntegerField()
    led_long_win_lr_pulse_height    =models.IntegerField()
    led_long_win_upr_pulse_height   =models.IntegerField()
    hed_short_win_lr_pulse_height   =models.IntegerField()
    hed_short_win_upr_pulse_height  =models.IntegerField()
    hed_long_win_lr_pulse_height    =models.IntegerField()
    hed_long_win_upr_pulse_height   =models.IntegerField()
    led_short_win_anticoin_time     =models.IntegerField()
    led_long_win_anticoin_time      =models.IntegerField()
    hed_short_win_anticoin_time     =models.IntegerField()
    hed_long_win_anticoin_time      =models.IntegerField()
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
    hed_bin9_lr_boundary            =models.IntegerField()
    hed_bin9_upr_boundary           =models.IntegerField()
    led_short_win_dur_1             =models.IntegerField()
    led_short_win_dur_2             =models.IntegerField()
    led_short_win_dur_3             =models.IntegerField()
    led_long_win_dur                =models.IntegerField()
    hed_short_win_dur_1             =models.IntegerField()
    hed_short_win_dur_2             =models.IntegerField()
    hed_short_win_dur_3             =models.IntegerField()
    hed_long_win_dur                =models.IntegerField()

class BackgroundObservation1Second(models.Model):
    background_observation = models.ForeignKey(BackgroundObservation, on_delete=models.CASCADE)
    utc_year                        =models.IntegerField('UTC year')
    utc_seconds                     =models.IntegerField('UTC seconds')
    utc_msec                        =models.IntegerField('UTC msec')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    dpu_count_prereset              =models.IntegerField()
    UNDEFINED = 'UD'
    CONFMODE  = 'CF'
    OPMODE   = 'OP'
    SW_MODE_CHOICES = (
        (UNDEFINED , "Undefined"            ),
        (CONFMODE  , "Configuration mode"   ),
        (OPMODE    , "Operational mode"     ),
    )
    sw_mode = models.CharField(max_length=2,
                                      choices=SW_MODE_CHOICES,
                                      default=UNDEFINED)
    UNDEFINED                       = 'UD'
    TGFSEARCH                       = 'TG'
    HIGHBACKGROUND                  = 'HB'
    AURORALCAPTURE                  = 'AC'
    SW_SUBMODE_CHOICES = (
        (UNDEFINED     , "Undefined"        ),
        (TGFSEARCH     , "TGF Search mode"  ),
        (HIGHBACKGROUND, "High Background"  ),
        (AURORALCAPTURE, "Auroral capture"  ),
    )
    sw_submode = models.CharField(max_length=2,
                                      choices=SW_SUBMODE_CHOICES,
                                      default=UNDEFINED)
    dau_data_reduc_factor           =models.IntegerField()
    led_count_ratemeter             =models.IntegerField()
    hed_count_ratemeter             =models.IntegerField()
    dau_total_rate                  =models.IntegerField()
    led_accept_count_rate_short     =models.IntegerField()
    led_accept_count_rate_long      =models.IntegerField()
    hed_accept_count_rate_short     =models.IntegerField()
    hed_accept_count_rate_long      =models.IntegerField()
    led_calc_background_rate_short  =models.IntegerField()
    led_calc_background_rate_long   =models.IntegerField()
    hed_calc_background_rate_short  =models.IntegerField()
    hed_calc_background_rate_long   =models.IntegerField()
    led_short_win_thresh_1          =models.IntegerField()
    led_short_win_thresh_2          =models.IntegerField()
    led_short_win_thresh_3          =models.IntegerField()
    led_long_win_thresh             =models.IntegerField()
    hed_short_win_thresh_1          =models.IntegerField()
    hed_short_win_thresh_2          =models.IntegerField()
    hed_short_win_thresh_3          =models.IntegerField()
    hed_long_win_thresh             =models.IntegerField()
    dau1_dm_if_1_current_offset     =models.IntegerField()
    dau1_dm_if_2_current_offset     =models.IntegerField()
    dau1_dm_if_3_current_offset     =models.IntegerField()
    dau1_dm_if_4_current_offset     =models.IntegerField()
    dau2_dm_if_1_current_offset     =models.IntegerField()
    dau2_dm_if_2_current_offset     =models.IntegerField()
    dau2_dm_if_3_current_offset     =models.IntegerField()
    dau2_dm_if_4_current_offset     =models.IntegerField()
    dau3_dm_if_1_current_offset     =models.IntegerField()
    dau3_dm_if_2_current_offset     =models.IntegerField()
    dau3_dm_if_3_current_offset     =models.IntegerField()
    dau3_dm_if_4_current_offset     =models.IntegerField()
    dau4_dm_if_1_current_offset     =models.IntegerField()
    dau4_dm_if_2_current_offset     =models.IntegerField()
    dau4_dm_if_3_current_offset     =models.IntegerField()
    dau4_dm_if_4_current_offset     =models.IntegerField()
    dau1_pmt_if_1_current_offset    =models.IntegerField()
    dau1_pmt_if_2_current_offset    =models.IntegerField()
    dau1_pmt_if_3_current_offset    =models.IntegerField()
    dau2_pmt_if_1_current_offset    =models.IntegerField()
    dau2_pmt_if_2_current_offset    =models.IntegerField()
    dau2_pmt_if_3_current_offset    =models.IntegerField()
    dau3_pmt_if_1_current_offset    =models.IntegerField()
    dau3_pmt_if_2_current_offset    =models.IntegerField()
    dau3_pmt_if_3_current_offset    =models.IntegerField()
    dau4_pmt_if_1_current_offset    =models.IntegerField()
    dau4_pmt_if_2_current_offset    =models.IntegerField()
    dau4_pmt_if_3_current_offset    =models.IntegerField()
    led_pulse_height_bin            =ArrayField( models.IntegerField(), size=10,)
    hed_pulse_height_bin            =ArrayField( models.IntegerField(), size=10,)
    led_time_bin_values             =ArrayField( models.IntegerField(), size=31,)
    hed_time_bin_values             =ArrayField( models.IntegerField(), size=31,)
    
    


# Pulse Height Spectrum Observation
class MXGSPulseHeightSpectrumObservation(models.Model)
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
    integration_period              =models.IntegerField()
    CZT4 = 'CZ'
    BGO12 = 'BG'
    DATA_PROVIDED_CHOICES = (
        (CZT4, "4 CZT spectra"),
        (BGO12, "12 BGO spectra"),
    )
    data_provided = models.CharField(max_length=2,
                                      choices=DATA_PROVIDED_CHOICES,
                                      default=CZT4)
    czt_dau_pulse_height_spectra    =models.FileField()
    bgo_dau_pulse_height_spectra    =models.FileField()
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


class MXGSSampledDetectorCounts(models.Model)
    dau_bgo_1_int_tmon_chan1        =models.IntegerField()
    dau_bgo_1_int_tmon_chan2        =models.IntegerField()
    dau_bgo_1_int_tmon_chan3        =models.IntegerField()
    dau_bgo_1_int_tmon_chan4        =models.IntegerField()
    dau_bgo_2_int_tmon_chan1        =models.IntegerField()
    dau_bgo_2_int_tmon_chan2        =models.IntegerField()
    dau_bgo_2_int_tmon_chan3        =models.IntegerField()
    dau_bgo_2_int_tmon_chan4        =models.IntegerField()
    dau_bgo_3_int_tmon_chan1        =models.IntegerField()
    dau_bgo_3_int_tmon_chan2        =models.IntegerField()
    dau_bgo_3_int_tmon_chan3        =models.IntegerField()
    dau_bgo_3_int_tmon_chan4        =models.IntegerField()
    dau_bgo_4_int_tmon_chan1        =models.IntegerField()
    dau_bgo_4_int_tmon_chan2        =models.IntegerField()
    dau_bgo_4_int_tmon_chan3        =models.IntegerField()
    dau_bgo_4_int_tmon_chan4        =models.IntegerField()

class MXGSSampledDetectorCounts1Second(models.Model)
    mxgs_sampled_detector_counts = models.ForeignKey(MXGSSampledDetectorCounts, on_delete=models.CASCADE)
    utc_year                        =models.IntegerField('UTC year')
    utc_msec                        =models.IntegerField('UTC msec')
    utc_seconds                     =models.IntegerField('UTC seconds')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    dpu_count_prereset              =models.IntegerField()
    dpu_count_Sample_Ratio          =models.IntegerField()
    grey_mode_data_reduc_factor     =models.IntegerField()
    detector_counts                 =models.IntegerField()
    detector_events                 =models.FileField()

class MXGSAuroralCaptureObservation(models.Model)
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


class MXGSMonitoredHousekeepingTM
    utc_year_hk_gen                 =models.IntegerField()
    utc_msec_hk_gen                 =models.IntegerField()
    utc_seconds_hk_gen              =models.IntegerField()
    alive_counter                   =models.IntegerField()
    boot_complete                   =models.IntegerField()
    boot_status_completed_with_errors = models.BooleanField()
    boot_status_completed_no_errors = models.BooleanField()
    boot_status_asw_load_ok         = models.BooleanField()
    boot_status_system_memory_test_ok = models.BooleanField()
    UNDEFINED = 'UD'
    CONFMODE  = 'CF'
    OPMODE   = 'OP'
    SW_MODE_CHOICES = (
        (UNDEFINED , "Undefined"            ),
        (CONFMODE  , "Configuration mode"   ),
        (OPMODE    , "Operational mode"     ),
    )
    sw_mode = models.CharField(max_length=2,
                                      choices=SW_MODE_CHOICES,
                                      default=UNDEFINED)
    UNDEFINED                       = 'UD'
    TGFSEARCH                       = 'TG'
    HIGHBACKGROUND                  = 'HB'
    AURORALCAPTURE                  = 'AC'
    SW_SUBMODE_CHOICES = (
        (UNDEFINED     , "Undefined"        ),
        (TGFSEARCH     , "TGF Search mode"  ),
        (HIGHBACKGROUND, "High Background"  ),
        (AURORALCAPTURE, "Auroral capture"  ),
    )
    sw_submode                      = models.CharField(max_length=2,
                                      choices=SW_SUBMODE_CHOICES,
                                      default=UNDEFINED)
    err_war_invalid_startcycle      = models.BooleanField()  # No valid or more than one valid Start Cycle Request TC packet is received by MMIA before the next TCP.
    err_war_nonscience_tm_discarded = models.BooleanField()  # Non-science downlink buffer is full
    err_war_comm_protocol           = models.BooleanField()  # Communication protocol error detected, will attempt to resynchonize protocol.
    err_war_invalid_EDLF_frame      = models.BooleanField() # Invalid EDLF frame received.
    err_war_task_deadline_missed    = models.BooleanField() # Task deadline missed or task queue full.
    err_war_software_exception      = models.BooleanField() # Software exception occured in Boot Software.
    err_war_nvm_powered_on          = models.BooleanField()
    psu_cont_tmon_chan1             = models.IntegerField()
    psu_cont_tmon_chan2             = models.IntegerField()
    dpu_int_tmon_1_fpga             = models.IntegerField()
    dpu_int_tmon_2_dcdc             = models.IntegerField()
    discarded_normal_packets        = models.IntegerField()
    ram_lhp_evap_tmon2              = models.IntegerField()
    wake_lhp_evap_tmon3             = models.IntegerField()
    led_count_ratemeter             = models.IntegerField()
    hed_count_ratemeter             = models.IntegerField()
    discarded_nonscience_packets    = models.IntegerField()
    recd_packets_count              = models.IntegerField()
    psu_cont_tmon_chan1_add         = models.IntegerField()
    psu_cont_tmon_chan2_add         = models.IntegerField()
    dpu_int_tmon_1_fpga_add         = models.IntegerField()
    dpu_int_tmon_2_dcdc_add         = models.IntegerField()
    psu_tmon_dau_czt_1_dcdc         = models.IntegerField()
    psu_tmon_dau_czt_2_dcdc         = models.IntegerField()
    psu_tmon_dau_czt_3_dcdc         = models.IntegerField()
    psu_tmon_dau_czt_4_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_1_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_2_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_3_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_4_dcdc         = models.IntegerField()
    dau_czt_1_tmon_chan2            = models.IntegerField()
    dau_czt_2_tmon_chan2            = models.IntegerField()
    dau_czt_3_tmon_chan2            = models.IntegerField()
    dau_czt_4_tmon_chan2            = models.IntegerField()
    dau_bgo_1_tmon_chan2            = models.IntegerField()
    dau_bgo_2_tmon_chan2            = models.IntegerField()
    dau_bgo_3_tmon_chan2            = models.IntegerField()
    dau_bgo_4_tmon_chan2            = models.IntegerField()

    

class MXGSInstrumentHousekeepingTM
    pass

class MXGSInstrumentSummaryHousekeepingTM
    pass
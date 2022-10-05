---
title: list hsc api find in vscode
created: 2022-Jun-08
tags:
  - 'permanent/fact'
---

```
C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_anlt.h
hsc_chn_an_status_get
hsc_chn_lt_status_get
hsc_chn_an_fsm_state_get
hsc_chn_lt_fsm_state_get
hsc_chn_an_result_get
hsc_chn_anlt_timestamp_query
hsc_chn_anlt_timestamp_print
hsc_chn_anlt_timestamp_show

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_bundle.h
  51,13: hsc_status_t hsc_bundle_init(hsc_bundle_t *bundle, hsc_bundle_rules_t *rules);
  61,13: hsc_status_t hsc_bundle_start(hsc_bundle_t *bundle, hsc_bundle_rules_t *rules);
  71,5: bool hsc_bundle_link_ready_wait(hsc_bundle_t *bundle, uint32_t timeout_us);
  81,5: bool hsc_bundle_is_link_ready(hsc_bundle_t *bundle, e_hsc_intf intf);
  96,13: hsc_status_t hsc_bundle_rules_query(hsc_bundle_t *bundle,
  112,13: hsc_status_t hsc_bundle_status_query(hsc_bundle_t *bundle, e_hsc_intf intf,
  130,13: hsc_status_t hsc_bundle_anlt_log_query(hsc_bundle_t *bundle, e_hsc_intf intf, char *buff, uint32_t buff_size);
  144,13: hsc_status_t hsc_bundle_rules_print(hsc_bundle_t *bundle, hsc_bundle_rules_t* rules);
  158,13: hsc_status_t hsc_bundle_status_print(hsc_bundle_t *bundle, hsc_bundle_rules_t* rules);
  173,13: hsc_status_t hsc_bundle_rules_show(hsc_bundle_t *bundle);
  186,13: hsc_status_t hsc_bundle_status_show(hsc_bundle_t *bundle);
  200,13: hsc_status_t hsc_bundle_link_status_show(hsc_bundle_t *bundle, e_hsc_intf intf);
  210,9: uint32_t hsc_bundle_id_get(hsc_bundle_t *bundle);
  219,11: hsc_dev_t* hsc_bundle_dev_get(hsc_bundle_t *bundle);
  243,13: hsc_status_t hsc_bundle_loopback_set(hsc_bundle_t *bundle, e_hsc_intf intf,
  254,20: e_hsc_loopback_mode hsc_bundle_loopback_get(hsc_bundle_t *bundle, e_hsc_intf intf);
  265,13: hsc_status_t hsc_bundle_anlt_restart(hsc_bundle_t *bundle, e_hsc_intf intf);

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_chn_dsp.h
  134,13: hsc_status_t hsc_chn_dsp_snr_mon_enable(hsc_chn_t *chn, bool enable);
  144,5: bool hsc_chn_dsp_snr_mon_is_enabled(hsc_chn_t *chn);
  171,13: hsc_status_t hsc_chn_dsp_snr_mon_set(hsc_chn_t *chn,
  192,13: hsc_status_t hsc_chn_dsp_snr_mon_get(hsc_chn_t *chn,
  203,7: double hsc_chn_dsp_snr_mon_value_get(hsc_chn_t *chn, e_hsc_snr_value_fmt fmt);
  214,13: hsc_status_t hsc_chn_dsp_ltp_get(hsc_chn_t *chn, e_hsc_value_fmt fmt, double *ltp);
  229,9: uint32_t hsc_chn_dsp_hist_size_get(hsc_chn_t *chn);
  242,13: hsc_status_t hsc_chn_dsp_hist_get(hsc_chn_t *chn, e_hsc_rx_error_gen err_inj_gen,
  259,13: hsc_status_t hsc_chn_dsp_hist_ascii_plot(hsc_chn_t *chn,
  276,13: hsc_status_t hsc_chn_dsp_hist_show(hsc_chn_t *chn,
  308,13: hsc_status_t hsc_chn_dsp_eyemon_query(hsc_chn_t *chn,
  326,13: hsc_status_t hsc_chn_dsp_ffe_taps_query(hsc_chn_t *chn, uint16_t ffe_sub_chn,
  364,15:  *   status |= hsc_chn_dsp_eyemon_to_file_dump(chn,         // The physical channel being accessed
  374,13: hsc_status_t hsc_chn_dsp_eyemon_to_file_dump(hsc_chn_t *chn,
  392,9: uint32_t hsc_chn_dsp_ffe_taps_num_get(hsc_chn_t *chn);
  409,13: hsc_status_t hsc_chn_dsp_ffe_taps_show(hsc_chn_t *chn, uint16_t ffe_sub_chn);
  422,13: hsc_status_t hsc_chn_dsp_dfe_coeffs_get(hsc_chn_t *chn, uint32_t sub_chn,
  433,13: hsc_status_t hsc_chn_dsp_mode_set(hsc_chn_t *chn, e_hsc_dsp_mode dsp_mode);
  443,15: e_hsc_dsp_mode hsc_chn_dsp_mode_get(hsc_chn_t *chn);

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_chn.h
hsc_chn_init
hsc_chn_fw_is_locked
hsc_chn_pll_is_locked
hsc_chn_dsp_is_ready
hsc_chn_signal_is_detected
hsc_chn_los_get
hsc_chn_lol_get
hsc_chn_latched_los_get
hsc_chn_latched_lol_get
hsc_chn_is_ready
hsc_chn_ready_wait
hsc_chn_reset_count_get
hsc_chn_intf_get
hsc_chn_id_get
hsc_chn_hw_id_get
hsc_chn_die_get
 hsc_chn_dev_get
hsc_chn_power_down
hsc_chn_is_power_down
hsc_chn_loopback_set
hsc_chn_loopback_get
hsc_chn_polarity_set
hsc_chn_polarity_get
hsc_chn_polarity_toggle
hsc_chn_demap_value_get
hsc_chn_squelch
hsc_chn_is_squelched
hsc_chn_squelch_lock
hsc_chn_is_squelch_locked
hsc_chn_auto_squelch_enable
hsc_chn_auto_squelch_is_enabled
hsc_chn_los_force
hsc_chn_autoctle_enable
hsc_chn_autoctle_is_enabled
hsc_chn_fir_taps_set
hsc_chn_fir_taps_get
hsc_chn_swing_set
hsc_chn_swing_get
hsc_chn_afe_trim_set
hsc_chn_afe_trim_get
hsc_chn_ctle_code_set
hsc_chn_ctle_code_get
hsc_chn_rx_qc_rules_apply
hsc_chn_rx_qc_rules_query
hsc_chn_rx_qc_stats_query
hsc_chn_rx_los_rules_query
hsc_chn_rx_qc_rules_print
hsc_chn_rx_qc_stats_print
hsc_chn_fll_enable
hsc_chn_fll_is_enabled
hsc_chn_status_show
hsc_chn_rx_los_rules_apply
hsc_chn_reg_read
hsc_chn_reg_write
hsc_chn_reg_rmw

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_dbg.h
hsc_dev_i2c_access_enable
hsc_dev_i2c_access_is_enabled
hsc_chn_pmd_state_get
hsc_mcu_self_init_enable
hsc_mcu_self_init_is_enabled
hsc_mcu_tap_set
hsc_mcu_tap_get
hsc_bundle_anlt_ic_coef_set
hsc_bundle_anlt_ic_coef_set
hsc_bundle_anlt_ic_coef_query
hsc_bundle_anlt_ic_coef_query
hsc_bundle_anlt_coef_clause_query
hsc_anlt_an_status_translate
hsc_anlt_an_hcd_translate
hsc_anlt_an_mode_translate
hsc_dev_dsp_mse_to_snr
hsc_dev_dsp_mse_to_snr_mdb
hsc_dev_dsp_snr_to_mse
hsc_dev_ldo_out_set
hsc_dev_ldo_out_get
hsc_dev_ldo_qpump_set
hsc_dev_ldo_qpump_get

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_dev.h

hsc_dev
hsc_dev_with_ips
hsc_dev_init
hsc_dev_soft_reset
hsc_dev_fw_is_running
hsc_dev_api_version
hsc_dev_fw_version
hsc_dev_asic_id
hsc_dev_num_chns
hsc_dev_num_bundles
hsc_dev_num_mcus
hsc_dev_num_dies
hsc_dev_num_gpio_pins
hsc_dev_num_eeproms
hsc_dev_has_fec
hsc_dev_has_hmux
hsc_dev_has_anlt
hsc_dev_has_xbar
hsc_dev_xbar_enable
hsc_dev_xbar_is_enabled
hsc_dev_gpio
hsc_dev_mcu
hsc_dev_eeprom
hsc_dev_bundle_rules
hsc_dev_bundle
hsc_dev_bundle_hmux
hsc_dev_xbar
hsc_dev_prbs
hsc_dev_prbs_gen_rules
hsc_dev_prbs_chk_rules
hsc_dev_prbs_err_inj_rules
hsc_dev_mcu_dnld
hsc_dev_eeprom_dnld
hsc_dev_chn
hsc_dev_rx_rules
hsc_dev_tx_rules
hsc_dev_rx_qc_rules
hsc_dev_rx_los_rules
hsc_dev_xbar_rules
hsc_dev_pwr_set
hsc_dev_pwr_get
hsc_dev_pwr_show
hsc_reg_get
hsc_reg_set
hsc_dev_reg_write
hsc_dev_reg_read
hsc_dev_reg_rmw
hsc_dev_delegate_set
hsc_dev_lock
hsc_dev_unlock
hsc_dev_temperature_query
hsc_dev_bias_is_ready
hsc_dev_eru_is_ready
hsc_dev_swizzle_enable
hsc_dev_swizzle_is_enabled
hsc_dev_pkg_type_get
hsc_dev_pkg_type_set
hsc_dev_spi_release
hsc_dev_pkg_show

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_dnld.h
hsc_dnld_download
hsc_dnld_download_from_file
hsc_dnld_download_with_handler
hsc_dnld_timeout_set
hsc_dnld_timeout_get
hsc_dnld_verify_enable
hsc_dnld_verify_is_enabled
hsc_dnld_two_stages_enable
hsc_dnld_two_stages_is_enabled
hsc_dnld_download_from_shared_eeprom
(*

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_eeprom.h
hsc_eeprom_verify
hsc_eeprom_calc_cks
hsc_eeprom_exp_cks
hsc_eeprom_metadata_get
hsc_eeprom_write
hsc_eeprom_read
hsc_eeprom_erase
hsc_eeprom_instruction_size_get
hsc_eeprom_data_size_get
hsc_eeprom_cks_is_good
hsc_eeprom_id_get
hsc_eeprom_dev_get

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_fec.h
hsc_chn_fec_stats_query
hsc_chn_fec_stats_show

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_gpio.h
hsc_gpio_enable
hsc_gpio_is_enabled
hsc_gpio_val_set
hsc_gpio_val_get
hsc_gpio_func_set
hsc_gpio_func_get
hsc_gpio_dir_set
hsc_gpio_dir_get
hsc_gpio_trigger
hsc_gpio_init
hsc_gpio_show
hsc_gpio_intr_enable
hsc_gpio_intr_is_enabled
hsc_gpio_intr_get
hsc_gpio_dev_get

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_hmux.h
hsc_hmux_position_set
hsc_hmux_position_get
hsc_hmux_rules_apply
hsc_hmux_rules_query
hsc_hmux_rules_show
hsc_hmux_pattern_set
hsc_hmux_pattern_get
 hsc_hmux_dev_get

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_mcu.h
hsc_mcu_fw_is_running
hsc_mcu_reset
hsc_mcu_fw_version
hsc_mcu_fw_mode_get
hsc_mcu_status_query
hsc_mcu_pc_log_query
hsc_mcu_log_query
hsc_mcu_stall
hsc_mcu_is_stalled
hsc_mcu_id_get
hsc_mcu_dev_get
hsc_mcu_pc_log_show
hsc_mcu_log_show
hsc_mcu_debug_log_filter_get
hsc_mcu_debug_log_filter_set
hsc_mcu_pif_write
hsc_mcu_pif_read

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_prbs.h
  42,13: hsc_status_t hsc_prbs_gen_rules_apply(hsc_prbs_t *prbs,
  58,13: hsc_status_t hsc_prbs_gen_rules_query(hsc_prbs_t *prbs,
  73,13: hsc_status_t hsc_prbs_chk_rules_query(hsc_prbs_t *prbs,
  88,13: hsc_status_t hsc_prbs_err_inj_rules_query(hsc_prbs_t *prbs,
  101,13: hsc_status_t hsc_prbs_chk_status_query(hsc_prbs_t *prbs,
  116,13: hsc_status_t hsc_prbs_gen_rules_show(hsc_prbs_t *prbs);
  127,13: hsc_status_t hsc_prbs_chk_rules_apply(hsc_prbs_t *prbs,
  142,13: hsc_status_t hsc_prbs_chk_rules_show(hsc_prbs_t *prbs);
  157,13: hsc_status_t hsc_prbs_chk_status_show(hsc_prbs_t *prbs);
  168,13: hsc_status_t hsc_prbs_err_inj_rules_apply(hsc_prbs_t *prbs,
  183,13: hsc_status_t hsc_prbs_err_inj_rules_show(hsc_prbs_t *prbs);
  194,13: hsc_status_t hsc_prbs_gen_enable(hsc_prbs_t *prbs, bool enable);
  204,13: hsc_status_t hsc_prbs_chk_enable(hsc_prbs_t *prbs, bool enable);

C:\Users\dutran\projects\hsc\lynx\api\inc\hsc_xbar.h
  37,13: hsc_status_t hsc_xbar_rules_apply(hsc_xbar_t *xbar, hsc_xbar_rules_t *rules);
  52,13: hsc_status_t hsc_xbar_rules_query(hsc_xbar_t *xbar, hsc_xbar_rules_t *rules);
  66,13: hsc_status_t hsc_xbar_rules_print(hsc_xbar_t *xbar, hsc_xbar_rules_t *rules);
  82,13: hsc_status_t hsc_xbar_rules_show(hsc_xbar_t *xbar);
  92,11: hsc_dev_t* hsc_xbar_dev_get(hsc_xbar_t *xbar);

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_an_rules.h
hsc_an_rules_enable
hsc_an_rules_mode_set
hsc_an_rules_supported_abilities_get
hsc_an_rules_cap_ad_set
hsc_an_rules_cap_ad_get
hsc_an_rules_hmux_restart_enable
hsc_an_rules_is_enabled
hsc_an_rules_mode_get
hsc_an_rules_hmux_restart_is_enabled
hsc_an_rules_link_time_budget_set
hsc_an_rules_link_time_budget_get
hsc_an_rules_pan_set
hsc_an_rules_pan_get
hsc_an_rules_pause_ability_set
hsc_an_rules_pause_ability_get
hsc_an_rules_remote_fault_enable
hsc_an_rules_remote_fault_is_enabled
hsc_an_rules_retry_threshold_set
hsc_an_rules_retry_threshold_get
hsc_an_rules_nonce_check_enable
hsc_an_rules_nonce_check_is_enabled

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_bundle_rules.h
hsc_bundle_rules_operation_mode_get
hsc_bundle_rules_baud_rate_set
hsc_bundle_rules_baud_rate_get
hsc_bundle_rules_chns_mask_set
hsc_bundle_rules_chns_mask_get
hsc_bundle_rules_ref_clk_set
hsc_bundle_rules_ref_clk_get
hsc_bundle_rules_ieee_demap_enable
hsc_bundle_rules_ieee_demap_is_enabled
hsc_bundle_rules_signalling_set
hsc_bundle_rules_signalling_get
hsc_bundle_rules_link_leader_set
hsc_bundle_rules_link_leader_get
hsc_bundle_rules_link_folwr_by_idx_set
hsc_bundle_rules_link_folwr_by_idx_get
hsc_bundle_rules_link_folwrs_set
hsc_bundle_rules_link_folwrs_get
hsc_bundle_rules_anlt_prbs_enable
hsc_bundle_rules_anlt_prbs_is_enabled
hsc_bundle_rules_num_chns_get
hsc_xbar_rules
hsc_hmux_rules
hsc_an_rules
hsc_lt_rules
hsc_fec_rules
hsc_chn_rx_rules
hsc_chn_tx_rules
hsc_bundle_rules_dev_get

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_fec_rules.h
hsc_fec_rules_mode_set
hsc_fec_rules_type_set
hsc_fec_rules_mode_get
hsc_fec_rules_type_get

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_hmux_rules.h
hsc_hmux_rules_default_position_set
hsc_hmux_rules_default_position_get
hsc_hmux_rules_mode_set
hsc_hmux_rules_mode_get
hsc_hmux_rules_broadcast_enable
hsc_hmux_rules_broadcast_is_enabled
hsc_hmux_rules_pattern_set
hsc_hmux_rules_pattern_get
hsc_hmux_rules_lf_timer_set
hsc_hmux_rules_lf_timer_get

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_lt_rules.h
  108,13: hsc_status_t hsc_lt_rules_enable(hsc_lt_rules_t *rules, bool en);
  119,13: hsc_status_t hsc_lt_rules_clock_source_set(hsc_lt_rules_t *rules,
  131,13: hsc_status_t hsc_lt_rules_extended_link_time_set(hsc_lt_rules_t *rules,
  143,13: hsc_status_t hsc_lt_rules_ctle_tune_enable(hsc_lt_rules_t *rules, bool en);
  154,13: hsc_status_t hsc_lt_rules_target_snr_set(hsc_lt_rules_t *rules, uint16_t target_snr);
  165,13: hsc_status_t hsc_lt_rules_algorithm_set(hsc_lt_rules_t *rules,
  177,13: hsc_status_t hsc_lt_rules_algorithm_cycle_set(hsc_lt_rules_t *rules,
  188,5: bool hsc_lt_rules_is_enabled(hsc_lt_rules_t *rules);
  199,14: e_hsc_clk_src hsc_lt_rules_clock_source_get(hsc_lt_rules_t *rules);
  209,5: bool hsc_lt_rules_ctle_tune_is_enabled(hsc_lt_rules_t *rules);
  219,9: uint16_t hsc_lt_rules_target_snr_get(hsc_lt_rules_t *rules);
  229,9: uint16_t hsc_lt_rules_extended_link_time_get(hsc_lt_rules_t *rules);
  239,9: uint32_t hsc_lt_rules_algorithm_get(hsc_lt_rules_t *rules);
  249,9: uint16_t hsc_lt_rules_algorithm_cycle_get(hsc_lt_rules_t *rules);
  260,13: hsc_status_t hsc_lt_rules_auto_invert_enable(hsc_lt_rules_t *rules, bool enable);
  271,13: hsc_status_t hsc_lt_rules_coef_preset_set(hsc_lt_rules_t *rules, e_hsc_lt_coef_preset preset);
  282,13: hsc_status_t hsc_lt_rules_fir_walk_enable(hsc_lt_rules_t *rules, bool enable);
  293,13: hsc_status_t hsc_lt_rules_honor_link_time_enable(hsc_lt_rules_t *rules, bool enable);
  304,13: hsc_status_t hsc_lt_rules_rx_precode_threshold_set(hsc_lt_rules_t *rules, uint8_t threshold);
  314,5: bool hsc_lt_rules_auto_invert_is_enabled(hsc_lt_rules_t *rules);
  324,21: e_hsc_lt_coef_preset hsc_lt_rules_coef_preset_get(hsc_lt_rules_t *rules);
  334,5: bool hsc_lt_rules_fir_walk_is_enabled(hsc_lt_rules_t *rules);
  344,5: bool hsc_lt_rules_honor_link_time_is_enabled(hsc_lt_rules_t *rules);
  354,8: uint8_t hsc_lt_rules_rx_precode_threshold_get(hsc_lt_rules_t *rules);
  364,13: hsc_status_t hsc_lt_rules_retry_threshold_set(hsc_lt_rules_t *rules, uint16_t threshold);
  373,9: uint16_t hsc_lt_rules_retry_threshold_get(hsc_lt_rules_t *rules);

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_prbs_rules.h
  210,13: hsc_status_t hsc_prbs_rules_pattern_set(hsc_prbs_rules_t * rules,
  221,15: e_hsc_prbs_pat hsc_prbs_rules_pattern_get(hsc_prbs_rules_t * rules);
  232,13: hsc_status_t hsc_prbs_rules_pattern_lsb_set(hsc_prbs_rules_t * rules,
  243,15: e_hsc_prbs_pat hsc_prbs_rules_pattern_lsb_get(hsc_prbs_rules_t * rules);
  255,13: hsc_status_t hsc_prbs_rules_pattern_value_set(hsc_prbs_rules_t * rules,
  268,13: hsc_status_t hsc_prbs_rules_pattern_value_get(hsc_prbs_rules_t * rules,
  281,13: hsc_status_t hsc_prbs_rules_pattern_value_lsb_set(
  294,13: hsc_status_t hsc_prbs_rules_pattern_value_lsb_get(
  308,13: hsc_status_t hsc_prbs_rules_pattern_gen_repeat_set(hsc_prbs_rules_t * rules,
  320,9: uint32_t hsc_prbs_rules_pattern_gen_repeat_get(hsc_prbs_rules_t * rules);
  331,13: hsc_status_t hsc_prbs_rules_pattern_gen_repeat_lsb_set(
  343,9: uint32_t hsc_prbs_rules_pattern_gen_repeat_lsb_get(
  354,13: hsc_status_t hsc_prbs_rules_mode_set(hsc_prbs_rules_t * rules,
  364,16: e_hsc_prbs_mode hsc_prbs_rules_mode_get(hsc_prbs_rules_t * rules);
  374,13: hsc_status_t hsc_prbs_rules_pattern_mode_set(hsc_prbs_rules_t * rules,
  384,20: e_hsc_prbs_pat_mode hsc_prbs_rules_pattern_mode_get(
  394,13: hsc_status_t hsc_prbs_rules_chk_autolock_enable(hsc_prbs_rules_t *rules, bool en);
  403,5: bool hsc_prbs_rules_chk_autolock_is_enabled(hsc_prbs_rules_t *rules);
  413,13: hsc_status_t hsc_prbs_rules_enable(hsc_prbs_rules_t * rules, bool en);
  422,5: bool hsc_prbs_rules_is_enabled(hsc_prbs_rules_t * rules);
  432,13: hsc_status_t hsc_prbs_rules_lsb_enable(hsc_prbs_rules_t * rules,
  442,5: bool hsc_prbs_rules_lsb_is_enabled(hsc_prbs_rules_t * rules);
  452,13: hsc_status_t hsc_prbs_rules_invert_enable(hsc_prbs_rules_t * rules,
  462,5: bool hsc_prbs_rules_invert_is_enabled(hsc_prbs_rules_t * rules);
  472,13: hsc_status_t hsc_prbs_rules_invert_lsb_enable(hsc_prbs_rules_t * rules,
  482,5: bool hsc_prbs_rules_invert_lsb_is_enabled(hsc_prbs_rules_t * rules);
  494,13: hsc_status_t hsc_prbs_gen_rules_pattern_mode_set(hsc_prbs_gen_rules_t * rules,
  504,20: e_hsc_prbs_pat_mode hsc_prbs_gen_rules_pattern_mode_get(
  515,13: hsc_status_t hsc_prbs_gen_rules_pattern_set(hsc_prbs_gen_rules_t * rules,
  526,15: e_hsc_prbs_pat hsc_prbs_gen_rules_pattern_get(hsc_prbs_gen_rules_t * rules);
  538,13: hsc_status_t hsc_prbs_gen_rules_pattern_lsb_set(hsc_prbs_gen_rules_t * rules,
  550,15: e_hsc_prbs_pat hsc_prbs_gen_rules_pattern_lsb_get(hsc_prbs_gen_rules_t * rules);
  563,13: hsc_status_t hsc_prbs_gen_rules_pattern_value_set(hsc_prbs_gen_rules_t * rules,
  576,13: hsc_status_t hsc_prbs_gen_rules_pattern_value_get(hsc_prbs_gen_rules_t * rules,
  589,13: hsc_status_t hsc_prbs_gen_rules_pattern_repeat_set(hsc_prbs_gen_rules_t * rules,
  601,9: uint32_t hsc_prbs_gen_rules_pattern_repeat_get(hsc_prbs_gen_rules_t * rules);
  613,13: hsc_status_t hsc_prbs_gen_rules_pattern_value_lsb_set(
  626,13: hsc_status_t hsc_prbs_gen_rules_pattern_value_lsb_get(
  639,13: hsc_status_t hsc_prbs_gen_rules_pattern_repeat_lsb_set(
  651,9: uint32_t hsc_prbs_gen_rules_pattern_repeat_lsb_get(
  663,13: hsc_status_t hsc_prbs_gen_rules_mode_set(hsc_prbs_gen_rules_t * rules,
  673,16: e_hsc_prbs_mode hsc_prbs_gen_rules_mode_get(hsc_prbs_gen_rules_t * rules);
  683,13: hsc_status_t hsc_prbs_gen_rules_enable(hsc_prbs_gen_rules_t * rules, bool en);
  692,5: bool hsc_prbs_gen_rules_is_enabled(hsc_prbs_gen_rules_t * rules);
  702,13: hsc_status_t hsc_prbs_gen_rules_lsb_enable(hsc_prbs_gen_rules_t * rules,
  712,5: bool hsc_prbs_gen_rules_lsb_is_enabled(hsc_prbs_gen_rules_t * rules);
  722,13: hsc_status_t hsc_prbs_gen_rules_invert_enable(hsc_prbs_gen_rules_t * rules,
  732,5: bool hsc_prbs_gen_rules_invert_is_enabled(hsc_prbs_gen_rules_t * rules);
  743,13: hsc_status_t hsc_prbs_chk_rules_pattern_set(hsc_prbs_chk_rules_t * rules,
  754,15: e_hsc_prbs_pat hsc_prbs_chk_rules_pattern_get(hsc_prbs_chk_rules_t * rules);
  765,13: hsc_status_t hsc_prbs_chk_rules_pattern_lsb_set(hsc_prbs_chk_rules_t * rules,
  776,15: e_hsc_prbs_pat hsc_prbs_chk_rules_pattern_lsb_get(hsc_prbs_chk_rules_t * rules);
  788,13: hsc_status_t hsc_prbs_chk_rules_pattern_value_set(hsc_prbs_chk_rules_t * rules,
  801,13: hsc_status_t hsc_prbs_chk_rules_pattern_value_get(hsc_prbs_chk_rules_t * rules,
  814,13: hsc_status_t hsc_prbs_chk_rules_pattern_value_lsb_set(
  827,13: hsc_status_t hsc_prbs_chk_rules_pattern_value_lsb_get(
  839,13: hsc_status_t hsc_prbs_chk_rules_mode_set(hsc_prbs_chk_rules_t * rules,
  849,16: e_hsc_prbs_mode hsc_prbs_chk_rules_mode_get(hsc_prbs_chk_rules_t * rules);
  859,13: hsc_status_t hsc_prbs_chk_rules_pattern_mode_set(hsc_prbs_chk_rules_t * rules,
  869,20: e_hsc_prbs_pat_mode hsc_prbs_chk_rules_pattern_mode_get(
  879,13: hsc_status_t hsc_prbs_chk_rules_autolock_enable(hsc_prbs_chk_rules_t *rules, bool en);
  888,5: bool hsc_prbs_chk_rules_autolock_is_enabled(hsc_prbs_chk_rules_t *rules);
  898,13: hsc_status_t hsc_prbs_chk_rules_enable(hsc_prbs_chk_rules_t * rules, bool en);
  907,5: bool hsc_prbs_chk_rules_is_enabled(hsc_prbs_chk_rules_t * rules);
  917,13: hsc_status_t hsc_prbs_chk_rules_lsb_enable(hsc_prbs_chk_rules_t * rules,
  927,5: bool hsc_prbs_chk_rules_lsb_is_enabled(hsc_prbs_chk_rules_t * rules);
  937,13: hsc_status_t hsc_prbs_chk_rules_invert_enable(hsc_prbs_chk_rules_t * rules,
  947,5: bool hsc_prbs_chk_rules_invert_is_enabled(hsc_prbs_chk_rules_t * rules);
  957,13: hsc_status_t hsc_prbs_chk_rules_invert_lsb_enable(hsc_prbs_chk_rules_t * rules,
  967,5: bool hsc_prbs_chk_rules_invert_lsb_is_enabled(hsc_prbs_chk_rules_t * rules);
  979,13: hsc_status_t hsc_prbs_err_inj_rules_pattern_set(
  991,23: e_hsc_prbs_err_inj_pat hsc_prbs_err_inj_rules_pattern_get(
  1004,13: hsc_status_t hsc_prbs_err_inj_rules_pattern_lsb_set(
  1016,23: e_hsc_prbs_err_inj_pat hsc_prbs_err_inj_rules_pattern_lsb_get(
  1027,13: hsc_status_t hsc_prbs_err_inj_rules_duration_set(
  1037,9: uint32_t hsc_prbs_err_inj_rules_duration_get(hsc_prbs_err_inj_rules_t * rules);
  1047,13: hsc_status_t hsc_prbs_err_inj_rules_gap_set(hsc_prbs_err_inj_rules_t * rules,
  1057,9: uint32_t hsc_prbs_err_inj_rules_gap_get(hsc_prbs_err_inj_rules_t * rules);
  1067,13: hsc_status_t hsc_prbs_err_inj_rules_enable(hsc_prbs_err_inj_rules_t * rules,
  1077,5: bool hsc_prbs_err_inj_rules_is_enabled(hsc_prbs_err_inj_rules_t * rules);

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_rx_los_rules.h
hsc_rx_los_rules_assert_threshold_set
hsc_rx_los_rules_assert_threshold_get
hsc_rx_los_rules_deassert_threshold_set
hsc_rx_los_rules_deassert_threshold_get

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_rx_qc_rules.h
hsc_rx_qc_rules_enable
hsc_rx_qc_rules_is_enabled
hsc_rx_qc_rules_data_mode_enable
hsc_rx_qc_rules_data_mode_is_enabled
hsc_rx_qc_rules_hist_enable
hsc_rx_qc_rules_hist_is_enabled
hsc_rx_qc_rules_up_threshold_set
hsc_rx_qc_rules_up_threshold_get
hsc_rx_qc_rules_up_sample_threshold_set
hsc_rx_qc_rules_up_sample_threshold_get
hsc_rx_qc_rules_down_threshold_set
hsc_rx_qc_rules_down_threshold_get
hsc_rx_qc_rules_down_sample_threshold_set
hsc_rx_qc_rules_down_sample_threshold_get
hsc_diags_rx_qc_rules_pause_enable
hsc_diags_rx_qc_rules_is_paused

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_rx_rules.h
hsc_rx_rules_baud_rate_set
hsc_rx_rules_baud_rate_get
hsc_rx_rules_signalling_set
hsc_rx_rules_signalling_get
hsc_rx_rules_ieee_demap_enable
hsc_rx_rules_ieee_demap_is_enabled
hsc_rx_rules_dsp_mode_set
hsc_rx_rules_dsp_mode_get
hsc_rx_rules_autoctle_enable
hsc_rx_rules_autoctle_is_enabled
hsc_rx_rules_polarity_set
hsc_rx_rules_polarity_get
hsc_rx_rules_gray_mapping_enable
hsc_rx_rules_gray_mapping_is_enabled
hsc_rx_rules_vga_tracking_enable
hsc_rx_rules_vga_tracking_is_enabled
hsc_rx_rules_dfe_precoder_enable
hsc_rx_rules_dfe_precoder_is_enabled
hsc_rx_rules_ctle_code_set
hsc_rx_rules_ctle_code_get
hsc_rx_rules_num_ctle_stages_get
hsc_rx_rules_advanced_set
hsc_rx_rules_advanced_get
hsc_rx_rules_scdr_enable
hsc_rx_rules_scdr_is_enabled

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_tx_rules.h
hsc_tx_rules_baud_rate_set
hsc_tx_rules_baud_rate_get
hsc_tx_rules_signalling_set
hsc_tx_rules_signalling_get
hsc_tx_rules_ieee_demap_enable
hsc_tx_rules_ieee_demap_is_enabled
hsc_tx_rules_polarity_set
hsc_tx_rules_polarity_get
hsc_tx_rules_gray_mapping_enable
hsc_tx_rules_gray_mapping_is_enabled
hsc_tx_rules_dfe_precoder_enable
hsc_tx_rules_dfe_precoder_is_enabled
hsc_tx_rules_swing_set
hsc_tx_rules_swing_get
hsc_tx_rules_fir_taps_set
hsc_tx_rules_fir_taps_get
hsc_tx_rules_eye_set
hsc_tx_rules_eye_get
hsc_tx_rules_squelch_lock
hsc_tx_rules_squelch_is_locked
hsc_tx_rules_src_set
hsc_tx_rules_src_get
hsc_tx_rules_fll_enable
hsc_tx_rules_fll_is_enabled

C:\Users\dutran\projects\hsc\lynx\api\inc\rules\hsc_xbar_rules.h
hsc_xbar_rules_chn_connect
hsc_xbar_rules_chn_src_get
hsc_xbar_rules_chn_dst_get
```




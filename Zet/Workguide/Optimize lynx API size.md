---
title: Optimize lynx API size
created: 2022-Oct-17
tags:
  - 'tasks/todo'
project: TBD
date:
  - start: 2022-10-17
  - end: 'TBD'
  - due: 'TBD'
publish: False
---
up:: [[Tasks list]]
https://stackoverflow.com/questions/662439/what-are-some-refactoring-methods-to-reduce-size-of-compiled-code

```
Hiện tại thấy đang compile ra 190K
Dz, hiện tại customer đang có nhu cầu optimize Lynx API xuống 64K
VD anlt có thể dim
gearbox có thể dim
```

```shell
export HSC_DIR=~/projects/hsc/
cd ${HSC_DIR}/lynx/api
${HSC_DIR}/../bin/legacy/gen_file_size_report.pl
```


## [[2022-10-19]]

```shell
make code_size
nm --format=bsd --size-sort --print-size --radix=d build-output/code_size/example.exe > size.csv
```

```log
0000004299182962 0000000000000001 T cpl_pll_rules_dump
0000004299182587 0000000000000001 T cpl_rx_dsp_snr_mon_cfg
0000004299182583 0000000000000001 T cpl_rx_dsp_snr_mon_en
0000004299182964 0000000000000001 T cpl_rx_rules_dump
0000004299182963 0000000000000001 T cpl_tx_rules_dump
0000004299193779 0000000000000002 T cpl_rx_ready_get
0000004299193769 0000000000000002 T cpl_tx_ready_get
0000004299196138 0000000000000002 T cpl_wait_for_pll_lock
0000004299182969 0000000000000003 T cpl_dbg_status_dump
0000004299182584 0000000000000003 T cpl_rx_dsp_snr_mon_enabled
0000004299183217 0000000000000004 T cpl_channel_rx_qc_print
0000004299182579 0000000000000004 T cpl_diags_register_dump
0000004299183213 0000000000000004 T cpl_dwld_fw
0000004299182965 0000000000000004 T cpl_link_status_query_dump
0000004299183357 0000000000000004 T cpl_mcu_debug_log_dump
0000004299183361 0000000000000004 T cpl_mcu_debug_log_query_dump
0000004299183353 0000000000000004 T cpl_mcu_pc_log_query_dump
0000004299183365 0000000000000004 T cpl_mcu_status_query_dump
0000004299182571 0000000000000004 T cpl_prbs_chk_ber
0000004299182575 0000000000000004 T cpl_prbs_chk_status_query_print
0000004299182757 0000000000000004 T cpl_rx_dsp_hist_query_dump
0000004299182761 0000000000000004 T cpl_rx_dsp_hist_query_dump_to_file
0000004299183221 0000000000000004 T cpl_rx_qc_stats_print
0000004299195595 0000000000000005 T cpl_pll_cp_overlays_to_rules
0000004299207596 0000000000000005 T cpl_rx_cp_overlays_to_rules
0000004299193654 0000000000000005 T cpl_tx_cp_overlays_to_rules
0000004299212259 0000000000000005 T cpl_tx_set
0000004299198229 0000000000000006 T cpl_reg_write
0000004299183199 0000000000000007 T cpl_show_progress
0000004299183206 0000000000000007 T cpl_show_progress_enable
0000004299193771 0000000000000008 T cpl_is_rx_ready
0000004299193761 0000000000000008 T cpl_is_tx_ready
0000004299250296 0000000000000008 r cpl_rx_qc_rules_default
0000004299182765 0000000000000008 T cpl_set_callback_for_lock
0000004299183296 0000000000000008 T cpl_set_callback_for_rcal
0000004299182807 0000000000000008 T cpl_set_callback_for_unlock
0000004299206198 0000000000000009 T cpl_tx_squelch_set
0000004299183341 0000000000000012 T cpl_mcu_decode_bootver
0000004299250484 0000000000000012 r cpl_pll_rules_default
0000004299222900 0000000000000014 T cpl_mcu_reset_into_application
0000004299182482 0000000000000015 T cpl_prbs_get_rx_hdwr_pat
0000004299182815 0000000000000018 T cpl_lock
0000004299182833 0000000000000018 T cpl_unlock
0000004299195576 0000000000000019 T cpl_pll_rules_query_dump
0000004299207577 0000000000000019 T cpl_rx_rules_query_dump
0000004299193635 0000000000000019 T cpl_tx_rules_query_dump
0000004299196348 0000000000000020 t cpl_fw_is_running
0000004299182441 0000000000000020 T cpl_prbs_get_rx_synth_pat
0000004299182421 0000000000000020 T cpl_prbs_get_synth_pat
0000004299208406 0000000000000020 T cpl_pwrup_iadc_ref_sel
0000004299193068 0000000000000020 T cpl_rx_dsp_snr_read_value
0000004299182461 0000000000000021 T cpl_prbs_get_hdwr_pat
0000004299177983 0000000000000022 t cpl_eru_rcal_callback
0000004299193781 0000000000000023 T cpl_tx_is_squelched
0000004299191963 0000000000000024 T cpl_reg_read
0000004299193042 0000000000000026 T cpl_rx_pam_read_mode
0000004299182851 0000000000000032 T cpl_dbg_translate_fw_mode
0000004299194114 0000000000000033 T cpl_rx_lol_get
0000004299182773 0000000000000034 T cpl_version
0000004299177947 0000000000000036 t cpl_mse_binary_search
0000004299208334 0000000000000036 T cpl_rx_latched_lol_clear
0000004299208370 0000000000000036 T cpl_rx_latched_los_clear
0000004299194078 0000000000000036 T cpl_rx_los_get
0000004299182972 0000000000000037 T cpl_pll_rules_set_default
0000004299182534 0000000000000037 T cpl_prbs_chk_rules_set_default
0000004299182497 0000000000000037 T cpl_prbs_gen_rules_set_default
0000004299183304 0000000000000037 T cpl_pwrup_rules_set_default
0000004299183046 0000000000000037 T cpl_tx_fir_set_default
0000004299183009 0000000000000037 T cpl_tx_rules_set_default
0000004299197409 0000000000000038 T cpl_mcu_fw_mode_query
0000004299182147 0000000000000042 T cpl_rebase_channel_by_addr
0000004299210647 0000000000000044 t cpl_mcu_msg_unlock
0000004299182189 0000000000000046 T cpl_reg_channel_addr
0000004299197256 0000000000000047 T cpl_pwrup_is_eru_ready
0000004299217471 0000000000000048 t cpl_pif_read
...
0000000004212988 0000000000000202 T ctc_mcu_pif_write
0000000004224138 0000000000000204 T cpl_tx_fir_query
0000000004262880 0000000000000207 t rx_rules_deserialize
0000000004223657 0000000000000208 T cpl_is_fw_running_ok
0000000004265200 0000000000000208 r prbs_chk_rule_ops
0000000004265408 0000000000000208 r prbs_gen_rule_ops
0000000004222749 0000000000000210 T cpl_dbg_fsm_query
0000000004251252 0000000000000211 T cpl_tx_equalization_set
0000000004262598 0000000000000211 t rx_rules_serialize
0000000004252314 0000000000000215 T cpl_mcu_pif_write_bcast
0000000004225235 0000000000000219 T cpl_mcu_version_query
0000000004228086 0000000000000221 T cpl_prbs_gen_error_inject
0000000004215760 0000000000000221 t xbar_disconnect
0000000004215315 0000000000000222 T ctc_mcu_get_buffer_address
0000000004238220 0000000000000224 T cpl_init
0000000004266960 0000000000000224 r tx_rules_ops
0000000004222287 0000000000000226 T cpl_version_firmware
0000000004267184 0000000000000232 r rx_rules_ops
0000000004208348 0000000000000234 t signalling_set
0000000004222513 0000000000000236 t mcu_fw_version
0000000004233294 0000000000000241 T cpl_channel_rx_qc_query
0000000004223115 0000000000000244 T cpl_wait_for_link_ready
0000000004238444 0000000000000244 t dev_init
0000000004232138 0000000000000249 t ctc_def_chk_status_query
0000000004247717 0000000000000250 T cpl_diags_internal_data_query
0000000004251463 0000000000000252 T cpl_tx_fir_set
0000000004213491 0000000000000255 T ctc_mcu_pif_read
0000000006402240 0000000000000256 d lynx_pkg_info
0000000004249101 0000000000000259 T cpl_mcu_pif_write
0000000004213931 0000000000000263 T ctc_mcu_pif_check
0000000004214433 0000000000000267 t ctc_msg_send.constprop.23
0000000004242096 0000000000000268 t init
0000000004244818 0000000000000279 T cpl_pwrup_bias_pwrup
0000000004269488 0000000000000280 r ctc_def_hsc_dev_ops
0000000006402640 0000000000000280 b ops_overide
0000000004226851 0000000000000281 T cpl_tx_invert_toggle
0000000004268832 0000000000000300 r cpl_snr_mon_tbl_5_79
0000000004214700 0000000000000321 t ctc_msg_recv.constprop.22
0000000004242364 0000000000000326 T cpl_pwrup_eru_pwrup
0000000004237876 0000000000000330 T cpl_mcu_reset_into_mode
0000000004221889 0000000000000339 t link_ready_wait
0000000004247327 0000000000000346 T cpl_mcu_pif_read
0000000004239222 0000000000000349 T cpl_init_rx
0000000004232939 0000000000000355 T cpl_channel_mask_rx_qc_update
0000000004238688 0000000000000355 T cpl_init_tx
0000000004248162 0000000000000360 t cpl_mcu_msg_wait_and_lock
0000000004248652 0000000000000369 T cpl_mcu_debug_log_query
0000000004212532 0000000000000377 t xbar_2to1_config
0000000004253085 0000000000000384 t xbar_chn_connect
0000000004262056 0000000000000388 t ctc_def_chk_rules_apply
0000000004225846 0000000000000390 T cpl_tx_cp_rules_to_overlays
0000000004243086 0000000000000394 T cpl_eru_query_temperature
0000000004236237 0000000000000394 T cpl_mcu_status_query
0000000004227132 0000000000000395 T cpl_rx_invert_toggle
0000000004242690 0000000000000396 T cpl_pwrup_eru_qpmp_ldo_pwrup
0000000004253469 0000000000000401 t xbar_rules_apply
0000000004227666 0000000000000420 T ctc_def_chk_rules_update
0000000004234243 0000000000000441 T cpl_rx_dsp_get_histogram_bypass
0000000004249625 0000000000000453 t cpl_mcu_msg_push_message
0000000004219070 0000000000000463 T ctc_mcu_reset_into_mode
0000000004219851 0000000000000503 t is_link_ready
0000000004246722 0000000000000504 T ctc_def_dev_all_cpls_in_die_init
0000000004220753 0000000000000506 T cpl_tx_rules_query
0000000004226236 0000000000000615 T cpl_rx_cp_rules_to_overlays
0000000004245097 0000000000000639 T cpl_pwrup_bias_qpmp_ldo_pwrup
0000000004237087 0000000000000651 T cpl_mcu_get_buffer_address
0000000004263657 0000000000000655 T ctc_def_bundle_rules
0000000004233535 0000000000000686 T cpl_rx_rules_query
0000000004250078 0000000000000728 t cpl_mcu_msg_pull_message
0000000004235133 0000000000000809 T cpl_pwrup_cal_rcal
0000000004217198 0000000000000810 t xbar_2xnrz_1xpam_fifo_config
0000000004218008 0000000000000883 t xbar_2xpam_1xpam_fifo_config
0000000004241162 0000000000000934 T ctc_def_bundle_delete
0000000004267872 0000000000000948 r cpl_snr_mon_tbl_80_1024
0000000004245736 0000000000000986 T cpl_pwrup_start
0000000004216128 0000000000001070 t xbar_4xnrz_1xpam_fifo_config
0000000004229637 0000000000001096 T cpl_prbs_chk_config
0000000004228431 0000000000001206 T cpl_prbs_gen_config
0000000004243480 0000000000001338 T cpl_pwrup_eru_rpll_init
0000000004239571 0000000000001395 t none_anlt_start
0000000004230733 0000000000001405 T cpl_prbs_chk_status
0000000004254092 0000000000002050 t ctc_def_gen_rules_apply
0000000004256491 0000000000005499 t start
```
E get branch nay `users/cphan/LYNX_API_NIGHTLY_936_optimize_size`

```
size: 107493 bytes  105.0 KiB
0000000004224051 0000000000000420 T ctc_def_chk_rules_update
0000000004230628 0000000000000441 T cpl_rx_dsp_get_histogram_bypass
0000000004246010 0000000000000453 t cpl_mcu_msg_push_message
0000000004215455 0000000000000463 T ctc_mcu_reset_into_mode
0000000004216236 0000000000000503 t is_link_ready
0000000004243107 0000000000000504 T ctc_def_dev_all_cpls_in_die_init
0000000004217138 0000000000000506 T cpl_tx_rules_query
0000000004222621 0000000000000615 T cpl_rx_cp_rules_to_overlays
0000000004241482 0000000000000639 T cpl_pwrup_bias_qpmp_ldo_pwrup
0000000004233472 0000000000000651 T cpl_mcu_get_buffer_address
0000000004257102 0000000000000655 T ctc_def_bundle_rules
0000000004229920 0000000000000686 T cpl_rx_rules_query
0000000004246463 0000000000000728 t cpl_mcu_msg_pull_message
0000000004231518 0000000000000809 T cpl_pwrup_cal_rcal
0000000004237547 0000000000000934 T ctc_def_bundle_delete
0000000004261280 0000000000000948 r cpl_snr_mon_tbl_80_1024
0000000004242121 0000000000000986 T cpl_pwrup_start
0000000004226022 0000000000001096 T cpl_prbs_chk_config
0000000004224816 0000000000001206 T cpl_prbs_gen_config
0000000004239865 0000000000001338 T cpl_pwrup_eru_rpll_init
0000000004235956 0000000000001395 t none_anlt_start
0000000004227118 0000000000001405 T cpl_prbs_chk_status
0000000004253193 0000000000002050 t ctc_def_gen_rules_apply
0000000004250241 0000000000002860 t start
size: 100077 bytes  97.7 KiB
```

Removable fuctions
```
0000000004217198 0000000000000810 t xbar_2xnrz_1xpam_fifo_config
0000000004218008 0000000000000883 t xbar_2xpam_1xpam_fifo_config
0000000004216128 0000000000001070 t xbar_4xnrz_1xpam_fifo_config
```
```c
#ifndef HSC_HAS_SIZE_OPTIMIZE_PATH_SETUP
```
```c
#endif // HSC_HAS_SIZE_OPTIMIZE_PATH_SETUP
```


```
#ifndef HSC_HAS_SIZE_OPTIMIZE_XBAR
```

```c
#endif // HSC_HAS_SIZE_OPTIMIZE_XBAR
```


```
bash-4.2$ size build-output/amalgamated/example 
   text    data     bss     dec     hex filename
 291306    1096    2112  294514   47e72 build-output/amalgamated/example
```
[[size.csv]]
What is this size?
function size or mem size?
```
Dz, hiện tại customer đang có nhu cầu optimize Lynx API xuống 64K (edited) 
Hiện tại thấy đang compile ra 190K
I would say these are our requirements at this point
1.	Supports duplex retimer at 56.25G and 53.125G @ PAM4 
2.	Support PRBS13 only at these rates. Both generator and checker
3.	We are booting from the flash memory so all the inbuilt arrays can be removed
4.	Any MDIO operation can be removed as we are I2C centric 
```
### Related:
- [[Inphi gen file size report]]
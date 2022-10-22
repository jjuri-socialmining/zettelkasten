---
title: Spica5 api checklist to integrate GUI
created: 2022-Sep-14
tags:
  - 'tasks/done'
project: spica5
date:
  - start: 2022-09-14
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Tasks list]]

### Rules config

#### Rules set/get
| Buldle rules                        | Implement |
| ----------------------------------- | --------- |
| odsp_bundle_rules_chns_mask_set     | x         |
| odsp_bundle_rules_protocol_mode_set | x         |
| odsp_bundle_rules_baud_rate_set     | x         |
| odsp_bundle_rules_ieee_demap_enable | x         |
| odsp_bundle_rules_signalling_set    | x         |


| Tx rules                          | Implement |
| --------------------------------- | --------- |
| odsp_tx_rules_gray_mapping_enable | x         |
| odsp_tx_rules_dfe_precoder_enable | x         |
| odsp_tx_rules_swing_set           | x         |
| odsp_tx_rules_fir_taps_set        | x         |
| odsp_tx_rules_eye_set             | x         |
|                                   |           |

| Rx rules                          | Implement |
| --------------------------------- | --------- |
| odsp_rx_rules_dsp_mode_get        | x         |
| odsp_rx_rules_autoctle_enable     | x         |
| odsp_rx_rules_polarity_set        | x         |
| odsp_rx_rules_gray_mapping_enable | x         |
| odsp_rx_rules_vga_tracking_enable | x         |
| odsp_rx_rules_dfe_precoder_enable | x         |
| odsp_rx_rules_ctle_code_set       | x         |

#### ASIC apply/query
|                         | Implement |
| ----------------------- | --------- |
| odsp_bundle_init        | x         |
| odsp_bundle_start       | x         |
| odsp_bundle_rules_query | x         |


### Dashboard

|                             | Implement |
| --------------------------- | --------- |
| odsp_chn_fw_is_locked       |           |
| odsp_chn_pll_is_locked      |           |
| odsp_chn_dsp_is_ready       |           |
| odsp_chn_signal_is_detected |           |
| odsp_chn_pmd_state_get      |           |
| odsp_chn_reset_count_get    |           |
| odsp_chn_is_power_down      |           |
| odsp_chn_polarity_set       |           |
| odsp_chn_polarity_toggle    |           |
| odsp_chn_squelch            | x         |
| odsp_chn_fir_taps_set       |           |
|                             |           |


### PRBS
#### Generator

|                           | Implement |
| ------------------------- | --------- |
| odsp_prbs_gen_rules_apply |           |
| odsp_prbs_gen_rules_query |           |

#### Checker

|                            | Implement |
| -------------------------- | --------- |
| odsp_prbs_chk_rules_apply  |           |
| odsp_prbs_chk_rules_query  |           |
| odsp_prbs_chk_status_query |           |


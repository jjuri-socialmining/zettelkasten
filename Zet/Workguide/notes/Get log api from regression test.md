# Get log api from regression test

Run the regression with flag `--log_api_calls sequence` it will generate a txt file under `regression/capella/results/api_cal_log` with the name of the test

```python
hsc_dev_fw_is_running(hsc_dev_s)
hsc_dnld_verify_enable(hsc_dnld_s, False)
hsc_dnld_download(hsc_dnld_s)
hsc_dev_init(hsc_dev_s)
hsc_bundle_rules_t()
hsc_dev_bundle_rules(hsc_dev_s, 0, hsc_bundle_rules_s)
hsc_bundle_rules_chns_mask_set(hsc_bundle_rules_s, 8, 1)
hsc_bundle_rules_chns_mask_set(hsc_bundle_rules_s, 1, 1)
hsc_bundle_rules_chns_mask_set(hsc_bundle_rules_s, 2, 1)
hsc_bundle_rules_chns_mask_set(hsc_bundle_rules_s, 4, 1)
hsc_bundle_rules_baud_rate_set(hsc_bundle_rules_s, 25781250)
hsc_bundle_rules_signalling_set(hsc_bundle_rules_s, 1, 1)
hsc_bundle_rules_signalling_set(hsc_bundle_rules_s, 2, 1)
hsc_chn_rx_rules(hsc_bundle_rules_s, 0, 3)
hsc_chn_rx_rules(hsc_bundle_rules_s, 0, 3)
hsc_rx_rules_dsp_mode_set(hsc_rx_rules_s, 0)
hsc_chn_tx_rules(hsc_bundle_rules_s, 0, 3)
hsc_chn_tx_rules(hsc_bundle_rules_s, 0, 3)
hsc_tx_rules_fir_taps_set(hsc_tx_rules_s, 0, [-50, 400, 0, 0, 0, 0, 0])
hsc_an_rules(hsc_bundle_rules_s, 3)
hsc_an_rules_enable(hsc_an_rules_s, True)
hsc_anlt_chn_t()
hsc_bundle_rules_link_leader_set(hsc_bundle_rules_s, 3, hsc_anlt_chn_t)
hsc_an_rules_mode_set(hsc_an_rules_s, 0)
hsc_an_cap_t()
hsc_an_rules_cap_ad_set(hsc_an_rules_s, 2, hsc_an_cap_t)
hsc_lt_rules(hsc_bundle_rules_s, 3)
hsc_lt_rules_enable(hsc_lt_rules_s, False)
hsc_anlt_chn_t()
hsc_bundle_rules_link_folwr_by_idx_set(hsc_bundle_rules_s, 3, 0, hsc_anlt_chn_t)
hsc_bundle_t()
hsc_dev_bundle(hsc_dev_s, 0, hsc_bundle_s)
hsc_bundle_init(hsc_bundle_s, hsc_bundle_rules_s)
hsc_bundle_start(hsc_bundle_s, hsc_bundle_rules_s)
hsc_bundle_rules_show(hsc_bundle_s)
hsc_bundle_rules_chns_mask_get(hsc_bundle_rules_s, 1)
hsc_bundle_rules_chns_mask_get(hsc_bundle_rules_s, 2)
hsc_bundle_rules_chns_mask_get(hsc_bundle_rules_s, 4)
hsc_bundle_rules_chns_mask_get(hsc_bundle_rules_s, 8)
hsc_chn_t()
hsc_dev_chn(hsc_dev_s, 0, 1, hsc_chn_s)
hsc_chn_an_status_get(hsc_chn_s)
hsc_an_result_t()
hsc_chn_t()
hsc_dev_chn(hsc_dev_s, 0, 1, hsc_chn_s)
hsc_chn_an_result_get(hsc_chn_s, hsc_an_result_t)
hsc_chn_t()
hsc_dev_chn(hsc_dev_s, 0, 1, hsc_chn_s)
hsc_chn_an_fsm_state_get(hsc_chn_s)
hsc_an_result_t()
hsc_chn_t()
hsc_dev_chn(hsc_dev_s, 0, 1, hsc_chn_s)
hsc_chn_an_result_get(hsc_chn_s, hsc_an_result_t)
hsc_anlt_an_hcd_translate(2)
hsc_chn_t()
hsc_dev_chn(hsc_dev_s, 0, 1, hsc_chn_s)
hsc_chn_an_status_get(hsc_chn_s)
```

Another sample command
```
pytest tests/anlt/test_anlt.py -k "Multiple and not rate_1x" --collect-only --quiet --type_of_regression reduced_anlt
```


Regression log
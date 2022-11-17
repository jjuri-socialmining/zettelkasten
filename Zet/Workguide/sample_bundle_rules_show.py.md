```python
# Import register and API
from lynx_400.python import hsc_api as api

# Get number of die on this device over API
dev = api.hsc_dev_t()
api.hsc_dev(dev, 0)


bundle_id = 0
tx_intf = api.HSC_INTF_LTX # HSC_INTF_HTX
rx_intf = api.HSC_INTF_LRX # HSC_INTF_HRX
chn_id = 0


def bool2str(bool_val):
    return "True" if bool_val == True else "False"


def tx_swing_str(tx_swing):
    switcher = {
        api.HSC_TX_SWING_60p:  "60 %",
        api.HSC_TX_SWING_70p:  "70 %",
        api.HSC_TX_SWING_80p:  "80 %",
        api.HSC_TX_SWING_90p:  "90 %",
        api.HSC_TX_SWING_100p: "100 %",
        api.HSC_TX_SWING_110p: "110 %",
        api.HSC_TX_SWING_120p: "120 %",
    }
 
    return switcher.get(tx_swing, "N/A")

def lut_mode_str(lut):
    switcher = {
        api.HSC_TX_LUT_3TAP:     "3-Tap LUT",
        api.HSC_TX_LUT_BYPASS:   "BYPASS",
        api.HSC_TX_LUT_7TAP_LIN: "7-Tap LIN",
        api.HSC_TX_LUT_7TAP_LUT: "7-Tap LUT",
    }
 
    return switcher.get(lut, "N/A")


def dsp_mode_to_str(dsp_mode):
    switcher = {
        api.HSC_DSP_MODE_SLC1:                 "SLC1",
        api.HSC_DSP_MODE_SLC1_RC_SLC2:         "SLC1_RC_SLC2",
        api.HSC_DSP_MODE_SLC1_MPICAN_SLC2:     "SLC1_MPICAN_SLC2",
        api.HSC_DSP_MODE_SLC1_RC_MPICAN_SLC2:  "SLC1_RC_MPICAN_SLC2",
        api.HSC_DSP_MODE_DFE1:                 "DFE1",
        api.HSC_DSP_MODE_DFE1_RC_DFE2:         "DFE1_RC_DFE2",
        api.HSC_DSP_MODE_DFE1_MPICAN_DFE2:     "DFE1_MPICAN_DFE2",
        api.HSC_DSP_MODE_DFE1_RC_MPICAN_DFE2:  "DFE1_RC_MPICAN_DFE2",
    }
    return switcher.get(dsp_mode, "N/A")


def afe_trim_to_str(afe_trim):
    switcher = {
        api.HSC_AFE_TRIM_BYPASS:     "bypass",
        api.HSC_AFE_TRIM_ISSE:       "ISSE",
        api.HSC_AFE_TRIM_AUTO:       "Auto",
        api.HSC_AFE_TRIM_0dB:        "0dB",
        api.HSC_AFE_TRIM_NEG_0p5dB:  "-0.5dB",
        api.HSC_AFE_TRIM_NEG_1dB:    "-1dB",
        api.HSC_AFE_TRIM_NEG_2dB:    "-2dB",
        api.HSC_AFE_TRIM_NEG_4dB:    "-4dB",
        api.HSC_AFE_TRIM_NEG_7dB:    "-7dB",
        api.HSC_AFE_TRIM_NEG_10dB:    "-10dB",
        api.HSC_AFE_TRIM_NEG_11dB:   "-11dB",
    }

    return switcher.get(afe_trim, "N/A")


def tx_rules_show(bundle_rules, chn_id, tx_intf):

    tx_rules = api.hsc_chn_tx_rules(bundle_rules, chn_id, tx_intf)
    status, lut, taps = api.hsc_tx_rules_fir_taps_get(tx_rules)

    print("chn_id | sig | baudrate | gray | dfe  | invert | eye1,eye2 | swing |    LUT    | taps ")
    print("--------------------------------------------------------------------------------------------------")
    print("%6d " % chn_id, end="|")

    print("%3s " % "PAM" if api.hsc_tx_rules_signalling_get(tx_rules) == api.HSC_SIGNAL_MODE_PAM else "NRZ", end=" |")
    print("%9d " % api.hsc_tx_rules_baud_rate_get(tx_rules), end="|")

    print("%5s " % bool2str(api.hsc_tx_rules_gray_mapping_is_enabled(tx_rules)), end="|")
    print("%5s " % bool2str(api.hsc_tx_rules_dfe_precoder_is_enabled(tx_rules)), end="|")
    print("%7s " % bool2str(api.hsc_tx_rules_polarity_get(tx_rules)), end="|")
    print("%4d " % (api.hsc_tx_rules_eye_get(tx_rules, api.HSC_EYE_LEVEL_LOWER)), end=",")
    print("%4d " % (api.hsc_tx_rules_eye_get(tx_rules, api.HSC_EYE_LEVEL_UPPER)), end="|")
    print("%5s " % tx_swing_str(api.hsc_tx_rules_swing_get(tx_rules)), end=" |")
    print("%10s " % lut_mode_str(lut), end="|")
    print(taps, end="\n")


def rx_rules_show(bundle_rules, chn_id, rx_intf):
    rx_rules = api.hsc_chn_rx_rules(bundle_rules, chn_id, rx_intf)
    advanced = api.hsc_rx_rules_advanced_t()
    api.hsc_rx_rules_advanced_get(rx_rules, advanced)

    print("\n")
    print("chn_id | Sig | Baudrate | DSP Mode    | Gray | Invert | AFE Trim | VGA Track | demap | CTLE auto, codes |")
    print("-------+-----+----------+-------------+------+--------+----------+-----------+-------+------------------+")

    print("%6d " % chn_id, end="|")
    print("%3s " % "PAM" if api.hsc_rx_rules_signalling_get(rx_rules) == api.HSC_SIGNAL_MODE_PAM else "NRZ", end=" |")
    print("%9d " % api.hsc_rx_rules_baud_rate_get(rx_rules), end="|")
    print("%12s " % dsp_mode_to_str(api.hsc_rx_rules_dsp_mode_get(rx_rules)), end="|")
    print("%5s " % bool2str(api.hsc_rx_rules_gray_mapping_is_enabled(rx_rules)), end="|")
    print("%7s " % bool2str(api.hsc_rx_rules_polarity_get(rx_rules)), end="|")
    print("%8s " % afe_trim_to_str(advanced.afe_trim), end=" |")
    print("%9s " % bool2str(api.hsc_rx_rules_vga_tracking_is_enabled(rx_rules)), end=" |")
    print("%6s " % bool2str(api.hsc_rx_rules_ieee_demap_is_enabled(rx_rules)), end="|")
    print("%7s " % bool2str(api.hsc_rx_rules_autoctle_is_enabled(rx_rules)), end="")
    print((api.hsc_rx_rules_ctle_code_get(rx_rules)), end="\n")


def rx_status_show(chn_id, rx_intf):
    '''
    chn_id:
    rx_intf: HSC_INTF_LRX/HSC_INTF_HRX
    '''
    chn = api.hsc_chn_t()
    api.hsc_dev_chn(dev, chn_id, rx_intf, chn)
    print("\n")
    print(" SDT  | DSP  | FW locked | PMD | RST CNT | SNR | DSPgain")
    print("%5s " % bool2str(api.hsc_chn_signal_is_detected(chn)), end="|")
    print("%5s " % bool2str(api.hsc_chn_dsp_is_ready(chn)), end="|")
    print("%10s " % bool2str(api.hsc_chn_fw_is_locked(chn)), end="|")
    print("%4d " % api.hsc_chn_pmd_state_get(chn), end="|")
    print("%8d " % api.hsc_chn_reset_count_get(chn), end="|")
    print("%4.2f " % api.hsc_chn_dsp_snr_mon_value_get(chn, api.HSC_SNR_VALUE_FMT_DB), end="|")
    #print("%7d " % api.hsc_chn_dsp_gain_get(chn), end="\n\n")
    print("\n")
    print("sub_chn", "[pre3, pre2, pre1, main, post1, post2, post3, post4, post5, post6 ]")
    for sub_chn in range(32):
        status, taps = (api.hsc_chn_dsp_ffe_taps_query(chn, sub_chn))
        print(sub_chn, taps)


def bundle_rules_query():
    bundle = api.hsc_bundle_t()
    api.hsc_dev_bundle(dev, 0, bundle)

    bundle_rules = api.hsc_bundle_rules_t()
    api.hsc_dev_bundle_rules(dev, 0, bundle_rules)

    api.hsc_bundle_rules_query(bundle, bundle_rules)
    
    return bundle_rules
    

    
tx_rules_show(bundle_rules_query(), chn_id, tx_intf)
rx_rules_show(bundle_rules_query(), chn_id, rx_intf)
rx_status_show(chn_id, rx_intf)
```

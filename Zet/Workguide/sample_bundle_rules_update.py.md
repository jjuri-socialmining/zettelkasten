```python
# Import register and API
from lynx_400.python import hsc_api as api

# Get number of die on this device over API
dev = api.hsc_dev_t()
api.hsc_dev(dev, 0)

hrx_channel = 0
chn_list = [0, 1, 2, 3]

rules = api.hsc_bundle_rules_t()
api.hsc_dev_bundle_rules(dev, api.HSC_OPER_MODE_DUAL_PRBS, rules)

bundle = api.hsc_bundle_t()
api.hsc_dev_bundle(dev, hrx_channel, bundle)

status = api.hsc_bundle_rules_query(bundle, rules)
print ("hsc_bundle_rules_query", status == api.HSC_OK)

adv_rules = api.hsc_rx_rules_advanced_t()

for chn in chn_list:

    # Host rx rule
    rx_rules = api.hsc_chn_rx_rules(rules, chn, api.HSC_INTF_HOST)
    api.hsc_rx_rules_advanced_get(rx_rules, adv_rules)
    adv_rules.afe_trim = api.HSC_AFE_TRIM_AUTO
    adv_rules.mlsd_en = True
    api.hsc_rx_rules_advanced_set(rx_rules, adv_rules)

    # Line rx rule
    rx_rules = api.hsc_chn_rx_rules(rules, chn, api.HSC_INTF_LINE)
    api.hsc_rx_rules_advanced_get(rx_rules, adv_rules)
    adv_rules.afe_trim = api.HSC_AFE_TRIM_NEG_4dB
    adv_rules.mlsd_en = False
    api.hsc_rx_rules_advanced_set(rx_rules, adv_rules)

taps = [-50, 650, 0]

for chn in chn_list:
    # Host tx rule
    tx_rules = api.hsc_chn_tx_rules(rules, chn, api.HSC_INTF_HOST)
    api.hsc_tx_rules_fir_taps_set(tx_rules, api.HSC_TX_LUT_3TAP, taps)

    # Line tx rule
    tx_rules = api.hsc_chn_tx_rules(rules, chn, api.HSC_INTF_LINE)
    api.hsc_tx_rules_fir_taps_set(tx_rules, api.HSC_TX_LUT_3TAP, taps)


status = api.hsc_bundle_init(bundle, rules)
print ("hsc_bundle_init", status == api.HSC_OK)

status = api.hsc_bundle_start(bundle, rules)
print ("hsc_bundle_start", status == api.HSC_OK)

# api.hsc_bundle_rules_show(bundle)

```
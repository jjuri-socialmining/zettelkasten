

## Device
```python
dev = api.odsp_dev_t()
api.odsp_dev(dev, 0)

num_dies = api.odsp_dev_num_dies(dev)
print(num_dies)

num_chns = api.odsp_dev_num_chns(dev, api.ODSP_INTF_HOST)
print(num_chns)
```

## Bundle
```python
bundle = api.odsp_bundle_t()
api.odsp_dev_bundle(dev, 0, bundle)

rules = api.odsp_bundle_rules_t()
api.odsp_dev_bundle_rules(dev, 0, rules)
print("odsp_bundle_rules_query", api.odsp_bundle_rules_query(bundle, rules))
print("odsp_bundle_rules_chns_mask_get %x" % api.odsp_bundle_rules_chns_mask_get(rules, api.ODSP_INTF_HOST))
```

## Channel
```python
dev = api.odsp_dev_t()
api.odsp_dev(dev, 0)
num_dies = api.odsp_dev_num_dies(dev)

chn = api.odsp_chn_t()
api.odsp_dev_chn(dev, 0, api.ODSP_INTF_LTX, chn)
print("is_power_down      :", api.odsp_chn_is_power_down(chn))
print("fw_is_locked       :", api.odsp_chn_fw_is_locked(chn))
print("dsp_is_ready       :", api.odsp_chn_dsp_is_ready(chn))
print("signal_is_detected :", api.odsp_chn_signal_is_detected(chn))

api.odsp_dev_chn(dev, 0, api.ODSP_INTF_LRX, chn)
print("is_power_down      :", api.odsp_chn_is_power_down(chn))
print("fw_is_locked       :", api.odsp_chn_fw_is_locked(chn))
print("dsp_is_ready       :", api.odsp_chn_dsp_is_ready(chn))
print("signal_is_detected :", api.odsp_chn_signal_is_detected(chn))
```

![[eye_chn.py]]

### MCU
![[sample_mcu_load_fw_from_file.py]]
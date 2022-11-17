

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
```python

# Import register and API
from lynx_400.python import lynx_400_registers as creg
from lynx_400.python import hsc_api as api
import time
# Get number of die on this device over API
dev = api.hsc_dev_t()
api.hsc_dev(dev, 0)
num_dies = api.hsc_dev_num_dies(dev)

ctle_stage = 0
chn_to_handle = api.hsc_chn_t()
api.hsc_dev_chn(dev, 0, api.HSC_INTF_HRX, chn_to_handle)
ctle = 9
api.hsc_chn_ctle_code_set(chn_to_handle, ctle, ctle_stage)
cur = time.time()
print(cur)
while True:
    tem = api.hsc_chn_ctle_code_get(chn_to_handle, ctle_stage)
    print(tem)
    if ctle == tem:
        break

print(time.time() - cur)
```
### MCU
![[sample_mcu_load_fw_from_file.py]]

### PRBS
[[prbs_sample.py]]

### Bundle rules
[[sample_bundle_rules_update.py]]
[[sample_bundle_rules_show.py]]

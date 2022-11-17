```python
# Import register and API
from lynx_400.python import lynx_400_registers as creg
from lynx_400.python import hsc_api as capi

# Get number of die on this device over API
dev = capi.hsc_dev_t()
capi.hsc_dev(dev, 0)
num_dies = capi.hsc_dev_num_dies(dev)

chn = capi.hsc_chn_t()

capi.hsc_dev_chn(dev, 0, capi.HSC_INTF_HRX, chn)
status, ltp = capi.hsc_chn_dsp_ltp_get(chn, capi.HSC_VALUE_FMT_16p8_FIXP)
print(status, ltp)

status, ltp = capi.hsc_chn_dsp_ltp_get(chn, capi.HSC_VALUE_FMT_DB)
print(status, ltp)
```
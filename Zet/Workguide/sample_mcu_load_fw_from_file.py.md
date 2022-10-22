```python
dev = capi.odsp_dev_t()
dnld = capi.odsp_dnld_t()

capi.odsp_dev(dev, 0)

path = "/path/to/firmware/image/firmware_direct_download.txt"

capi.odsp_dev_mcu_dnld(dev, 0x1, dnld)

capi.odsp_dnld_verify_enable(dnld, False)

capi.odsp_dnld_download_from_file(dnld, path)

```


```python
mcu = capi.odsp_mcu_t()
capi.odsp_dev_mcu(dev, 0x1, mcu)
capi.odsp_mcu_stall(dnld, False)
```

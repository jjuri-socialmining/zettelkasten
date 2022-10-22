---
title: Add spica5 uapi to support GUI
created: 2022-Oct-19
tags:
  - 'tasks/todo'
project: TBD
date:
  - start: 2022-10-19
  - end: 'TBD'
  - due: 'TBD'
publish: False
---
up:: [[Tasks list]]

- [x] Todo add: pkg type ✅ 2022-10-19

```c
uint8_t (*pkg_type_get)(hsc_dev_t *dev);
hsc_status_t (*pkg_type_set)(hsc_dev_t *dev, uint8_t pkg_type);
/**
 * This method is used to indicate the current package type of device
 *
 * @param dev           [I] - Device handle.
 *
 * @return package type, will define on specific product
 */
uint8_t hsc_dev_pkg_type_get(hsc_dev_t *dev);

/**
 * This method is used to set the current package type of device
 *
 * @param dev           [I] - Device handle.
 *
 * @return HSC_OK on success, HSC_ERROR on failure.
 */
hsc_status_t hsc_dev_pkg_type_set(hsc_dev_t *dev, uint8_t pkg_type);


uint8_t hsc_dev_pkg_type_get(hsc_dev_t *dev)
{
    if (HSC_DEV_OPS_VALID(pkg_type_get))
    {
        bool type = 0;

        HSC_LOCK(dev, 0);
        type = HSC_DEV_OPS(dev)->pkg_type_get(dev);
        HSC_UNLOCK(dev, 0);

        return type;
    }

    return 0;
}

hsc_status_t hsc_dev_pkg_type_set(hsc_dev_t *dev, uint8_t pkg_type)
{
    if (HSC_DEV_OPS_VALID(pkg_type_set))
    {
        hsc_status_t status = HSC_ERROR;

        HSC_LOCK(dev, HSC_ERROR);
        status = HSC_DEV_OPS(dev)->pkg_type_set(dev, pkg_type);
        HSC_UNLOCK(dev, HSC_ERROR);

        return status;
    }

    return HSC_ERROR;
}
```

- [x] PLL FSM dashboard spica5 ⏫ ✅ 2022-10-19

```c
/**
 * This method is called to get the pll state of channel.
 *
 * @param chn   [I] - The channel handle.
 *
 * @return pll fsm state
 */
uint32_t hsc_chn_pll_state_get(hsc_chn_t *chn);
uint32_t (*pll_state_get)(hsc_chn_t *chn);

uint32_t hsc_chn_pll_state_get(hsc_chn_t *chn)
{
    if (HSC_CHN_OPS_VALID(pll_state_get))
    {
        uint32_t ret = 0;

        HSC_LOCK(HSC_CHN_DEV(chn), INVALID_UINT32_VAL);
        ret = HSC_CHN_OPS(chn)->pll_state_get(chn);
        HSC_UNLOCK(HSC_CHN_DEV(chn), INVALID_UINT32_VAL);

        return ret;
    }

    return INVALID_UINT32_VAL;
}
```

- [x] Reg instance ✅ 2022-10-19
```c
/**
 * This method is used to get the die and hardware id of given software channel
 * id and interface
 *
 * @param dev           [I] - Device handle.
 * @param chn_id        [I] - The channel Id
 * @param intf          [I] - The interface, detail in e_hsc_intf enum
 * @param die           [O] - The die id of channel
 * @param hw_id         [O] - The hardware id of channel
 *
 * @return HSC_OK on success, HSC_ERROR on failure.
 */
hsc_status_t hsc_dev_chn_remap(hsc_dev_t *dev, uint32_t chn_id, e_hsc_intf intf, uint32_t *die, uint32_t *hw_id);
```

- [x] Temperature -> Asked Thuan hide this on dashboard Spica5 GUI ⏫ ✅ 2022-10-19
	- ![[Pasted image 20221019100040.png]]

Add on this version [http://dc5lp-vlas-sw-01/projects/sw/spica5/uapi/nightly/0.0.1.143](http://dc5lp-vlas-sw-01/projects/sw/spica5/uapi/nightly/0.0.1.143)

- [ ] Retest on GUI [[Add spica5 uapi to support GUI]] 🔼 
---
title: CTLE
UID: 221108160516
created: 08-Nov-2022
tags:
  - 'created/2022/Nov/08'
  - 'permanent/concept'
aliases:
  -
publish: False
---

CTLE is lowpass filter


CTLE capella
- `ctle_manual_control` control dis/en table convert, do not relate to autoctle
- Auto ctle in bit7_6 of CTLE field.

If ctleauto enable -> read ctle in configure register, dont read in rules register:
Do it as following:

```c
    uint16_t ctle = CPL_RX_RXA_AFE_CTL0_CFG__CTLE1_PEAK__READ(die, hw_chn);
    uint16_t ctle2 = CPL_RX_RXA_AFE_CTL1_CFG__CTLE2_PEAK__READ(die, hw_chn);
```

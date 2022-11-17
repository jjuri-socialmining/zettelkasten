---
title: Collect setting in cpl should be interface on lynx rules
created: 2022-Nov-15
tags:
  - 'tasks/done'
project: TBD
date:
  - start: 2022-11-15
  - end: 'TBD'
  - due: 'TBD'
publish: False
---
up:: [[Tasks list]]

url:: https://essjira.marvell.com/browse/RETCSW-316

```
    bool ffe_track_en;

    uint8_t ffe_track_ted_mode;
    uint8_t ffe_taps_select;
    
    bool rc_dual_bank_en;
} cpl_rx_rules_t;

typedef struct
{
    bool enable;
    bool beta_adapt_enable;
    uint8_t coef_sel;
    uint8_t mul_sel;
} hsc_rx_rules_scdr_t;
```


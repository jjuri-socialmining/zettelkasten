---
title: spica5 MCU
created: 2022-Oct-18
tags:
  - 'permanent/common'
publish: False
---

```c
/* Number of dies */
#define SPICA5_NUM_DIES 1

/* Number of MCUs */
#define SPICA5_NUM_MCUS_PER_DIE 2
#define SPICA5_NUM_MCUS (SPICA5_NUM_DIES * SPICA5_NUM_MCUS_PER_DIE)

/* MCU ID assignment */
#define SPICA5_MAIN_MCU_ID 0
#define SPICA5_AUX_MCU_ID  1
#define SPICA5_HOST_MCU_ID(die) SPICA5_MAIN_MCU_ID
#define SPICA5_LINE_MCU_ID(die) SPICA5_AUX_MCU_ID
```

https://ewiki.marvell.com/display/ODSP/Spica5+Architecture

![[mcu_top_MAS_rev0p0.pdf]]

![[Pasted image 20221018145938.png]]

![[20221018145055 ~ MCU spica5.png]]

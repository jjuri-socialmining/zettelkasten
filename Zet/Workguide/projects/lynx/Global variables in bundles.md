---
title: Global variables in bundles
created: 2022-Jul-12
tags:
  - 'tasks/done'
project: TBD
date:
  - start: 2022-07-12
  - end: 'TBD'
  - due: 2022-07-12
---
up:: [[Issues list]]


> [!Mail from Rock Michael]
We are setting up or data paths and testing for CMIS compliance and noticing something odd about the bundles.  We are seeing bundle setting that are overwriting other bundle settings.  For instance:
>
>\-   Bundle_id 0 has channels 1-4 and an amplitude scalar of 60
>
>\-   Bundle_id 1 has channels 5-8 and an amplitude scalar of 100
>
>If we write bundle 0, then bundle 1, the amplitude for the channels associated with bundle 0 are being overwritten with 100 (instead of 60).  This leads me to believe that certain things are global and not bundle specific.  Is this the case?  If so, what else is global?

### Research

Amplitude Scalar

- [[CMIS documents]]
- [[Common Management Interface Specification (CMIS)]]
- [[amplitude scalar]] ??
	- https://en.wikipedia.org/wiki/Amplitude_and_phase-shift_keying

CMIS document
[[QSFP-DD-mgmt-rev3p0-final-9-18-18-Default-clean.pdf]]


> [!Notice] [[lynx_tuning_guide.pdf|Tunning Guide]]
CMIS has a table of voltage amplitude and EQ boost. In order to properly calculate the table, the issue will need a scope. Below is an equation to help estimate Lynx amplitude and EQ boost setting from the 3 tap FIR TX. 
>
> Vpp = |pre tap| + |main tap| + |post tap|
> 
> V ampltidue = pretap + main tap + post tap


Anh Thắng
> nếu là phía TX thì amplitude scalar là thông số để control peak-power cho NRZ hoặc PAM4
> còn phía RX thì là 1 dạng của trimming



## [[2022-07-13]]
```
It appears they figured out their 2 bundle issue and that is now working.

The problem they are now running into is when they create their script for 2 bundles the SNR performance on the Line side of the cable, Lynx to lynx across the cable, drops by about 3 or 4 dB when they configure the two separate bundles compared to when they do a single 8 lane bundle.

They say the only change they make is to the Host mask, from 0xff to either 0xf0 or 0x0F, where with the mask set to 0xff for a single bundle the performance is great.

However, when they change the mask to 0x0f and 0xf0 for the two 4x100G bundles the SNR performance drops by 3 to 4dB.

They have been analyzing the differences and the only difference they see is the change in the CMI_MODE.

When they run the 8 port script that is one bundle they see the CMI_MODE print out as AC coupled but when they run the script with 2 4 port bundles they see the CMI_MODE print out as DC coupled.

They are not changing anything but the Host mask so this parameter should not be changing.

They even tried adding in the Advanced Rule to set the CMI_MODE but it still always reads back as DC coupled when they setup 2 bundles.

We need to understand why this is happening and if it is actually influencing the performance.
```

[[CMI mode]]

![[Retimer_Config_functions.c]]
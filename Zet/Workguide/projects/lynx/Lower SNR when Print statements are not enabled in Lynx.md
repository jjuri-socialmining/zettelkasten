---
title: Lower SNR when Print statements are not enabled in Lynx
created: 2022-Oct-14
tags:
  - 'issue/todo'
project: TBD
date:
  - start: 2022-10-14
  - end: 'TBD'
  - due: 'TBD'
publish: False
---
up:: [[Issues list]]


```mail
**From:** Brad Wilson <[bwilson@marvell.com](mailto:bwilson@marvell.com)>  
**Sent:** Tuesday, August 2, 2022 11:01 PM  
**To:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>  
**Cc:** Bob Ward <[bward@marvell.com](mailto:bward@marvell.com)>  
**Subject:** RE: Firmware build vs BER (1).pptx

Hi Cuong,

TE is saying that if they don’t have the print statements then the SNR is worse when the links come up.

-   I’m assuming that. As your said, the issue maybe here is: If setup 8 lanes WITH “**Marvell print out infor**” the result is better than WIHOUT print out
```



```mail
**From:** Brad Wilson <[bwilson@marvell.com](mailto:bwilson@marvell.com)>  
**Sent:** Friday, October 14, 2022 8:51:05 AM  
**To:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>  
**Subject:** Lower SNR when Print statements are not enabled in Lynx

Hi Cuong,

TE is seeing a 2 to 3dB reduction in the SNR when they turn off the print statements that are part of the Lynx Code.

They say if they change the below highlighted defines to 0 in the hsc_config.h file so when the Lynx configuration is running it will not print out any statements then the SNR is 2 to 3dB lower than when these prints are enabled.

Can you please try this and see if you see this behavior?

Also,  can I try this by just changing these values or is there something else I need to do?

I tried changing them on my EVB with short cables and did not see a difference in the SNR.
```

SNR (Turn OFF print) < SNR (print)

Gui 6.1.372
Line
1708 
retimer
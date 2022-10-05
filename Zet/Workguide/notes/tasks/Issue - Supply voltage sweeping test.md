---
title: Issue - Supply voltage sweeping test
tags:
  - 'tasks/todo'
start: 2022-05-05
end: 'TBD'
---

Collect debug message to print out when this issue happen
- Thông tin nào cần in ra đây ta, 
	- Current có những api nào print?


```
**From:** Mike Takefman <[mtakefman@marvell.com](mailto:mtakefman@marvell.com)>  
**Sent:** Sunday, May 8, 2022 12:31 AM  
**To:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>; Parmanand Mishra <[mparmanand@marvell.com](mailto:mparmanand@marvell.com)>  
**Cc:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>; Santosh Padmanabha <[spadmanabha@marvell.com](mailto:spadmanabha@marvell.com)>  
**Subject:** RE: LYNX 800G Supply voltage step down/up

The device should keep working as long as you don’t ramp the voltage too sharply. It should still work even then, but I can’t promise it.
```

```
And Could you pls try to extend the waiting time for bundle_links ready… Just try to confirm this cannot UP permanent or need more time to come UP.  

Regards,

Cuong Phan

**From:** Cuong Phan  
**Sent:** Thursday, May 5, 2022 1:17 PM  
**To:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>; Dung Tran <[dutran@marvell.com](mailto:dutran@marvell.com)>  
**Subject:** RE: Optimize time to setup/query bundle

Yes, [@Dung Tran](mailto:dutran@marvell.com) will help to share the log msg query for debug analyzing purpose.

One thing, which supply voltage make the issue happen? How about if we do not sweep the voltage and set these value at the beginning.

Regards,

Cuong Phan

**From:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>  
**Sent:** Thursday, May 5, 2022 12:02 PM  
**To:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>; Dung Tran <[dutran@marvell.com](mailto:dutran@marvell.com)>  
**Subject:** RE: Optimize time to setup/query bundle

Hi Cuong,

No, DUT should work at supply voltage corners +/-10%nom, +/-5%nom,  +/-2.5%nom.

Other similar products worked at the same conditions.

This error is not repeatable on the same unit at specific test condition, but happens after few data path tests without reloading FW.

Is any debug func to dump all debug messages if this error showed up? So that I can collect debug data to explore further.

Regards,  
Guru

**From:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>  
**Sent:** Wednesday, May 4, 2022 9:18 PM  
**To:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>; Dung Tran <[dutran@marvell.com](mailto:dutran@marvell.com)>  
**Subject:** RE: Optimize time to setup/query bundle

So I think this is the TRUE error. The CHIP may not work under this condition.

Regards,

Cuong Phan

**From:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>  
**Sent:** Thursday, May 5, 2022 11:02 AM  
**To:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>; Dung Tran <[dutran@marvell.com](mailto:dutran@marvell.com)>  
**Subject:** RE: Optimize time to setup/query bundle

Hi Cuong,

Result is good 😊, without sweeping test.

Regards,  
Guru

**From:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>  
**Sent:** Wednesday, May 4, 2022 8:59 PM  
**To:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>; Dung Tran <[dutran@marvell.com](mailto:dutran@marvell.com)>  
**Subject:** RE: Optimize time to setup/query bundle

Hi Guru,

How about the result if we just run the data path without “supply voltage sweeping test”.

Regards,

Cuong Phan

**From:** Cuong Phan  
**Sent:** Thursday, May 5, 2022 10:53 AM  
**To:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>; Dung Tran <[dutran@marvell.com](mailto:dutran@marvell.com)>  
**Subject:** RE: Optimize time to setup/query bundle

+ DungTran

**From:** Guru Gnanaguru <[pgnanaguru@marvell.com](mailto:pgnanaguru@marvell.com)>  
**Sent:** Thursday, May 5, 2022 10:42 AM  
**To:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>  
**Subject:** RE: Optimize time to setup/query bundle

Hi Cuong,

It seems like “CRITICAL” error showed up intermittently, may be due to self-heating of device while running the same unit with supply voltage sweeping test for data path.

I have to reload FW into DUT and then found working for few runs and then again showed the same error.

Attached sample data. Pls check it and let me know how to fix this issue, since for characterization test, we need to run the same unit for different voltage settings to collect SNR, BER.

So, we should not see this error.



Regards,  
Guru

```
![[Pasted image 20220505140748.png]]


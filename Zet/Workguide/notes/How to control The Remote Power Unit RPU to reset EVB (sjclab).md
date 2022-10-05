---
title: How to control The Remote Power Unit RPU to reset EVB
created: 2022-May-20
tags:
  - 'permanent/howto'
aliases:
  - Remote reboot bench
---

These steps send from Ignacio
this is the address for [[sjclab-007265]] [http://10.109.2.98/](http://10.109.2.98/)

1.  Log to that IP with user=apc pass=apc
2.  Go to Control -> RPDU
3.  Look for SJCLab-007265 and the serial MB
4.  Check the PC for power cycle/reset
5.  Click on perform the action

## Notes:
[[Ignacio]] report  
```
I can log in now to the RPU but the option for remote power management disappeared. It is not the 1st time that this happens, the RPU site always has issues
```

Related:
- [[ottlab bench remote reboot]]
- [[Remote Power Unit]]
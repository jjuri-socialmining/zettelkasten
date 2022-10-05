---
title: Process intergrate FW,API of CPL,LYNX
created: 2022-May-18
tags:
  - 'permanent/howto'
---

### Intergrate CPL/LYNX FW

1. Step 1: build mode Nightly/release in cpl fw
	- http://sw.inphi-corp.local/jenkins/job/capella/job/capella.firmware/job/capella.application.build/

2. Step 2: Get manual CPL fw to `firmware\application\src\cpl_ip\cpl_app_fw_image.h`

3. Step 3: Build Lynx FW:
	- http://sw.inphi-corp.local/jenkins/job/lynx/job/lynx.firmware/job/lynx.application.build/

### Integrate API/FW
1. 

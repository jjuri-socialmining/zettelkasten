---
title: ZTE change PDV guide
created: 2022-Jun-06
tags:
  - 'permanent/howto'
---


Because this value can't be able hot changed, so we need to update the software.

You can open file and edit register:
`\atsdk\driver\src\implement\codechip\Af70003011\sar\Af70003011SarChannelCommon.c`

in function 
```c
static eAtRet HwInit(AtChannel self)
{
	...
    mChannelHwWrite(self, baseAddr + cAf7Reg_calib_pdv(chnId), 0xA, cAtModuleSar);
}
```

The curent init value is `0xA`. You can adjust the delay by changing the value of below register follow the RTL description, then recompile the software.
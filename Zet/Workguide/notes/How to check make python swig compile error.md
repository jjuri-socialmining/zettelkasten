---
title: How to check make python error
created: 2022-Aug-29
tags:
  - 'permanent/howto'
---
[[swig]]

## Compile 
check error in 
```
<PRODUCT>\api\build-output\python\products\<PRODUCT>\Release\Intermediate\hsc_api.log
```

### [[2022-08-29]]
Content of `hsc_api.log`
```
  hsc_rtos.c
  hsc_api.c
../../hsc_api.c(4030): warning C4244: 'return' : conversion from 'double' to 'hsc_status_t', possible loss of data
  por_dr.c
  hsc_api.h
  hsc_api_wrap.cxx
Release\Intermediate\hsc_api.obj : warning LNK4042: object specified more than once; extras ignored
     Creating library build-output\Release\hsc_api.lib and object build-output\Release\hsc_api.exp
hsc_api_wrap.obj : error LNK2001: unresolved external symbol _lynx_400_dev
hsc_api_wrap.obj : error LNK2001: unresolved external symbol _lynx_dev
build-output\Release\hsc_api.pyd : fatal error LNK1120: 2 unresolved externals
```

should remove the interfaces in `hsc_dev.h`
```c
#define lynx_800_dev lynx_dev
hsc_dev_t* lynx_dev(hsc_dev_t *dev, uint32_t asic_id);
hsc_dev_t* lynx_400_dev(hsc_dev_t *dev, uint32_t asic_id);
```
move to product interface.

[[@2022-11-01]]
```
     Creating library build-output\Release\hsc_api.lib and object build-output\Release\hsc_api.exp
hsc_api_wrap.obj : error LNK2001: unresolved external symbol _cpl_mcu_get_inline_firmware
hsc_api_wrap.obj : error LNK2001: unresolved external symbol _cpl_mcu_verify_image_wrapper
hsc_api_wrap.obj : error LNK2001: unresolved external symbol _cpl_mcu_download_firmware
hsc_api_wrap.obj : error LNK2001: unresolved external symbol _cpl_mcu_direct_download_image_bcast_inline
```
### Jenkins:
If the error happen in Jenkin, check workspace of that job:

example:

http://sw.inphi-corp.local/jenkins/job/porrimadr.capi/job/porrimadr.capi.python.wrapper.win/

![[Pasted image 20220831113040.png]]
Then access the directory of `hsc_api.log` file. Download and check the error log.
[[221102153547 - python compile error]]
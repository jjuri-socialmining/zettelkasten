---
title: swig feature doxygen
created: 2022-Jun-10
tags:
  - 'permanent/howto'
---
up:: [[swig]]

This feture will generate the doxygen comment of function.

http://las-gitlab/hsc/porrima/-/blob/alcor/api/bin/asic_types.i

### Doxygen

```make
$${swig} -doxygen -c++ ${keyword_args} -I. -I$${TOP_DIR}/platform/inc -I$${TOP_DIR} -I$${TOP_DIR}../../ $${defs} -DHSC_HAS_PYTHON -python ${chip_lc}_api.i
```
```
**2022-06-10 16:13:12 GMT+07:00** C:/usr/tools/swig/swig.exe -doxygen -c++ -keyword -I. -I../../platform/inc -I../../. -I../../../../ -DRELEASE_PLATFORM -DHSC_LITTLE_ENDIAN -DHSC_HAS_PYTHON -DHSC_IS_SWIG_BINDING -DHSC_HAS_FILESYSTEM=1 -DHSC_PRODUCT_SPICAP -python hsc_api.i
**2022-06-10 16:13:13 GMT+07:00** ..\..\..\amalgamated\hsc_api.h(921) : Error: Syntax error in input(3).
```
![[Pasted image 20220610164337.png]]
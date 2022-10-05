---
title: Add option for swig compiler
created: 2022-May-20
tags:
  - 'permanent/howto'
---

Go to this file `gen_swig_wrapper.py`

```
${swig} -c++ ${keyword_args} -I. -I$${TOP_DIR}/platform/inc -I$${TOP_DIR}/. -I$${TOP_DIR}/../../ -DRELEASE_PLATFORM -DHSC_LITTLE_ENDIAN -DHSC_HAS_PYTHON -DHSC_IS_SWIG_BINDING -DHSC_HAS_FILESYSTEM=1 $${DEFINES:/%=-%} -python ${chip_lc}_api.i
```




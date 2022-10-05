---
title: Function-like macro
created: 2022-Jun-08
tags:
  - 'permanent/concept'
aliases:
  -
---

```c
#define ARRAY_SIZE(x)  ((unsigned char)(sizeof(x) / sizeof((x)[0])))
#define ARRAY_MASK(x) \
({ \
        int i, mask = 0; \
        for (i = 0; i < ARRAY_SIZE(x); i++) \
            mask |= 1 << x[i]; \
        mask; \ // returned value is result of last operation
})
```




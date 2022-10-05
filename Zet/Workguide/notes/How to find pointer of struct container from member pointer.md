---
title: How to find pointer of struct container from member pointer
created: 2022-Aug-03
tags:
  - 'permanent/howto'
---

```c
/**
 * @ingroup common
 *
 * @brief Return the pointer to parent data data structure of the input pointer.
 *
 * @param ptr Pointer to find parent data structure that it belongs to
 * @param type Data structure type
 * @param member Member that is declared within the data structure
 */
#define TLOG_CONTAINER_OF(ptr, type, member) \
        ((type *)(((uintptr_t)ptr) - ((size_t) &((type *)0)->member)))
```



This will point to member from 0 ~ (&member - &struct) = offset
```c
((size_t) &((type *)0)->member))
```

Then `&struct` = ptr - offset
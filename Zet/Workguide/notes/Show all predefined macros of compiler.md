---
title: Show all predefined macros of compiler
created: 2022-May-18
tags:
  - 'permanent/howto'
---


[[gcc]]

```shell
$ gcc -dM -E  - < /dev/null
#define __DBL_MIN_EXP__ (-1021)
#define __pentiumpro__ 1
#define __UINT_LEAST16_MAX__ 0xffff
#define __ATOMIC_ACQUIRE 2
#define __FLT128_MAX_10_EXP__ 4932
#define __FLT_MIN__ 1.17549435082228750796873653722224568e-38F
#define __GCC_IEC_559_COMPLEX 2
#define __UINT_LEAST8_TYPE__ unsigned char
#define __SIZEOF_FLOAT80__ 12
#define __INTMAX_C(c) c ## LL
#define __CHAR_BIT__ 8
#define __UINT8_MAX__ 0xff
#define __WINT_MAX__ 0xffffffffU
#define __FLT32_MIN_EXP__ (-125)
#define __ORDER_LITTLE_ENDIAN__ 1234
#define __SIZE_MAX__ 0xffffffffU
#define __WCHAR_MAX__ 0xffff
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_1 1
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_2 1
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_4 1
#define __DBL_DENORM_MIN__ ((double)4.94065645841246544176568792868221372e-324L)

$ gcc -dM -E  - < /dev/null | grep __INT
#define __INTMAX_C(c) c ## L
#define __INT8_C(c) c
#define __INT64_C(c) c ## L
#define __INT32_MAX__ 0x7fffffff
#define __INT_FAST32_MAX__ 0x7fffffffffffffffL
#define __INT_FAST16_TYPE__ long int
#define __INT_LEAST32_MAX__ 0x7fffffff
#define __INT_FAST64_TYPE__ long int
#define __INT32_C(c) c
#define __INT_FAST32_TYPE__ long int
#define __INT16_MAX__ 0x7fff
#define __INT8_TYPE__ signed char
#define __INT_LEAST16_TYPE__ short int
#define __INT_FAST16_MAX__ 0x7fffffffffffffffL
```

---
title: Gcc -I option without param
created: 2022-Jun-23
tags:
  - 'permanent/common'
---

[[gcc]]

Gcc -I option without param will cause error undefined

## without param
```shell
dutran@MRVL-quyC4VI9v7 /cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests
$ gcc -Wlogical-op -Wshadow -Wno-unused-parameter -Wno-unused-function -Wno-format-truncation -std=c99 -fdata-sections -fPIC -Wall -ffunction-sections -fmessage-length=0 -g3 -O0 -Werror -fprofile-arcs -ftest-coverage -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../platform/inc -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../inc -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../src/generic -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../src/generic/rules -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../src/impl/spicap -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests    -I/cygdrive/c/Users/dutran/projects/hsc/lynx/libs/inc -I/cygdrive/c/Users/dutran/projects/hsc/lynx/libs/src -I -c -o /cygdrive/c/Users/dutran/projects/hsc/lynx/api/build-output/tests/main.o main.c
/usr/lib/gcc/i686-pc-cygwin/11/../../../../i686-pc-cygwin/bin/ld: /tmp/cc0ka93T.o: in function `main':
/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/main.c:44: undefined reference to `options_parse'
/usr/lib/gcc/i686-pc-cygwin/11/../../../../i686-pc-cygwin/bin/ld: /cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/main.c:47: undefined reference to `inphi_dbg_set_remote_server'
/usr/lib/gcc/i686-pc-cygwin/11/../../../../i686-pc-cygwin/bin/ld: /cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/main.c:55: undefined reference to `inphi_dbg_close'
/usr/lib/gcc/i686-pc-cygwin/11/../../../../i686-pc-cygwin/bin/ld: /tmp/cc0ka93T.o: in function `chip_id':
...

```

## with param
```shell
dutran@MRVL-quyC4VI9v7 /cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests
$ gcc -Wlogical-op -Wshadow -Wno-unused-parameter -Wno-unused-function -Wno-format-truncation -std=c99 -fdata-sections -fPIC -Wall -ffunction-sections -fmessage-length=0 -g3 -O0 -Werror -fprofile-arcs -ftest-coverage -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../platform/inc -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../inc -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../src/generic -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../src/generic/rules -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests/../src/impl/spicap -I/cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests    -I/cygdrive/c/Users/dutran/projects/hsc/lynx/libs/inc -I/cygdrive/c/Users/dutran/projects/hsc/lynx/libs/src -c -o /cygdrive/c/Users/dutran/projects/hsc/lynx/api/build-output/tests/main.o main.c

dutran@MRVL-quyC4VI9v7 /cygdrive/c/Users/dutran/projects/hsc/lynx/api/tests

```


---
title: Use LCOV to coverage function
created: 2022-Jun-16
tags:
  - 'permanent/howto'
---

```
#   git clone https://github.com/linux-test-project/lcov.git
lcov:
    lcov/bin/lcov --capture --directory ./hsc_api.gcda  --output-file coverage.info
    lcov/bin/genhtml coverage.info --output-directory out
```


Related:
- [[How to use gcov to generate coverage report]]
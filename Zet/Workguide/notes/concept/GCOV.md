---
title: GCOV
created: 2022-Jun-10
tags:
  - 'permanent/concept'
aliases:
  -
---

GCOV is used for Analyzing Code Coverage



https://docs.oracle.com/en/operating-systems/oracle-linux/6/porting/ch02s05s01.html


To use Gcov, perform the following steps:

1.  Compile the code with the **-fprofile-arcs** and **-ftest-coverage** flags, for example:
    
    $ **`gcc -fprofile-arcs -ftest-coverage test.c`**
    
    The **-ftest-coverage** flag causes **gcc** to add instrumentation codes to the binary.
    
2.  Run the instrumented binary and perform functional testing.
    
    Running the binary generates profile output. For each source file that you compiled with **-fprofile-arcs**, a `.gcda` profile output file is created in the object file directory.
    
3.  Generate a report file based on the data that is stored in the profile output files:
    
    $ **`gcov test.c`**
    56.0% of 110 source lines executed in file test.c
    Creating test.c.gcov.

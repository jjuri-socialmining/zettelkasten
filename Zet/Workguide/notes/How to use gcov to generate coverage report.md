---
title: How to use gcov to generate coverage report
created: 2022-Jun-16
tags:
  - 'permanent/howto'
---


- `gcc` compile with `-fprofile-arcs -ftest-coverage` every compiled c files will generate `.o` and `.gcno` file
- When the `.out` file was executed, the files `.gcda` will be generated to track the called line/function  coverage.
- use the commaned `gcov -dump main.gcda` to dump info from bin file to readable format `main.c.gcov`
- use `gcovr` to conver `.gcov` file to html `gcovr -r main.c.gcov --html --html-details -o main-coverage.html`


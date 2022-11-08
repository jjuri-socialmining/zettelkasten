---
title: Câu lệnh test và [] trong shell
UID: 221108222653
created: 08-Nov-2022
tags:
  - 'created/2022/Nov/08'
  - 'garden'
  - 'permanent/linking'
aliases:
  - 
publish: False
---
## Notes:
lệnh `test` và `[]` được sử dụng để kiểm tra boolean nhưng lệnh `[]` được sử dụng nhiều hơn.
```shell
# check hello.c file is exist
if test -f hello.c
then
	...
fi
```
hoặc
```shell
# check hello.c file is exist
if [ -f hello.c ]
then
	...
fi
```
sau dấu `[` và trước `]` phải có một khoảng trắng, vì chúng là một lệnh
`then` có thể cùng dòng với `if` và được phân cách bởi một dấu `;`
```shell
if [ -f hello.c ] ; then
	...
fi
```

|                   |                                 |
| ----------------- | ------------------------------- |
| `expr1 -eq expr2` | `True` if 2 exprs are equal     |
| `expr1 -ne expr2` | `True` if 2 exprs are not equal |
| `expr1 -gt expr2` | `True` if expr1 > expr2         |
| `expr1 -ge expr2` | `True` if expr1 >= expr2        |
| `!expr`           | `True` if expr = False          |

## Ideas & thoughts:



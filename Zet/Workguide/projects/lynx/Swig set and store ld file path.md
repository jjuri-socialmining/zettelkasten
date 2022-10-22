---
title: Swig set and store ld file path
created: 2022-Sep-20
tags:
  - 'issue/todo'
project: TBD
date:
  - start: 2022-09-20
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Issues list]]
```c
hsc_mcu_log_ld_file_set(mcu, char *ld_path)
	mcu.ld_path = ld_path

hsc_mcu_log_ld_file_get(mcu)
	return mcu.ld_path
```

string from python pass to c. If that string do not keep that path, c won't work properly

mcu store ld_path reference from user (python)
`hsc_api_wrap.cxx`

![[20220920160811 ~ ld path set.png]]

https://docs.python.org/2/c-api/string.html#c.PyString_AsString
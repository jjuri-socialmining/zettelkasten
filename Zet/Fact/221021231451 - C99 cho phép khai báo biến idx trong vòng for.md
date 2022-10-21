---
title: C99 cho phép khai báo biến idx trong vòng for
UID: 221021231451
created: 21-Oct-2022
tags:
  - 'created/2022/Oct/21'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221021231451'
publish: False
---
## Notes:
[[C99 Standard|C99]] cho phép khai báo biến idx trong vòng for

```c
for (int i = 0; i < 10, i++)
{

}
```

[[C89 Standard]] chưa hỗ trợ cú pháp này.

## Source:
up:: [[Advanced C Programming Course]], section 1

## Relate:

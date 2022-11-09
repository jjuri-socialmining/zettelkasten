---
title: Đọc các tham số truyền vào bash script
UID: 221109205718
created: 09-Nov-2022
tags:
  - 'created/2022/Nov/09'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221109205718'
publish: False
---
## Notes:
Đọc các tham số truyền vào bash script bằng `$*`

hello.sh
```bash
#!bash
echo "hello $*"
```

./hello.sh
```
$ hello.sh VN Uc USA
Hello VN Uc USA
```

source:: [[@ Mokhtar, Mastering Linux shell scripting a practical guide to Linux command-line]], Chap 1

## Relate:

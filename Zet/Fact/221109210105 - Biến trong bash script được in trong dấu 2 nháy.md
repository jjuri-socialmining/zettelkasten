---
title: Biến trong bash script được in trong dấu 2 nháy
UID: 221109210105
created: 09-Nov-2022
tags:
  - 'created/2022/Nov/09'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221109210105'
publish: False
---
## Notes:
Biến trong bash script được in trong dấu 2 nháy `echo "$1"`
```bash
$ echo "$USER earn $1"
linux earn
$ echo '$USER earn $1'
$USER earn $1
$ echo "$USER earn \$1"
linux earn $1
```
source:: [[@ Mokhtar, Mastering Linux shell scripting a practical guide to Linux command-line]], Chap

## Relate:

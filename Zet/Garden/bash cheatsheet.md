---
title: bash cheatsheet
UID: 221109210458
created: 09-Nov-2022
tags:
  - 'created/2022/Nov/09'
  - 'garden'
  - 'permanent/linking'
aliases:
  - 
publish: False
---
## Notes:
![[221109205347 - Đọc return của bash script bằng $#Notes:]]
![[221109205718 - Đọc các tham số truyền vào bash script#Notes:]]
![[221109210105 - Biến trong bash script được in trong dấu 2 nháy#Notes:]]

## Script name
In tên của script file
$HOME/bin/hello2.sh
```bash
#!/bin/bash
echo "You are using $0"
echo "hello $*"
exit 0
```
Run the script
```bash
$ hello.sh VN
You are using /home/linux/bin/hello2.sh
hello VN
```
Nếu chỉ muốn in tên file, không cần in đường dẫn, chỉ cần dùng cú pháp `basename`
`echo "You are using $(basename $0)"`
run script
```bash
$ hello.sh VN
You are using hello2.sh
hello VN
```

 cú pháp `$( )` tương đương với ` `` `
 
## Ideas & thoughts:



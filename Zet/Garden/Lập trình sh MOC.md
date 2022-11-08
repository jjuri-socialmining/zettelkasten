---
title: Lập trình sh MOC
UID: 221108221047
created: 08-Nov-2022
tags:
  - 'created/2022/Nov/08'
  - 'garden'
  - 'permanent/linking'
aliases:
  - 
publish: False
---
up:: [[sh programing|sh]]
## Notes:
- Biến
- Điều kiện
- Danh sách
- Hàm
- Các lệnh nội tại của sh
- Lấy kết quả trả về của một lệnh

`$1`, `$2`, ... vị trí và nội dung của các tham số trên dòng lệnh
`$@` Danh sách các tham số được chuyển thành chuỗi

```shell
$ IFS="^"
$ set foo bar bam
$ echo "$@"
foo bar bam
$ echo "$*"
foo^bar^bam
$ unset IFS
$ echo "$*"
foo bar bam
```

[[Câu lệnh test và [] trong shell]]

## Ideas & thoughts:



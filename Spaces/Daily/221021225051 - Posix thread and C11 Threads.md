---
title: what difference between pthread and threads.h
UID: 221021225051
created: 21-Oct-2022
tags:
  - 'created/2022/Oct/21'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221021225051'
publish: False
---
## Notes:
[[C Programming]] đã hỗ trợ multithreading hàng thập kỷ nhưng thư viện C threading lại không được chuẩn hóa, non-standard -> non-portable.

[[C11 Standard]] khắc phục bằng cách định nghĩa thư viện chuẩn [[threads.h]], hay còn được gọi là [[C11 Thread]]. Trước đó, thư viện multithreading phổ biến được sử dụng là [[Posix Thread]]

## Source:
up:: [[Advanced C Programming Course]], section 1
[[❓221022-0819 - What is posix threads and C11 threads]]
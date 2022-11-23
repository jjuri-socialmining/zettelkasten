---
title: Watchdog timer là một phần tử ngoại vi giám sát chương trình
UID: 221123201921
created: 23-Nov-2022
tags:
  - 'created/2022/Nov/23'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221123201921'
publish: False
---
## Notes:
[[Watchdog Timer]] là một phần tử bên ngoài chương trình giúp giám sát chương trình. Ví dụ chương trình là một người bảo vệ được thuê về để canh gác ngân hàng. 

Nhưng sẽ xảy ra trường hợp người bảo vệ ngủ gật, và bị trộm đột nhập. Chính vì thế, để đảm bảo người bảo vệ (chương trình) vẫn đang hoạt động bình thường, người ta thuê thêm một con chó. Giúp giám sát chương trình. 

Mỗi khi con chó được cho ăn thì nó sẽ khởi động lại bộ đếm 1,2,3... tới N (N thời gian timeout, hay hiểu nôm na là thời điểm con chó đói). Nếu tới N mà nó không được cho ăn, nó sẽ thấy có gì bất thường và sủa (reset chương trình) để đánh thức người bảo vệ.

source:: [[Microcontrollers and the C Programming Language (MSP430)]] Udemy course

## Relate:

---
title: Có tối đa 4 phân vùng Primary partition, điều này có còn đúng
tags:
  - 'created/2022/Nov/08'
  - 'tasks/done'
---

## Notes:
Trong [[@ Nguyễn Phương Lan, Lập trình Linux]], Ổ cứng có tối đa 4 phân vùng Primary partition để cài đặt hệ điều hành, điều này có còn đúng không?

- Điều này hoàn toàn đúng, giới hạn này do [[Master Boot Record (MBR)]] chỉ chứa 4 entry lưu phân vùng ổ cứng

- Để khắc phục nhược điểm này, [[GUID Partition Table (GPT)]] ra đời với giới hạn tăng lên 128 primary partition

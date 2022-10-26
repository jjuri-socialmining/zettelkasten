---
title: Step by step to use Shared memory between 2 processes
UID: 221025231549
created: 25-Oct-2022
tags:
  - 'created/2022/Oct/25'
  - 'howto'
aliases:
  - 
publish: False
---
## Notes:
Step by step to use (up:: [[Shared Memory]]) between 2 processes
- Create new or use exist the shared memory segment by `shmget()`
- attach the process to created shared memory `shmat()`
- detach process from shared memory `shmdt()`
- control operation on shared memory `shmctl()`

## Ideas & thoughts:

## Related:
- Xem thêm các bước sử dụng [[Message Queues]] -> [[Step by step to perform communication using Message Queues between 2 processes]]


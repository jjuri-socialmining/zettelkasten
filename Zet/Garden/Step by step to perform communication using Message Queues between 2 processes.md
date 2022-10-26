---
title: Step by step to perform communication using Message Queues between 2 processes
UID: 221025230659
created: 25-Oct-2022
tags:
  - 'created/2022/Oct/25'
  - 'howto'
aliases:
  - 
publish: False
---
## Notes:
Step by step to perform communication using (up:: [[Message Queues]]) between 2 processes
- Generate unique key: `ftok()`
- Create new or connect exist message queues `msgget()`
- Write into message queues `msgsnd()`
- read from message queues `msgrcv()`
- Control operations on MQ `msgctl()`
---
title: 2 process có thể giao tiếp với nhau bằng nhiều cách thức
UID: 221025230213
created: 25-Oct-2022
tags:
  - 'created/2022/Oct/25'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221025230213'
publish: False
---
## Notes:
- pipes (same process) -> first process communicate with second process (half duplex)
	- Parent/childs/grand childs
- [[Named Pipes]] (difference processes, FIFO) (full duplex)
- [[Message Queues]] (fullduplex)
- [[Shared Memory]]
- [[Socket programming|Socket]]: mostly used to Communicate over network between client and server
- [[signal() func]]

source:: [[Advanced C Programming Course]], Section 20

## Relate:

---
title: ODSP - IPC over Ring Buffer
created: 2022-Oct-26
tags:
  - 'permanent/common/source'
publish: False
---

- https://ewiki.marvell.com/display/ODSP/IPC+over+ring+buffer
- ![[ODSP-IPCoverringbuffer-261022-0039-124.pdf]]
```
Due to Security reason, Hardware Mailbox and the ability to access to hardware registers may be cut-off, only access to shared memory is allowed from the C-API layer.
```

> [!INFO]- Ringbuffer
> This page is to introduce new communication between API and Firmware in an Object Oriented way via Shared memory. The Shared memory can be:
> - Scratch Memory
> - Buffer in DRAM
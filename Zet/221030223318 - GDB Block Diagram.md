---
title: GDB Block Diagram
UID: 221030223318
created: 30-Oct-2022
tags:
  - 'created/2022/Oct/30'
  - 'garden'
  - 'permanent/concept'
aliases: '221030223318'
publish: False
---
previous:: [[$ 221029 - Mô tả cách gdb hoạt động để debug trên code c 🔎]]
source:: [[@ aosabook.org, The Architecture of Open Source Applications (Volume 2) GDB]]

## Notes:
![[20221030090022 ~ GDB Structure.png]]

Theo structure ở trên: GDB được chia thành symbol side và target side
- Symbol side : CLI, [[BFD Library]], COFF, ELF DWARF
- Targe side: Execution control, Stackframe, Arch support
	- Target vector: Linux native, execute table, [[gdb corefile]], remote protocol

GDB interface:
- [[CLI]]
- [[GDB Machine Interface (MI)]]
- 
## Relate:

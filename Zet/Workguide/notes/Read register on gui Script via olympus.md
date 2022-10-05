---
title: Read register on gui Script via olympus
created: 2022-Mar-23
tags:
  - 'permanent/howto'
---

# Read register on gui Script via olympus

[[spica+]]

```
# Example for SPICA PLUS
# Read remap.c
# mb mainboard id, check GUI
# devtype = address(0x1e4831) >> 16 = 0x1e
# die 0 -> phy 0, die 1 -> phy = 0x10

import Olympus
print("%x" % Olympus.rd(mb=1593, address=0x1e4831, bus=0, phy=0x10, devtype=0x1e))

```

![[20220323120044 ~ olympus lib.png]]

![[Pasted image 20220323115733.png]]
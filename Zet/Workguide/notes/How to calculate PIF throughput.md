---
title: How to calculate PIF throughput
created: 2022-Jun-29
tags:
  - 'permanent/howto'
---

Sample code on PLR, ref from [[Tiny logger|tlog]] document.

simple loop to repeatedly fetch 2048 bytes on GUI:

```python
import plr_api as api
import time

start_addr = 0x5ff80000
nb_words = 512
repeat = 50
die = inphi_gui_get_current_die()

words = api.new_uint32arr(nb_words)
start = time.time()
for _ in range(repeat):
    api.plr_mcu_pif_read(die, start_addr, words, nb_words)
elapsed = time.time() - start

nb_bytes = nb_words * repeat * 4
bps = int(nb_bytes / elapsed)
print "{:.1f}KBps".format(bps / 1000.0)
```


Related:
- [[PIF]]
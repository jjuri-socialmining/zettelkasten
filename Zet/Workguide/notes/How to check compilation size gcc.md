---
title: How to check compilation size gcc
created: 2022-May-25
tags:
  - 'permanent/howto'
---


```shell
$ size example.exe
   text    data     bss     dec     hex filename
 601965    2480   66000  670445   a3aed example.exe

$ size --format=sysv example.exe
example.exe  :
section             size      addr
.text             295844   4198400
.data                224   4497408
.rdata            242728   4501504
.buildid              53   4747264
.eh_frame          52808   4751360
.bss               66000   4804608
.idata              1000   4874240
.rsrc               1256   4878336
.reloc             10532   4882432
.debug_aranges       408   4894720
.debug_info        27672   4898816
.debug_abbrev       3540   4927488
.debug_line         2229   4931584
.debug_frame          56   4935680
.debug_str           202   4939776
.debug_line_str     5807   4943872
.debug_loclists      255   4952064
Total             710614
```

- ‘text’ contain: function, constant.
- The ‘bss’ contains all the uninitalized data.
- ‘data’ is used for **initialized data**. This is best explained with the following (global/extern) variable:
	- `int32_t` `myVar = 0x12345678;`
- dec = text + data + bss


## Reference:
- [text-data-and-bss](https://mcuoneclipse.com/2013/04/14/text-data-and-bss-code-and-data-size-explained/)
- [[Inphi gen file size report]]

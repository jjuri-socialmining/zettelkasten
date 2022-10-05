---
title: Xbar PG4 imlement note
created: 2022-May-30
tags:
  - 'permanent/fact'
---

```c

SPICA_FOR_CHANNEL_IN_BUNDLE(die, bundle_idx, SPICA_INTF_STX)
{
	// The Rx channel to select as a source
	src_ch = rules->stx_xbar_src_chan[channel][0];
	if((src_ch == 0) || (src_ch >= 0xf))
	{
		src_inst = 0xf;
	}
	else
	{
		// NOTE: Rebases package channel to FW channel (What the register requires)
		src_inst = spica_get_die_inst_from_pkg_ch(die, src_ch, src_intf);
		if (src_intf == SPICA_INTF_SRX) 
		{
			src_inst -= (src_inst)/3; // To remap {0,1,3,4,6,7,9,10} -> {0,1,2,3,4,5,6,7}
		}
	}

	src_clk_ch = rules->stx_clk_xbar[channel];
	if((src_clk_ch == 0) || (src_clk_ch >= 0xf)) // out of range
	{
	   src_clk_inst = 0xf;
	}
	else
	{
		src_clk_inst = spica_get_die_inst_from_pkg_ch(die, src_clk_ch, src_intf);
		if (src_intf == SPICA_INTF_SRX) 
		{
			src_clk_inst -= (src_clk_inst)/3; // To remap {0,1,3,4,6,7,9,10} -> {0,1,2,3,4,5,6,7}
		}
	}
	SPICA_STX_CLK_XBAR__SRC_CHANNEL__RMW(die, channel, src_clk_inst);

	//INPHI_NOTE("STX ch%d src_ch=%d, src_ch_interleave=%d\n", channel, src_ch, rules->stx_xbar_src_chan[channel][1]);
	SPICA_STX_XBAR__SRC_CHANNEL__RMW(die, channel, src_inst);

	// The sub-channel interleave to select within the selected Rx channel
	// The offset value is already zero based, no need to rebase
	SPICA_STX_XBAR__SRC_CHANNEL_INTERLEAVE__RMW(die, channel, rules->stx_xbar_src_chan[channel][1]);
}
```

KP8-KP4

Run by CAPI
![[Pasted image 20220530162954.png]]

Run by PG4
![[Pasted image 20220530163106.png]]


```python
import spica_registers as creg
die = __regdb__.get_current_die()

for channel in range(1, 9):
    print("STX chn id %d" % channel)
    print(" - src id    = %x" % creg.SPICA_STX_XBAR__SRC_CHANNEL__READ(die, channel))
    print(" - inteleave = %x" % creg.SPICA_STX_XBAR__SRC_CHANNEL_INTERLEAVE__READ(die, channel))
    print(" - clk       = %x" % creg.SPICA_STX_CLK_XBAR__SRC_CHANNEL__READ(die, channel))


for channel in range(1, 5):
    print("OTX chn id %d" % channel)
    print(" - src id 0  = %x" % creg.SPICA_OTX_XBAR__SRC_CHANNEL_0__READ(die, channel))
    print(" - src id 1  = %x" % creg.SPICA_OTX_XBAR__SRC_CHANNEL_1__READ(die, channel))
    print(" - src id 2  = %x" % creg.SPICA_OTX_XBAR__SRC_CHANNEL_2__READ(die, channel))
    print(" - src id 3  = %x" % creg.SPICA_OTX_XBAR__SRC_CHANNEL_3__READ(die, channel))
    print(" - clk       = %x" % creg.SPICA_OTX_CLK_XBAR__SRC_CHANNEL__READ(die, channel))
```

Log Good
```
STX chn id 1
 - src id    = 3
 - inteleave = 0
 - clk       = 3
STX chn id 2
 - src id    = 3
 - inteleave = 1
 - clk       = 3
STX chn id 3
 - src id    = 2
 - inteleave = 0
 - clk       = 2
STX chn id 4
 - src id    = 2
 - inteleave = 1
 - clk       = 2
STX chn id 5
 - src id    = 1
 - inteleave = 0
 - clk       = 1
STX chn id 6
 - src id    = 1
 - inteleave = 1
 - clk       = 1
STX chn id 7
 - src id    = 0
 - inteleave = 0
 - clk       = 0
STX chn id 8
 - src id    = 0
 - inteleave = 1
 - clk       = 0
OTX chn id 1
 - src id 0  = 0
 - src id 1  = 1
 - src id 2  = f
 - src id 3  = f
 - clk       = 0
OTX chn id 2
 - src id 0  = 2
 - src id 1  = 3
 - src id 2  = f
 - src id 3  = f
 - clk       = 2
OTX chn id 3
 - src id 0  = 4
 - src id 1  = 5
 - src id 2  = f
 - src id 3  = f
 - clk       = 4
OTX chn id 4
 - src id 0  = 6
 - src id 1  = 7
 - src id 2  = f
 - src id 3  = f
 - clk       = 6


Summary
=======
 register reads = 44
 register writes = 0
 duration (ms)   = 143
```


Fail log
```
STX chn id 1
 - src id    = 3
 - inteleave = 0
 - clk       = 3
STX chn id 2
 - src id    = 3
 - inteleave = 1
 - clk       = 3
STX chn id 3
 - src id    = 2
 - inteleave = 0
 - clk       = 2
STX chn id 4
 - src id    = 2
 - inteleave = 1
 - clk       = 2
STX chn id 5
 - src id    = 1
 - inteleave = 0
 - clk       = 1
STX chn id 6
 - src id    = 1
 - inteleave = 1
 - clk       = 1
STX chn id 7
 - src id    = 0
 - inteleave = 0
 - clk       = 0
STX chn id 8
 - src id    = 0
 - inteleave = 1
 - clk       = 0
OTX chn id 1
 - src id 0  = 0
 - src id 1  = f
 - src id 2  = f
 - src id 3  = f
 - clk       = 0
OTX chn id 2
 - src id 0  = 1
 - src id 1  = f
 - src id 2  = f
 - src id 3  = f
 - clk       = 1
OTX chn id 3
 - src id 0  = 2
 - src id 1  = f
 - src id 2  = f
 - src id 3  = f
 - clk       = 2
OTX chn id 4
 - src id 0  = 3
 - src id 1  = f
 - src id 2  = f
 - src id 3  = f
 - clk       = 3


Summary
=======
 register reads = 44
 register writes = 0
 duration (ms)   = 153

```
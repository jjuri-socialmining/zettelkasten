---
title: Issue fail clearing ACK
created: 2022-Sep-27
tags:
  - 'issue/todo'
project: TBD
date:
  - start: 2022-09-27
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Issues list]]

> [!Bob]
> I’ve still got some things to check but in the mean time thought I would ping you.  
I’m working on getting the Lynx400 to self boot from NVM. After asserting the Reset_N and Self_init lines, I see no data on any of the 1.8v SPI lines and the MCU gives me the error: “Failed Clearing the chip ACK”  
At this point the SPI bus is released for the lynx400 to be the master and I have taken out the code where our uP drives the CS.  
Any suggestions?
When you get a chance let me know what define the lynx400 needs to have modified in the lynx800 API per todays meeting please.



```c
// example_init_112p5g_prbs_broadcast.c
// Broadcast clear any request bits in the event a previous configuration
// was done. The firmware won't clear these bits in self-config mode if
// the SELF_TEST.QUERY_RULES bit is set
```


```c
// cpl_top.c
// Clear the ACK bit if the request line goes low
else if((!chip_init_req) && chip_init_ack)
{
	log_debug("Clearing all top level ACK\n");

	chip_init = false;
	//pll_init = false;

	for(int ch = 0; ch < 2; ch++)
	{
		cpl_tx_rules_t* tx_rules = query_tx_rules(ch);
		tx_rules->enable = false;

		cpl_rx_rules_t* rx_rules = query_rx_rules(ch);
		rx_rules->enable = false;

		rx_set_active_channel(ch, false);
		tx_set_active_channel(ch, false);
	}

	// Clear the per-channel ACKs
	CPL_CHANNEL_INIT_ACK__WRITE(0);
	CPL_TOP_INIT_ACK__WRITE(0);
	continue;
}
```
---
title: Prbs total bit count
created: 2022-Aug-02
tags:
  - 'permanent/concept'
aliases:
  -
---

DP_CHK_PRBS_CFG

![[Pasted image 20220802163849.png]]

> Enables separate PRBS checking on even and odd bits (PAM4 MSB and LSB) of the parallel data from the SerDes. When 0, a single PRBS stream is expected. When this is set the DP_CHK_WORD_CNT status is in 128-bit words, when it is cleared the DP_CHK_WORD_CNT status is in 64-bit words.

Logic on [[spica+]]

```c
// spica_prbs_chk_config
uint16_t dual_prbs;

/* Force dual PRBS mode to false when signalling is NRZ */
if (chk_rules->nrz_mode)
{
	dual_prbs = false;
}
else
{
	dual_prbs = (chk_rules->prbs_mode != SPICA_PRBS_MODE_COMBINED);
}

data = SPICA_VAL(SPICA_SRX_RXD_DP_CHK_PRBS_CFG__DUAL_PRBS,            dual_prbs                                                             ) |
	   SPICA_VAL(SPICA_SRX_RXD_DP_CHK_PRBS_CFG__AUTO_POLARITY_THRESH, chk_rules->auto_polarity_thresh                                       ) |
	   SPICA_VAL(SPICA_SRX_RXD_DP_CHK_PRBS_CFG__AUTO_POLARITY_EN,     chk_rules->auto_polarity_en                                           ) |
	   SPICA_VAL(SPICA_SRX_RXD_DP_CHK_PRBS_CFG__PRBS_INV,             chk_rules->prbs_inv                                                   ) |
	   SPICA_VAL(SPICA_SRX_RXD_DP_CHK_PRBS_CFG__PRBS_MODE_ODD,        spica_prbs_get_hdwr_pat((e_spica_prbs_pat)chk_rules->prbs_pattern_lsb)) |
	   SPICA_VAL(SPICA_SRX_RXD_DP_CHK_PRBS_CFG__PRBS_MODE,
	spica_prbs_get_hdwr_pat((e_spica_prbs_pat)chk_rules->prbs_pattern)    );
spica_reg_channel_write(die, channel, SPICA_SRX_RXD_DP_CHK_PRBS_CFG__ADDRESS+chk_offset, data);

```

```c
// spica_prbs_chk_status
data = spica_reg_channel_read(die, channel, SPICA_SRX_RXD_DP_CHK_WORD_CNT0__ADDRESS+chk_offset);
word_count = (uint64_t)data;
data = spica_reg_channel_read(die, channel, SPICA_SRX_RXD_DP_CHK_WORD_CNT1__ADDRESS+chk_offset);
word_count += (((uint64_t)data) << 16);
data = spica_reg_channel_read(die, channel, SPICA_SRX_RXD_DP_CHK_WORD_CNT2__ADDRESS+chk_offset);
word_count += (((uint64_t)data) << 32);

/* Convert the word count to a cycle count */
chk_status->prbs_total_bit_count = ((uint64_t)(word_count) * 128);
```
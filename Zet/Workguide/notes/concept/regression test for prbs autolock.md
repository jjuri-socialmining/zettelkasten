---
title: regression test for prbs autolock
created: 2022-Sep-06
tags:
  - 'permanent/concept'
aliases:
  -
---
up:: [[HSC Regression test]]

```
Gen rules = CapellaPrbsGenRules(mode='COMBINED', enable=True, pattern={'msb': 'PRBS31', 'lsb': 'PRBS31'}, prbs_pat_mode='PRBS')
Chk rules = HscApiPrbsChkRules(mode='COMBINED', enable=True, autolock=True, pattern={'msb': 'PRBS23', 'lsb': 'PRBS23'})
[2022-09-02 17:24]-CRITICAL [CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
```

Configure source prbs gen
```c
    if (CPL_INTF_SERIAL_TX == intf)
    {
        if (gen_rules->en == false)
        {
            //INPHI_NOTE("Turning OFF the %s PRBS generator for Die=%x Channel=%d\n", label, die, channel);
            CPL_TX_TXD_CLKEN__GEN__RMW(die, channel, 0);
            CPL_TX_TXD_GEN_CFG__WRITE(die, channel, 0);
        }
        else
        {
            //INPHI_NOTE("Turning ON the %s PRBS generator for Die=%x Channel=%d\n", label, die, channel);
            CPL_TX_TXD_CLKEN__GEN__RMW(die, channel, 1);

            // Put the generator in reset when the configuration is being changed
            CPL_TX_TXD_RESET__GEN__RMW(die, channel, 1);
```
The reset will make interrupt a moment, need to wait FW_LOCK before configuring rx_checker at receive side
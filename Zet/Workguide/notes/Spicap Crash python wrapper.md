# Spicap Crash python wrapper

[SPICSW-242](https://essjira.marvell.com/browse/SPICSW-242)
[SPICSW-333](https://essjira.marvell.com/browse/SPICSW-333)

API 1.0.0.720
Risky code
```
	// Done at end since we need to know the LRX signalling type  
    // The los_a/dsrt_rules are top level but overlays are per-channel  
    data = SPICA_ORX_LOS_RULES__READ(bdie, 1);  
    uint16_t lrx_los_dsrt_startup_dac = SPICA_ORX_LOS_RULES__LOS_DSRT_CTRL__GET(data);  
    uint16_t lrx_los_asrt_startup_dac = SPICA_ORX_LOS_RULES__LOS_ASRT_CTRL__GET(data);

    for(int i=0; i<SPICA_LOS_CTRL_AMP_MAX; i++)  
	{         
		if(lrx_los_dsrt_startup_dac  == los_ctrl_amp_thresholds_dsrt[rules->orx[1].signalling][i]) rules->lrx_los_dsrt_ctrl_startup  = i;         
		if(lrx_los_asrt_startup_dac  == los_ctrl_amp_thresholds_asrt[rules->orx[1].signalling][i]) rules->lrx_los_asrt_ctrl_startup  = i;     
	}
```

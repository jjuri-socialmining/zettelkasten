---
title: Demap value combine from conditions
created: 2022-Aug-23
tags:
  - 'permanent/common'
---

Demap value are different when apply bundle and prbs is not locked in combine mode, it is only locked in msb/lsb
![[Pasted image 20220823102040.png]]

![[Pasted image 20220823102221.png]]


```c

inphi_status_t rx_pmd_dsp_set_demap_polarity(
    channel_t*      ch,
    cpl_rx_rules_t* rules,
    bool flip)
{
    inphi_status_t status = INPHI_OK;

    uint32_t channel = ch->channel;
    e_sw_intf   intf = ch->intf;

    uint16_t demap_val = 0x1b;
    e_pkr_an_states an_state = pkr_an_fsm_get_an_state(channel, intf);

    bool invert_channel = rules->invert_chan;
    if (flip) invert_channel = !invert_channel;

    if ((rules->signalling == SIGNAL_MODE_NRZ) ||
        ((an_state > STATE_AN_IDLE) && (an_state < STATE_AN_ACK_DETECT))/* ||
        (an_state == STATE_AN_TRAIN_ACK_INIT)*/)
    {
        if (invert_channel)
        {
            demap_val = 0xf0; // 11 xx xx 00
        }
        else
        {
            demap_val = 0x0f; // 00 xx xx 11
        }
    }
    else if (invert_channel)
    {
        if (rules->gray_mapping)
        {
            //precoder is on&&polarity inverted
            if ( ((rules->dsp_mode == DSP_MODE_DFE1) ||
                  (rules->dsp_mode == DSP_MODE_DFE1_RC_DFE2))
                    &&
                  (rules->dfe_precoder_en) )
            {
                if (rules->ieee_demap)
                {
                    demap_val = 0xe1; //// 11100001
                }
                else
                {
                    demap_val = 0xd2; //// 11010010
                }
            }
            else
            {
                if (rules->ieee_demap)
                {
                    demap_val = 0x78;
                }
                else
                {
                    demap_val = 0xb4; //// 10110100
                }
            }
        }
        else {
            //precoder is on&&polarity inverted
            if ( ((rules->dsp_mode == DSP_MODE_DFE1) ||
                  (rules->dsp_mode == DSP_MODE_DFE1_RC_DFE2))
                    && 
                  (rules->dfe_precoder_en) )
            {
                if (rules->ieee_demap)
                {
                    demap_val = 0x63; //// 01100011
                }
                else
                {
                    demap_val = 0x93; //// 10010011
                }
            }
            else {
                if (rules->ieee_demap)
                {
                    demap_val = 0xd8;
                }
                else
                {
                    demap_val = 0xe4; //// 11100100
                }
            }
        }
    }
    else {
        if (rules->gray_mapping)
        {
            if (rules->ieee_demap)
            {
                demap_val = 0x2d;
            }
            else
            {
                demap_val = 0x1e; //// 00011110
            }
        }
        else
        {
            if (rules->ieee_demap)
            {
                demap_val = 0x27; //// 00011011
            }
            else
            {
                demap_val = 0x1b; //// 00011011
            }
        }
    }

    CPL_RX_DSP_PAM4_DEMAP_CFG__WRITE(channel, demap_val);

    return status;
}
```

![[20220823105136 ~ aThang Ieee demap issue.png]]

### Personal notes
- [[Tìm hiểu các mã khác ngoài gray]]
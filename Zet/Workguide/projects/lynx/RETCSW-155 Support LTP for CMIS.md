---
title: RETCSW-155 Support LTP for CMIS
created: 2022-May-18
tags:
  - 'tasks/done'
project: Lynx
start: 2022-05-18
end: 'TBD'
---
up:: [[Tasks list]]

![[LTP.png]]

LTP feature seem like SNR feature, it need to check continously

LTP is [[Level Transition Parameter]]

## Step to do:
- [x] Update CPL FW to support `lrx_ltp_check`, `lrx_compute_ltp`. Store ltp value in overlay
	- [x] Build CPL B FW
- [x] Integrate CPL FW to LYNX FW
	- [x] make -f build.inc fetch_cpl_fw
	- [x] Build Lynx FW
		- http://sw/~swott-jenkins/projects/lynx/firmware/application/nightly/LYNX_NIGHTLY_488/
- [x] Add API to read LTP in lynx API
	- `hsc_chn_rx_dsp_ltp_read()`
- [x] Test FW ✅ 2022-09-21
	- [ ] Soft reset clear register LTP
	- [ ] Add more register	
	- [ ] Check why hist_bin = 0
http://sw/~swott-jenkins/projects/capella/firmware/application/b/nightly/CAPELLAB_NIGHTLY_2355/

http://sw/~swott-jenkins/projects/porrima/api/nightly/1.5.1870/src/amalgamated/por_api.c

## Porima
Ref from repo: `http://las-gitlab/hsc/porrima`

`firmware\application\src\lrx_fw.c`

```c
inphi_status_t lrx_ltp_check(int channel)
inphi_status_t lrx_compute_ltp(int channel, uint32_t hist_bins[160], uint8_t slicer_bins[7])
```

Some infor get from FW
```c
lrx_hist_fsm_t* lrx_hist_fsm = get_lrx_hist_fsm();

status |= lrx_compute_ltp(channel, lrx_hist_fsm->hist_bins, lrx_hist_fsm->slicer_bins);
```

## Capella
```c
static void rx_qc_histogram_check(uint16_t        channel,
                                  e_rx_qc_mode    qc_mode,
                                  cpl_rx_rules_t* rx_rules)

static bool compute_histogram_quality(
    uint16_t        channel,
    uint32_t        hist_bins[160],
    uint8_t         slicer_bins[7],
    uint16_t        mse_threshold,
    e_signal_mode   signalling)
```


http://sw.inphi-corp.local/jenkins/job/capella/job/capella.firmware/job/capella.application.build/2339/

## Test log:
Get QC

```python
import ctc_registers as creg
die = inphi_gui_get_current_die()

# CTC Chip ID
print("LO = %x" % creg.CTC_MMD30_DEVICE_ID_LOW__READ(die))
print("HI = %x" % creg.CTC_MMD30_DEVICE_ID_HIGH__READ(die))

rules = cpl_rx_qc_rules_t()
cpl_channel_rx_qc_query(die +3, 0,  rules)
cpl_channel_rx_qc_print(die +3, 0,  rules)

stats = cpl_rx_qc_stats_t()
cpl_rx_qc_stats_query(die +3, 0,  stats)
cpl_rx_qc_stats_print(die +3, 0,  stats)
```

MCU Log

```python
mcuhdl = api.hsc_mcu_t()
api.hsc_dev_mcu(dev, 4, mcuhdl)
status, buff = api.hsc_mcu_log_query(mcuhdl, 10000)
print(buff)

```

http://sw/~swott-jenkins/projects/capella/firmware/application/b/debug/0.12.0.2346/

```
20869196:928:QC:0 rx_quality_check
20869211:929:p_rx_qc_rules->qc_status.bf.snr_done 1
20869232:930:p_rx_qc_rules->qc_status.bf.snr_pass 1
20869252:931:p_rx_qc_rules->qc_status.bf.hist_done 0
20869273:932:qc_mode 1
20869285:933:qc_hist_up_enable 0
20869300:934:qc_hist_dn_enable 0

20869389:928:QC:1 rx_quality_check
20869405:929:p_rx_qc_rules->qc_status.bf.snr_done 1
20869425:930:p_rx_qc_rules->qc_status.bf.snr_pass 1
20869445:931:p_rx_qc_rules->qc_status.bf.hist_done 0
20869466:932:qc_mode 1
20869478:933:qc_hist_up_enable 0
20869493:934:qc_hist_dn_enable 0
```

```c
// fw cpl_rx_qc_command_update
rx_rules->rx_qc.qc_ctrl.bf.hist_up_enable = ((data >> 9) & 1) ? 0 : 1;
rx_rules->rx_qc.qc_ctrl.bf.up_enable      = ((data >> 8) & 1) ? 0 : 1;
rx_rules->rx_qc.qc_ctrl.bf.hist_dn_enable = ((data >> 1) & 1) ? 0 : 1;
rx_rules->rx_qc.qc_ctrl.bf.dn_enable      = ((data     ) & 1) ? 0 : 1;
```

```c
/* QC rules */
data =   (rx_rules->rx_qc.hist_dis           << 9)
	   | (rx_rules->rx_qc.dis                << 8)
	   | (rx_rules->rx_qc.data_mode_hist_dis << 1)
	   | (rx_rules->rx_qc.data_mode_dis          );
CPL_RX_XFER_0__WRITE(die, channel, data);
```

```
20869478:933:qc_hist_up_enable 0
20869493:934:qc_hist_dn_enable 0
->
rx_rules->rx_qc.qc_ctrl.bf.hist_up_enable = false
rx_rules->rx_qc.qc_ctrl.bf.hist_dn_enable = false
->
hist_dis
data_mode_hist_dis
```


```c

    if (rx_rules->rx_qc.qc_ctrl.bf.up_enable == 0)
    {
        rx_rules->rx_qc.qc_ctrl.bf.hist_up_enable = 0;
        rx_rules->rx_qc.qc_ctrl.bf.dn_enable = 0;
    }

    if (rx_rules->rx_qc.qc_ctrl.bf.dn_enable == 0)
    {
        rx_rules->rx_qc.qc_ctrl.bf.hist_dn_enable = 0;
    }

	// if PAM, his up/dn disabled
    if (rx_rules->signalling == SIGNAL_MODE_PAM)
    {
        rx_rules->rx_qc.qc_ctrl.bf.hist_up_enable = 0;
        rx_rules->rx_qc.qc_ctrl.bf.hist_dn_enable = 0;
    }
```

NRZ mode ![[qc_ltp.py]]
```log
20192156:928:QC:1 rx_quality_check

20192172:929:p_rx_qc_rules->qc_status.bf.snr_done 1

20192192:930:p_rx_qc_rules->qc_status.bf.snr_pass 1

20192212:931:p_rx_qc_rules->qc_status.bf.hist_done 0

20192233:932:qc_mode 1

20192245:933:qc_hist_up_enable 0

20192260:934:qc_hist_dn_enable 1

20192275:943:QC:1 rx_qc_histogram_check

20192309:731:QC:1 pending: ready=0 lane_req=0 user=2
```

## [[2022-05-19]]
```
ne may reg a dang dung cho AEC la dc
master(CPL) + submodule ANLT

- CPL_RX_TOP_SCRATCH7__READ
- CPL_RX_TOP_SCRATCH6__WRITE
- CPL_RX_TOP_SCRATCH4__READ
- CPL_RX_TOP_SCRATCH2__READ
- CPL_RX_TOP_SCRATCH1__READ

- CPL_TX_TOP_SCRATCH5__READ
- CPL_TX_TOP_SCRATCH3__READ
- CPL_RX_PLL_SCRATCH7__WRITE (0-7)
```

- [x] Define Scratch reg in register browser cplb
	- `users/dutran/cpl_ltp`
	- `RX_RXA_SCRATCH4` -> `RX_LTP`
```shell
python register_browser.py 
No module named twisted.internet
```

```shell
# install pip for local user
pip install pathlib --user
```

## [[2022-05-20]]

## Related
- [[Process intergrate FW,API of CPL,LYNX]]
- [[16.8 fixed point]]

DC5 server
```
which gcc && gcc --version | head -n1 && gcc --std=c99 -Wall -Wextra -Wlogical-op -Wshadow -Werror -Wno-unused-parameter -Wno-unused-function -Wformat=2 -O2 -I . -I ../ucode -I platform/inc -I products/lynx   -DHSC_PRODUCT_LYNX_800 -o example platform/src/hsc_rtos.c products/lynx/ctc_def.c products/lynx/lynx.c products/lynx/lynx_400.c hsc_api.c main.c -lm
/bin/gcc
gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44.0.3)
make[1]: Leaving directory `/home/dutran/projects/hsc/lynx/api/build-output/amalgamated'
touch build-output/events/amalgamated

```

Jenkins server
```
which gcc && gcc --version | head -n1 && gcc --std=c99 -Wall -Wextra -Wlogical-op -Wshadow -Werror -Wno-unused-parameter -Wno-unused-function -Wformat=2 -O2 -I . -I ../ucode -I platform/inc -I products/lynx   -DHSC_PRODUCT_LYNX_400 -o example platform/src/hsc_rtos.c products/lynx/ctc_def.c products/lynx/lynx.c products/lynx/lynx_400.c hsc_api.c main.c -lm
**2022-05-20 14:10:13 GMT+07:00** /tools/swott/rh7/gcc/latest/bin/gcc
**2022-05-20 14:10:13 GMT+07:00** gcc (GCC) 4.8.3
**2022-05-20 14:10:13 GMT+07:00** products/lynx/ctc_def.c: In function 'dsp_ltp_get':
**2022-05-20 14:10:13 GMT+07:00** products/lynx/ctc_def.c:36106:20: error: 'INFINITY' undeclared (first use in this function)
**2022-05-20 14:10:13 GMT+07:00**              *ltp = INFINITY;
```

```python
# Import register and API
from lynx_400.python import lynx_400_registers as creg
from lynx_400.python import hsc_api as capi

# Get number of die on this device over API
dev = capi.hsc_dev_t()
capi.hsc_dev(dev, 0)
num_dies = capi.hsc_dev_num_dies(dev)

chn = capi.hsc_chn_t()

capi.hsc_dev_chn(dev, 0, capi.HSC_INTF_HRX, chn)
status, ltp = capi.hsc_chn_dsp_ltp_get(chn, capi.HSC_VALUE_FMT_16p8_FIXP)
print(status, ltp)

status, ltp = capi.hsc_chn_dsp_ltp_get(chn, capi.HSC_VALUE_FMT_DB)
print(status, ltp)
```

Sao thay ben porrima cung ra FFFF het rao ne
![[Pasted image 20220524110318.png]]
![[Pasted image 20220524110252.png]]

```
LTP value in decimal =65535
LTP value in dB = 1.#INF00
Device ID Low = 210
Device ID High = 76a0
```

lynx api:
users/dutran/lynx_ltp
7735e5cac6a16725973e663ebe1ea71e71adca45

cpl fw
users/dutran/ltp_read

register browser, synced to master
branch: users/dutran/cpl_ltp
commit ef07ae0a0402080cbc94c1009dcae64eb115edd1
RETCSW-155 add cpl regs for LTP CMIS


Version test on [[hcm-lab-1006]]
![[Pasted image 20220524185557.png]]
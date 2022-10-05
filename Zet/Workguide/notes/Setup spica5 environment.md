---
title: Setup spica5 environment
created: 2022-Sep-21
tags:
  - 'permanent/howto'
aliases:
  - Spica5 build
---
up::
Setup environment on [[DC5 server]] follow by [[Spica5_API_FW_interwork_api_check_unittest.pdf]] guide:

```bash
export HSC_DIR=~/projects/hsc/
export PATH=${PATH}:${HSC_DIR}/spica5/tools/pyral/scripts
export PYTHONPATH=${PYTHONPATH}:${HSC_DIR}/spica5/tools/pyral:${HSC_DIR}/spica5/tools/simulators

python3 ${HSC_DIR}/spica5/tools/pyral/scripts/ral_server --chip spica5 --port 50000 simulator
```

After start ral server, the sample log will be printed out.
```
2022-09-21 03:00:11 dc5lp-vinetx023.inphi-corp.local root[19346] INFO Starting simulator server and listening on port 50000
```

### Build/Run FW
```bash
# install to ~/.local/bin
pip3 install meson --user
pip3 install Ninja --user

# add local bin path to path
export PATH=${PATH}:~/.local/bin

# Build FW
cd ${HSC_DIR}/spica5/firmware/application
meson setup .x86 --buildtype=plain
meson setup .x86 -Dxmlrpc=false --reconfigure
meson compile -C .x86 -j 3
./.x86/spica5_fw_app --ip localhost --port 50000 --cli-port 52000
```

After start FW APP, some log will be printed out.
```
Starting target 0 ...
Starting target 1 ...
Main process: 25841.
Target 0, PID: 25844, CLI port: 52000
CLI server started and listening on port 52000
Target 1, PID: 25845, CLI port: 52001
CLI server started and listening on port 52001
```

Then on the simulator shell, some log will be printout 
```
2022-09-21 03:01:33 dc5lp-vinetx023.inphi-corp.local root[19346] INFO Connected from 127.0.0.1:58728
2022-09-21 03:01:33 dc5lp-vinetx023.inphi-corp.local root[19346] INFO Connected from 127.0.0.1:58730
Enabling sw_counter
Enabling sw_counter
[eru.bias0] DBG : [eru.bias0] power up REFGEN FSM
[eru.bias0] DBG : [eru.bias0] BIAS up
[eru.bias0] DBG : [eru.bias0] !Configuring BIAS LDO 19
[eru.bias0] DBG :   bypass:    0
[eru.bias0] DBG :   on:        1
[eru.bias0] DBG :   bandwidth: 3
[eru.bias0] DBG : [eru.bias0] !Configuring BIAS LDO 19
[eru.bias0] DBG :   bypass:    0
[eru.bias0] DBG :   on:        1
[eru.bias0] DBG :   bandwidth: 3
[eru.bias0] DBG : [eru.bias0] !Configuring BIAS LDO 20
[eru.bias0] DBG :   bypass:    0
[eru.bias0] DBG :   on:        1
[eru.bias0] DBG :   bandwidth: 0
[eru.bias0] DBG : [eru.bias0] !Configuring BIAS LDO 20
[eru.bias0] DBG :   bypass:    0
[eru.bias0] DBG :   on:        1
[eru.bias0] DBG :   bandwidth: 0
[eru.bias0] DBG : STRT_VTOP_CAL
[eru.bias0] DBG : STRT_VTOP_CAL
[eru.bias0] DBG : VTOP Cal Done, set status
[eru.bias0] DBG : refgen_status3 updated
[eru.bias0] DBG : VTOP Cal Done, set status
[eru.bias0] DBG : refgen_status3 updated
[eru.bias0] DBG : STRT_IADC_INPUT_CAL
[eru.bias0] DBG : STRT_IADC_INPUT_CAL
[eru.bias0] DBG : IADC_INPUT_CAL_DONE, set status
[eru.bias0] DBG : refgen_status3 updated
[eru.bias0] DBG : IADC_INPUT_CAL_DONE, set status
[eru.bias0] DBG : refgen_status3 updated
[eru.bias0] DBG : STRT_VLDO_CAL
[eru.bias0] DBG : STRT_VLDO_CAL
[eru.bias0] DBG : VLDO_CAL_DONE, set status
[eru.bias0] DBG : refgen_status3 updated
[eru.bias0] DBG : Write latch_en_low
```

### Build API
```shell
export HSC_DIR=~/projects/hsc/
make -C ${HSC_DIR}/spica5/capi clean
make -C ${HSC_DIR}/spica5/capi PRODUCTS=spica5 PROJECT_PREFIX=spica5 CC_OPTIONS="-g3 -O0" legacy -j5

# CLIB
make -C ${HSC_DIR}/spica5/capi PRODUCTS=spica5_spicap PROJECT_PREFIX=spica5 CC_OPTIONS="-g3 -O0" legacy -j5
```
### Build Test

```shell
meson setup --werror --warnlevel 2 -Db_coverage=true -DSIZE_T=size_t .x86


make -C ${HSC_DIR}/spica5/api/capi/tests clean
make -C ${HSC_DIR}/spica5/api/capi/tests xmlrpc
make -C ${HSC_DIR}/spica5/api/capi/tests PRODUCTS=spica5 PROJECT_PREFIX=spica5 CC_OPTIONS="-g3 -O0" DEBUG=1 -j3
```


### Eclipse debug
```shell
/home/dutran/projects/hsc/spica5/api/capi/build-output/tests/tests --rawtcp --ip 127.0.0.1 --port 50000 --product spica5
```

--rawtcp --ip 127.0.0.1 --port 50000 --product spica5



## Relate:
- https://ewiki.marvell.com/pages/viewpage.action?pageId=242602988#NovaFW/APIWorkingEnvironment-Emulationenvironment
---
title: Spica5 - GUI and API test on Emulator Platform
created: 2022-Oct-04
tags:
  - 'tasks/todo'
project: TBD
date:
  - start: 2022-10-04
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Tasks list]]

GUI:
http://dc5lp-vlas-sw-01/projects/sw/inphi_explorer/hsc/builds/debug/spica5n/6.1.614/
http://sw.inphi-corp.local/~swott-jenkins/projects/inphi_explorer/hsc/builds/debug/spica5n/6.1.620/

Depend on emulator that started on which server
```
Connect type: Socket
10.112.96.85, Port: 7713
```

![[20221004140047 ~ GUI emulator port and ip address.png]]

- GUI 614 vs 620

![[20221004151438 ~ POR RX.png]]

![[20221004163415 ~ POR TX block.png]]

### Source:
[[Debug_GUI_Demo_v1.pdf]]


[[2022-10-06]]

`spica5n\python\private\startup.py`

```python
def odsp_bundle_rules_query(bundle, rules):
    return _odsp_api.ODSP_OK

def odsp_chn_is_power_down(chn):
    return False

def odsp_dev_fw_is_running(dev):
    return True
```


```python
def odsp_prbs_chk_rules_t():
	return odsp_prbs_rules_t()

def odsp_prbs_gen_rules_t():
	return odsp_prbs_rules_t()
```
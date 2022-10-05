---
title: How to use Inphi Register web browser
created: 2022-May-19
tags:
  - 'permanent/howto'
---

## Run
- Register web browser has already ran on inphi server at http://sw.inphi-corp.local:8086/browser


## Develop
Start local server on Cygwin on local windows

Python version: 2.7

```
dutran@MRVL-quyC4VI9v7 /cygdrive/c/Users/dutran/projects/hsc/register_web_browser
$ python register_browser.py
register_browser.py:405:<module>(): Starting device_manager


register_browser.py:453:<module>(): Starting register browser
register_browser.py:482:<module>():
Launching service. Open a browser window at:
  http://MRVL-quyC4VI9v7:8086/browser
    OR
  http://127.0.0.1:8086/browser

```

then input http://127.0.0.1:8086/browser to browser

export full registers list, then copy the list to `register_web_browser\dbs\<product>\public_registers.txt`

![[Pasted image 20220520104429.png]]

```
// public_registers.txt file

AN_STATUS
AN_STATUS2			// public
#LT_FSM_STATE=INPHI // Private
LT_STATUS
#ANLT_TSTAMP0=INPHI
#ANLT_TSTAMP1=INPHI
#LT_EQ_TAP_CM3=INPHI
```
Make register public or private then start register again.

Some error happen when first time running:

---
hl_reg not found

Error:
```shell
ModuleNotFoundError: No module named 'hl_reg'
```
Solution: Check python version, It should be python 2.7

---
twisted lib not found

Error:
```shell
No module named twisted.internet
```

Solution:
```shell
pip install twisted
python -m pip install twisted --user # local user
```
	

## Notes:
- If define reg on CPL FW, need to define for both CPLA and CPLB

- [ ] Compare speed when start server on Cygwin vs dc5lp-vinetx000. 🔽
	- dc5lp-vinetx000: 3min
	- Local: 8min

```shell
# Edit makefile to get both capella/capellab regs
cd regdb
make get_hl_reg
```

Make firmware
```shell
make -f build.inc build
make -f build.inc gcc 		# fast check
```
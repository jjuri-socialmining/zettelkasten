---
title: How to scan device via Olympus
created: 2022-May-27
tags:
  - 'permanent/howto'
---


http://las-gitlab/hsc-sw-hcm/gui_gen2/tools/misc/-/blob/master/python/supports/olympus/evb_info_discovery.py

```shell
File "C:\usr\dutran\python_supports_olympus_evb_info_discovery.py", line 10, in <module>
    import Olympus64 as olympus
SystemError: initialization of Olympus64 raised unreported exception
```
-> Driver hang

```
OTT-LAB-5010+ottlab@OTT-LAB-5010 MINGW64 /c/usr/dutran
$ python --version
Python 2.7.13 :: Anaconda 4.3.0 (32-bit)

OTT-LAB-5010+ottlab@OTT-LAB-5010 MINGW64 /c/usr/dutran
$ python python_supports_olympus_evb_info_discovery.py
Rev 1.0; 2022-05-10; 11:00AM GTM+7
Start scanning
 Scanning config:
  - Scan Janus: True
  - Scan Zeus:  True
  - Scan phy:   True
    + From:     0x0
    + To:       0x1f



-----Olympus Version------
     2021.6 05-28-2020
-----INDEX (0)------
General Info:          index=0, serial number=2528, name=ZEUS-3 2528
Motherboard Info:      Name=ZEUS-3 MB, version=0, serial number=2528
                       FPGA=11.16 Artix 7 FPGA, FW=5.1 Firmware for USB FX3 ARM Controller
Daughterboard Info:    Name=ANTEVORTA-S3 Assy 17 DB, Board ID=4355(0x1103), serial number=16
Chip Info:             Name=PORRIMA-GEN4-EML-TOP, Chip ID=97(0x61)
-- Scanning PHY in bus 0
  -- Found phy=0x0 Die:Mira/Spica/SpicaP Die
  xx Phy=0x1 0ffff
  xx Phy=0x2 0ffff
  xx Phy=0x3 0ffff
  xx Phy=0x4 0ffff
  xx Phy=0x5 0ffff
  xx Phy=0x6 0ffff
  xx Phy=0x7 0ffff
  xx Phy=0x8 0ffff
  xx Phy=0x9 0ffff
  xx Phy=0xa 0ffff
  xx Phy=0xb 0ffff
  xx Phy=0xc 0ffff
  xx Phy=0xd 0ffff
  xx Phy=0xe 0ffff
  xx Phy=0xf 0ffff
  xx Phy=0x10 0ffff
  xx Phy=0x11 0ffff
  xx Phy=0x12 0ffff
  xx Phy=0x13 0ffff
  xx Phy=0x14 0ffff
  xx Phy=0x15 0ffff
  xx Phy=0x16 0ffff
  xx Phy=0x17 0ffff
  xx Phy=0x18 0ffff
  xx Phy=0x19 0ffff
  xx Phy=0x1a 0ffff
  xx Phy=0x1b 0ffff
  xx Phy=0x1c 0ffff
  xx Phy=0x1d 0ffff
  xx Phy=0x1e 0ffff

```
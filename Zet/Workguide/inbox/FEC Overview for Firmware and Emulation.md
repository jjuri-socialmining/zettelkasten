---
title: FEC Overview for Firmware and Emulation
created: 2022-Sep-15
tags:
  - 'inbox'
url:
  - https://ewiki.marvell.com/display/ODSP/FEC
---
source:
- [[spica5n_fec_mon_overview.pdf]]
- https://ewiki.marvell.com/display/ODSP/FEC

Recording session from Michael Duckering: 
- [link](https://marvell.zoom.us/rec/share/hovoyEGyo-FfqXn9EGsED_w2hfgoov_4fCYV8emL-66aAmFJ8LGuDc7_QfLWYsqi.jEtmjnrznJFy1bX-)
- Passcode: 2FwR5g9%

## Note
Reed-Solomon FEC encoding calculate message and appending a codeword to message
Decode a codeword, calculate syndrome, if syndrome is 0, there is no errors.


Basics

Two encoding supported:
- KR: [[RS(528, 514)]] 14 parity symbols, T=7
- KP: [[RS(544, 514)]] 30 parity symbols, T=15

![[20220915104010 - FEC Basics.png]]

- [ ] KP add 300 parity bit, why output 544/528 times faster than input? [[RS(544, 514)]]? why 528, not 514? #tasks/todo/research 

RS symbols are distributed to FEC lanes, each FEC lane has alignment markers. AM are used to reorder FEC lanes.


- T represents the number of Error that can be corrected
- KR: T=7: codeword with 1-7 errors are correctable
- KP, T=15: codeword with 1-15 errors are correctable


![[20220915105521 - FEC standards.png]]

KP and KR are different FEC
https://marvell.sharepoint.com/sites/hsc/engineering/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2Fhsc%2Fengineering%2FShared%20Documents%2FPublications%2FStandards%2FIEEE%20%28Ethernet%20802%2E3%29&viewid=d3d420ea%2D5d2c%2D496e%2Dac6f%2D18a1d80a0df3

[[FEC Codeword]]

[[Spica5n FEC Block Diagram]]

![[LL-FEC-Specification-1.0-25G-Consortium.pdf]]

[[Spica5n PCS Diagram]]

There are two types of FEC methods used in Falcon:
1.  Fire Code FEC (FC-FEC), used primarily for 10G ports with lower latency and error correction
2.  Reed-Solomon FEC (RS-FEC), used for 25G to 100G ports with higher latency,

Idle pattern gen
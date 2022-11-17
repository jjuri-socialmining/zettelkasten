---
title: Dfe precoder should not be turned on in non-DFE modes
UID: 221115094515
created: 15-Nov-2022
tags:
  - 'created/2022/Nov/15'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221115094515'
publish: False
---
## Notes:
```
The DFE precoder helps to transform burst errors from the DFE to error events with smaller number of bit flips in order to improve BER. The precoder should not be turned on in non-DFE modes since it can actually increase the BER.

- the link partner's transmit precoder must be enabled if this rule is set to true.
- the precoder should only be enabled in PAM mode (it should be turned off in NRZ)
```

source:: [[Capella api]]

## Relate:
---
title: Por GUI description about FIR taps
UID: 221108151905
created: 08-Nov-2022
tags:
  - 'created/2022/Nov/08'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221108151905'
publish: False
---
## Notes:
```
- It is advisable to keep Tap 1 > 500. A negative Tap 1 will simply invert the data polarity.

- Overall peak-to-peak amplitude can be adjusted with a combination of the Swing control and Tap 1. If a lower output swing is desired, it is advisable to use the Swing control as it is more power-efficient. Using Tap 1 is ideal for finer amplitude control.

- LUT mode cannot be switched on the fly in the Transmitter Tab. The device needs to be re-initialized to change the LUT mode.

- Tap1 is chosen as main tap just to maintain symmetry of 1-pre and 1-post in the 3-Tap mode. The main tap location in the 3 tap or 7 tap mode can be arbitrary and is governed by the tap that0 has the largest value. This allows flexibility in the number of pre and post taps. For example, in 3-tap mode, if tap2 has the largest value, then the 3-tap FIR is configured effectively with 2 pre taps in 1 main tap.
```

![[20221108152251 ~ POR FIR description.png]]

## Relate:
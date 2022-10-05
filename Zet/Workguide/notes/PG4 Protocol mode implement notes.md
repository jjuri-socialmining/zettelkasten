---
title: PG4 Protocol mode implement notes
created: 2022-May-27
tags:
  - 'permanent/fact'
---


```c
    /** NOT SUPPORTED - Host 4x106.25Gbps (PAM4) to Line 4x106.25Gbps (PAM4*/
    POR_MODE_400G_KP4_TO_KP4       =  0,
    /** Host 4x25.78125 Gbps (NRZ) to Line 4x25.78125 Gbps (NRZ) */
    POR_MODE_100G_PCS4_TO_PCS4,
    /** NOT SUPPORTED - Host 4x82.5Gbps (PAM4) to Line 4x82.5Gbps (PAM4) [Discount Rate]*/
    POR_MODE_300G_KP4_TO_KP4,
    /** Host 200GAUI-4 (PAM4) to Line KP4 (PAM4), Host 4x53.125 Gbps (PAM4) to Line 4x53.125 Gbps (PAM4) */
    POR_MODE_200G_KP4_TO_KP4,
    /** Host 4x25.78125 Gbps (NRZ) to Line 2x51.5625 Gbps (PAM4) */
    POR_MODE_100G_PCS4_TO_KP2,
    /** Host 400GAUI-8 (PAM4) to Line KP4 (PAM4), Host 8x53.125 Gbps (PAM) to Line 4x106.25 Gbps (PAM4) */
    POR_MODE_400G_KP8_TO_KP4,
    /** Host 200GAUI-4 (PAM4) to Line KP2 (PAM4), Host 4x53.125 Gbps (PAM) to Line 2x106.25 Gbps (PAM4) */
    POR_MODE_200G_KP4_TO_KP2,
    /** Host 100GAUI-2 (PAM4) to Line KP1 (PAM4), Host 2x53.125 Gbps (PAM) to Line 1x106.25 Gbps (PAM4) */
    POR_MODE_100G_KP2_TO_KP1,
    /** Host 100GAUI-4 (NRZ) to Line KP1 (PAM4), Host 4x26.5625 Gbps (NRZ) to Line 1x106.25 Gbps (PAM4) */
    POR_MODE_100G_KP4_TO_KP1,
    /** NOT SUPPORTED - Host 4x53.1Gbps (NRZ) to Line 4x53.1Gbps (NRZ)*/
    POR_MODE_200G_4Nx53p1_TO_4Nx53p1,
    /** Host 200GAUI-8 (NRZ) to Line KP4 (PAM4), Host 8x26.5625 Gbps (NRZ) to Line 4x53.1Gbps (PAM4) */
    POR_MODE_200G_KP8_TO_KP4,
    /** Host 8x27.95237 Gbps (PAM) to Line 4x55.90474 Gbps (PAM) */
    POR_MODE_400G_FOIC8_TO_FOIC4,
    /** Host 8x26.628 Gbps (PAM) to Line 4x53.256 Gbps (PAM) */
    POR_MODE_400G_FOICE8_TO_FOICE4,
    /** Host 8x28.70618 Gbps (PAM) to Line 4x57.41236 Gbps (PAM) */
    POR_MODE_400G_OTLC8_TO_OTLC4,
```
Not support:
- `POR_MODE_400G_KP4_TO_KP4 Host 4x106.25Gbps (PAM4) to Line 4x106.25Gbps (PAM4` 
- `POR_MODE_300G_KP4_TO_KP4 Host 4x82.5Gbps (PAM4) to Line 4x82.5Gbps (PAM4) [Discount Rate]`
- `POR_MODE_200G_4Nx53p1_TO_4Nx53p1 Host 4x53.1Gbps (NRZ) to Line 4x53.1Gbps (NRZ)`

Support:
```c
    /** Host 4x25.78125 Gbps (NRZ) to Line 4x25.78125 Gbps (NRZ) */
    POR_MODE_100G_PCS4_TO_PCS4,
    /** Host 200GAUI-4 (PAM4) to Line KP4 (PAM4), Host 4x53.125 Gbps (PAM4) to Line 4x53.125 Gbps (PAM4) */
    POR_MODE_200G_KP4_TO_KP4,
    /** Host 4x25.78125 Gbps (NRZ) to Line 2x51.5625 Gbps (PAM4) */
    POR_MODE_100G_PCS4_TO_KP2,
    /** Host 400GAUI-8 (PAM4) to Line KP4 (PAM4), Host 8x53.125 Gbps (PAM) to Line 4x106.25 Gbps (PAM4) */
    POR_MODE_400G_KP8_TO_KP4,
    /** Host 200GAUI-4 (PAM4) to Line KP2 (PAM4), Host 4x53.125 Gbps (PAM) to Line 2x106.25 Gbps (PAM4) */
    POR_MODE_200G_KP4_TO_KP2,
    /** Host 100GAUI-2 (PAM4) to Line KP1 (PAM4), Host 2x53.125 Gbps (PAM) to Line 1x106.25 Gbps (PAM4) */
    POR_MODE_100G_KP2_TO_KP1,
    /** Host 100GAUI-4 (NRZ) to Line KP1 (PAM4), Host 4x26.5625 Gbps (NRZ) to Line 1x106.25 Gbps (PAM4) */
    POR_MODE_100G_KP4_TO_KP1,
    /** Host 200GAUI-8 (NRZ) to Line KP4 (PAM4), Host 8x26.5625 Gbps (NRZ) to Line 4x53.1Gbps (PAM4) */
    POR_MODE_200G_KP8_TO_KP4,
    /** Host 8x27.95237 Gbps (PAM) to Line 4x55.90474 Gbps (PAM) */
    POR_MODE_400G_FOIC8_TO_FOIC4,
    /** Host 8x26.628 Gbps (PAM) to Line 4x53.256 Gbps (PAM) */
    POR_MODE_400G_FOICE8_TO_FOICE4,
    /** Host 8x28.70618 Gbps (PAM) to Line 4x57.41236 Gbps (PAM) */
    POR_MODE_400G_OTLC8_TO_OTLC4,
```
Retimer: 4x25gNRZ, 4x26gPAM
Gearbox: 4x25gNRZ-2x25gPAM, 8x26gPAM-4x53gPAM, 4x26gPAM-2x53gPAM, 4x26gNRZ-1x53gPAM, 8x26gNRZ-4x26gPAM

GUI protocol MODE
![[Pasted image 20220523110256.png]]




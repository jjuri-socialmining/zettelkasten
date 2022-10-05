---
title: 2022-07-04 - Alaska_A status
created: 2022-Jul-04
tags:
  - 'permanent/common'
---

![[lynx.png]]

New text:

## 1.1 Latency Variation Measurement / Control

For the purposes of explaining how Latency Variation Measurement / Control works consider the following figure that includes a simplified Capella TX block diagram and an updated diagram with changes needed to implement the variation control.

![[latency_measure.jpg]]

Figure 12: Latency Measurement Capella TX Pipeline Change

The FIFO is the source of the latency variation due to the potential meta-stability of the FIFO_RECENTER commands. As the firmware will recenter the FIFO when bringing up a channel there is a +/- 1 clock uncertainty due to the read and write pointers being offset. The meta-stability is due to the uncorrelated phase (and frequency) of the read and write data clocks relative to the processor clock.

Note that the generic_fifo is composed of 4 FIFO slices. Depending on configuration / mode some or all of the FIFO slices may be active. Also depending on mode, some or all of the FIFO slices may be synchronized.

The generic_fifo has been updated to output 8 signals. For each FIFO slice, r0_pulse and w0_pulse will  go high for 1 clock cycle (of their respective clocks) when the pointer value equals 0.

Note that Capella supports 4 different rates: 100G PAM, 50G NRZ, 50G PAM, 25G NRZ. For PAM the pipeline is 128 bits wide. For the NRZ modes the internal pipeline is 64 bits and for the last 2 modes the baud rate is 1/2. The delays described below are referenced to 50/100G PAM. For NRZ modes the amount that can be shifted remains the same, but the number of unique shift values is halved.

Recall that: PAM/NRZ mode each pipeline clock is 64-UI, but the number of bits per UI are 2/1 respectively.

The latency_measurement_block (lat_meas_top) has a free running counter (clocked by a high speed [nominally 6.6GHz] clock] that samples the [rw]0_pulse signals and stores the values in registers (as a 1 shot). FW can read these counter values and get a reading of the delay between read and write pointers. As the clock is faster than the read / write clock, the resolution is 150 ps.

A barrel shifter is added after the FIFO and the barrel shifter can delay the data from 0 to 15/16th of a 64-UI period. In other words, 0 .. 15 shifts of 8 bits. Note that in NRZ mode this is 0..7 shifts of 8 bits. The barrel shifter is controlled by the firmware. 

The generic_fifo has the ability to bump the read or write pointer by a single step as well. Thus, if the FW wants to remove 8 bits of delay, the fifo read pointer can be bumped up by 1 (removing 1 whole clock of delay) and the barrel shifter can be set to adding 120 bits of delay (15/16). Again for NRZ, the shifter would be set to 7/8 or 56 bits of delay.

### 1.1.1        Linear Delay Model of Multiple FIFOs

As the crossbar also contains 8 generic_fifo instances (to support gearboxing), the same latency measurement circuit will be used. One of the Capella instances will output the 6.6G clock and it will be routed in the core to the latency measurement circuits.

The latency variation is piece-wise linear, meaning that each FIFO adds a “variable” amount of delay each time it is recentered, as the pipelines between the FIFOs are synchronous they always add an integer number of clocks (and thus can be ignored).

FW will monitor the delay in both the core and the Capella FIFOs.

The total “variable” delay is the sum of both measurement.

The goal is to modify that delay to a “known fixed value”.

Each FIFO has the ability to bump the read or write pointer by +/- 1 clock (at a time).

Therefore only 1 barrel shifter is needed because there need only be 1 place where fractional delays should be applied.

### 1.1.2        Firmware Use / Programming Model

The lat_meas_top block contains 8 instances of lat_meas_unit, for Capella the mapping of signals to units is event[7..0] = {w0_pulse[3], r0_pulse[3], w0_pulse[2], r0_pulse[2], w0_pulse[1], r0_pulse[1], w0_pulse[0], r0_pulse[0]}.

One of the 8 units is designated the primary and is the first to capture a timestamp. All the other units will begin capturing after the primary.

Each of the 8 units can select which event they monitor, although there is little reason to program the select values to anything other than the default which is {7,6,5,4,3,2,1,0}.

There are 3 control bits needed to actually cause a capture are: reset, clken, start. Reset is default 1 and holds the block in reset. Cklen must be set to 1 to turn on the clock, thus it offers a low power mode (or just reset it). Start must be set to 1 to cause the data to be captured and then should be set to 0 a “short” time later. Note that it is not a self-clearing bit.

The lat_meas_block contains a number of registers for control and status monitoring detailed in the table below. **__N is in the range of 0..7 for the core FIFOs. Within Capella there is no need for a trailing _N._**

![[Pasted image 20220704141542.png]]

The expectation on FW / DV is to: set primary and select values, then remove reset, enable clken and start.

Then remove start, read all count values and then disable clken and assert reset.

### 1.1.3        Timing / Skew Requirement for Physical Design

The r0_pulse and w0_pulse for a given FIFO slice should be delay matched from their launch flop to the two gen_sync_scalar_v2 blocks that sample them in the high speed domain. In theory this means there are 4 sets of 2 signals that have to be skew controlled.

The lat_meas_top block instantiates 8 lat_meas_unit blocks. Each of those blocks receives all 8 [r/w]0_pulse signals and uses a mux to select which signal a given lat_meas_unit cares about.

If we want to enable the programmability then the skew problem is much more difficult as you have a combinatorial increase number of end points that have to be matched.

Instead, it is proposed that we assume a fixed programming of the select bits and therefore limit ourselves to control the skew between 4 pairs of signals to 4 pair of endpoints.

To be clear, given the definition of the event vector above, units 0/1, 2/3, 4/5, 6/7 should be skew match pairs.




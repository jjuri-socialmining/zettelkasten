```
$ ./example.exe 127.0.0.1 2533 run_traffic
Connecting to 127.0.0.1:2533
run_traffic()
bundle_teardown()-
time taken 0.000569/(0.000571)
time taken 2.223333/(2.223937)
done
hsc_dev_bundle_rules()
done
hsc_bundle_rules_chns_mask_set()
done
hsc_bundle_rules_baud_rate_set()
done
hsc_bundle_rules_signalling_set()
done
hsc_chn_tx_rules()
done
hsc_chn_rx_rules()
done
time taken 0.000059/(2.224029)
hsc_bundle_init()
done
time taken 0.000265/(2.224307)
hsc_bundle_start()
done
time taken 1.953454/(4.177777)
prbs_generator_config()
________ PRBS htx ser gen cfg ___________
prbs_generator_config(), chn_idx=0, intf=HTX_SERIAL
prbs_generator_config(), chn_idx=1, intf=HTX_SERIAL
prbs_generator_config(), chn_idx=2, intf=HTX_SERIAL
prbs_generator_config(), chn_idx=3, intf=HTX_SERIAL
prbs_generator_config(), chn_idx=4, intf=HTX_SERIAL
prbs_generator_config(), chn_idx=5, intf=HTX_SERIAL
prbs_generator_config(), chn_idx=6, intf=HTX_SERIAL
prbs_generator_config(), chn_idx=7, intf=HTX_SERIAL
done
time taken 0.232350/(4.410151)
time taken 0.000000/(4.410169)
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 0
time taken 1.622190/(6.032369)
bundle_id = 0, Status: 0
time taken 1.640660/(7.673050)
bundle_id = 0, Status: 0
time taken 1.640454/(9.313580)
done
time taken 0.000004/(9.313610)
prbs_checker_config()
________ PRBS hrx serial ckr cfg ___________
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 0 rx intf
prbs_checker_config(), chn_idx=0, intf=HRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 1 rx intf
prbs_checker_config(), chn_idx=1, intf=HRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 2 rx intf
prbs_checker_config(), chn_idx=2, intf=HRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 3 rx intf
prbs_checker_config(), chn_idx=3, intf=HRX_SERIAL
WARNING: Can not enable checker at channel 4 rx intf
prbs_checker_config(), chn_idx=4, intf=HRX_SERIAL
WARNING: Can not enable checker at channel 5 rx intf
prbs_checker_config(), chn_idx=5, intf=HRX_SERIAL
WARNING: Can not enable checker at channel 6 rx intf
prbs_checker_config(), chn_idx=6, intf=HRX_SERIAL
WARNING: Can not enable checker at channel 7 rx intf
prbs_checker_config(), chn_idx=7, intf=HRX_SERIAL
________ PRBS lrx serial ckr cfg ___________
prbs_checker_config(), chn_idx=0, intf=LRX_SERIAL
prbs_checker_config(), chn_idx=1, intf=LRX_SERIAL
prbs_checker_config(), chn_idx=2, intf=LRX_SERIAL
prbs_checker_config(), chn_idx=3, intf=LRX_SERIAL
prbs_checker_config(), chn_idx=4, intf=LRX_SERIAL
prbs_checker_config(), chn_idx=5, intf=LRX_SERIAL
prbs_checker_config(), chn_idx=6, intf=LRX_SERIAL
prbs_checker_config(), chn_idx=7, intf=LRX_SERIAL
________ PRBS hrx core ckr cfg ___________
prbs_checker_config(), chn_idx=0, intf=HRX_CORE
prbs_checker_config(), chn_idx=1, intf=HRX_CORE
prbs_checker_config(), chn_idx=2, intf=HRX_CORE
prbs_checker_config(), chn_idx=3, intf=HRX_CORE
prbs_checker_config(), chn_idx=4, intf=HRX_CORE
prbs_checker_config(), chn_idx=5, intf=HRX_CORE
prbs_checker_config(), chn_idx=6, intf=HRX_CORE
prbs_checker_config(), chn_idx=7, intf=HRX_CORE
________ PRBS lrx core ckr cfg ___________
prbs_checker_config(), chn_idx=0, intf=LRX_CORE
prbs_checker_config(), chn_idx=1, intf=LRX_CORE
prbs_checker_config(), chn_idx=2, intf=LRX_CORE
prbs_checker_config(), chn_idx=3, intf=LRX_CORE
prbs_checker_config(), chn_idx=4, intf=LRX_CORE
prbs_checker_config(), chn_idx=5, intf=LRX_CORE
prbs_checker_config(), chn_idx=6, intf=LRX_CORE
prbs_checker_config(), chn_idx=7, intf=LRX_CORE
________ PRBS htx core ckr cfg ___________
prbs_checker_config(), chn_idx=0, intf=HTX_CORE
prbs_checker_config(), chn_idx=1, intf=HTX_CORE
prbs_checker_config(), chn_idx=2, intf=HTX_CORE
prbs_checker_config(), chn_idx=3, intf=HTX_CORE
prbs_checker_config(), chn_idx=4, intf=HTX_CORE
prbs_checker_config(), chn_idx=5, intf=HTX_CORE
prbs_checker_config(), chn_idx=6, intf=HTX_CORE
prbs_checker_config(), chn_idx=7, intf=HTX_CORE
________ PRBS ltx core ckr cfg ___________
prbs_checker_config(), chn_idx=0, intf=LTX_CORE
prbs_checker_config(), chn_idx=1, intf=LTX_CORE
prbs_checker_config(), chn_idx=2, intf=LTX_CORE
prbs_checker_config(), chn_idx=3, intf=LTX_CORE
prbs_checker_config(), chn_idx=4, intf=LTX_CORE
prbs_checker_config(), chn_idx=5, intf=LTX_CORE
prbs_checker_config(), chn_idx=6, intf=LTX_CORE
prbs_checker_config(), chn_idx=7, intf=LTX_CORE
done
time taken 0.042073/(9.355697)
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 0
time taken 0.000022/(9.355735)
bundle_id = 0, Status: 0
time taken 0.000018/(9.355765)
bundle_id = 0, Status: 0
time taken 0.000018/(9.355795)
done
time taken 0.000003/(9.355810)
Bundle rules

API Version 0.8.0.909
API Built on Apr 22, 2022 at 16:00:47


Application Firmware Version (Major.Minor.Patch.Update) 0.14.0.406


Bundle Rule - ID : 0
oper mode = DUPLEX_RETIMER
baud rate = 56.250000 G

HTX
  chn_id | Signalling | Baudrate | LUT Mode  | Gray Map | Precoder | Invert | Inner Eye 1 | Inner Eye 2 | Tx Swing | IEEE DeMap
  -------+------------+----------+-----------+----------+----------+--------+-------------+-------------+----------+------------
       0 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       1 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       2 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       3 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       4 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       5 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       6 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       7 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
  Taps  |  Pre  |  Main |  Post
  ------+-------+-------+-------
     0  |   -50 |   650 |     0
     1  |   -50 |   650 |     0
     2  |   -50 |   650 |     0
     3  |   -50 |   650 |     0
     4  |   -50 |   650 |     0
     5  |   -50 |   650 |     0
     6  |   -50 |   650 |     0
     7  |   -50 |   650 |     0

HRX
  chn_id | Signalling | Baudrate | DSP Mode     | Gray Map | Precoder | Invert | CTLE auto, codes | AFE Trim | VGA Track | AC Cpl Bp | IEEE DeMap | MLSD  | SCDR
  -------+------------+----------+--------------+----------+----------+--------+------------------+----------+-----------+-----------+------------+-------+------
       0 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       1 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       2 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       3 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       4 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       5 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       6 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       7 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False

LTX
  chn_id | Signalling | Baudrate | LUT Mode  | Gray Map | Precoder | Invert | Inner Eye 1 | Inner Eye 2 | Tx Swing | IEEE DeMap
  -------+------------+----------+-----------+----------+----------+--------+-------------+-------------+----------+------------
       0 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       1 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       2 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       3 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       4 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       5 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       6 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
       7 |        PAM | 56250000 | 3-Tap LUT |     True |    False |  False |        1000 |        2000 |    100 % |       True
  Taps  |  Pre  |  Main |  Post
  ------+-------+-------+-------
     0  |   -50 |   650 |     0
     1  |   -50 |   650 |     0
     2  |   -50 |   650 |     0
     3  |   -50 |   650 |     0
     4  |   -50 |   650 |     0
     5  |   -50 |   650 |     0
     6  |   -50 |   650 |     0
     7  |   -50 |   650 |     0

LRX
  chn_id | Signalling | Baudrate | DSP Mode     | Gray Map | Precoder | Invert | CTLE auto, codes | AFE Trim | VGA Track | AC Cpl Bp | IEEE DeMap | MLSD  | SCDR
  -------+------------+----------+--------------+----------+----------+--------+------------------+----------+-----------+-----------+------------+-------+------
       0 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       1 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       2 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       3 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       4 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       5 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       6 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False
       7 |        PAM | 56250000 |         SLC1 |     True |    False |  False |   False, { 0, 0} |     Auto |     False |        DC |       True | False | False

time taken 0.810905/(10.166727)
Bundle status

Bundle Status - ID : 0
HTX
  chn_id | fw locked
  -------+------------
       0 |       yes
       1 |       yes
       2 |       yes
       3 |       yes
       4 |       yes
       5 |       yes
       6 |       yes
       7 |       yes
HRX
  chn_id | fw locked | signal detected | dsp ready | SNR(dB)
  -------+-----------+-----------------+-----------+--------
       0 |        no |              no |        no | 0.00
       1 |        no |              no |        no | 0.00
       2 |        no |              no |        no | 0.00
       3 |        no |              no |        no | 0.00
       4 |       yes |             yes |       yes | 26.69
       5 |       yes |             yes |       yes | 26.69
       6 |       yes |             yes |       yes | 26.69
       7 |       yes |             yes |       yes | 26.69
LTX
  chn_id | fw locked
  -------+------------
       0 |        no
       1 |        no
       2 |        no
       3 |        no
       4 |       yes
       5 |       yes
       6 |       yes
       7 |       yes
LRX
  chn_id | fw locked | signal detected | dsp ready | SNR(dB)
  -------+-----------+-----------------+-----------+--------
       0 |       yes |             yes |       yes | 25.96
       1 |       yes |             yes |       yes | 25.96
       2 |       yes |             yes |       yes | 25.64
       3 |       yes |             yes |       yes | 25.64
       4 |       yes |             yes |       yes | 26.69
       5 |       yes |             yes |       yes | 26.31
       6 |       yes |             yes |       yes | 25.96
       7 |       yes |             yes |       yes | 26.69
time taken 0.894894/(11.061635)
time taken 0.000001/(11.061650)
time taken 0.000437/(11.062099)
+---------------------------------------------------------
| Receive Status - BER
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
| Ckr        | Ch# |       Total_Bits   |    Err_Bit_Cnt_MSB |    Err_Bit_Cnt_LSB |       BER_MSB      |       BER_LSB      |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    hrx_ser |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   4 |       121439162624 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   5 |       121383994752 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   6 |       121357045888 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   7 |       121306550912 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   hrx_core |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   4 |       121439232000 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   5 |       121383977728 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   6 |       121328895744 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   7 |       121306638336 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   htx_core |   0 |       121474587648 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   1 |       121473141760 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   2 |       121473332480 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   3 |       121478092544 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   4 |       121439310336 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   5 |       121383960320 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   6 |       121329371648 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   7 |       121307736832 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    lrx_ser |   0 |       121472908288 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   1 |       121473202048 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   2 |       121473471360 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   3 |       121477590528 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   4 |       121424702720 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   5 |       121384289152 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   6 |       121296633600 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   7 |       121307260928 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   lrx_core |   0 |       121474275840 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   1 |       121473306112 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   2 |       121474041856 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   3 |       121439184384 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   4 |       121424685056 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   5 |       121357263616 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   6 |       121296192512 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   7 |       121306188288 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   ltx_core |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   4 |       121422167296 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   5 |       121357323264 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   6 |       121306958080 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   7 |       121306594816 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
time taken 1.162842/(12.224957)
time taken 0.000000/(12.224975)
Example returned success
```
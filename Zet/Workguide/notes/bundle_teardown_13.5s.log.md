```
$ ./example.exe 127.0.0.1 50006 run_traffic
Connecting to 127.0.0.1:50006
inphi_xmlrpc_open: resolved hostname to 127.0.0.1
run_traffic()
bundle_teardown()-
time taken 0.007722
time taken 3.339657
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
time taken 3.339736
hsc_bundle_init()
done
time taken 3.341911
hsc_bundle_start()
done
time taken 5.255617
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
time taken 5.698206
time taken 5.698222
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 1
time taken 7.805859
done
time taken 7.805878
prbs_checker_config()
________ PRBS hrx serial ckr cfg ___________
prbs_checker_config(), chn_idx=0, intf=HRX_SERIAL
prbs_checker_config(), chn_idx=1, intf=HRX_SERIAL
prbs_checker_config(), chn_idx=2, intf=HRX_SERIAL
prbs_checker_config(), chn_idx=3, intf=HRX_SERIAL
prbs_checker_config(), chn_idx=4, intf=HRX_SERIAL
prbs_checker_config(), chn_idx=5, intf=HRX_SERIAL
prbs_checker_config(), chn_idx=6, intf=HRX_SERIAL
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
time taken 8.379273
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 1
time taken 8.379309
done
time taken 8.379325
Bundle rules

API Version 0.8.0.909
API Built on Apr 19, 2022 at 15:17:22


Application Firmware Version (Major.Minor.Patch.Update) 0.14.0.318


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
       0 |       yes |             yes |       yes | 25.96
       1 |       yes |             yes |       yes | 25.34
       2 |       yes |             yes |       yes | 25.96
       3 |       yes |             yes |       yes | 25.96
       4 |       yes |             yes |       yes | 26.31
       5 |       yes |             yes |       yes | 26.31
       6 |       yes |             yes |       yes | 25.96
       7 |       yes |             yes |       yes | 25.96
LTX
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
LRX
  chn_id | fw locked | signal detected | dsp ready | SNR(dB)
  -------+-----------+-----------------+-----------+--------
       0 |       yes |             yes |       yes | 25.96
       1 |       yes |             yes |       yes | 25.96
       2 |       yes |             yes |       yes | 25.64
       3 |       yes |             yes |       yes | 25.64
       4 |       yes |             yes |       yes | 26.31
       5 |       yes |             yes |       yes | 25.96
       6 |       yes |             yes |       yes | 25.64
       7 |       yes |             yes |       yes | 25.96
time taken 11.038878
time taken 11.044155
+---------------------------------------------------------
| Receive Status - BER
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
| Ckr        | Ch# |       Total_Bits   |    Err_Bit_Cnt_MSB |    Err_Bit_Cnt_LSB |       BER_MSB      |       BER_LSB      |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    hrx_ser |   0 |       192360865408 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   1 |       187878960000 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   2 |       187873759744 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   3 |       187851060736 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   4 |       107000704512 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   5 |         6271152256 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   6 |        13515118976 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   7 |        20649927296 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   hrx_core |   0 |       192673816832 |         4294967295 |         4294967295 |       4.458278e-02 |       4.458278e-02 |
|   hrx_core |   1 |       187914329344 |         4294967295 |         4294967295 |       4.571197e-02 |       4.571197e-02 |
|   hrx_core |   2 |       187815848704 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   3 |       188052350720 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   4 |       188263026688 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   5 |       187911887872 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   6 |       187667035904 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   7 |       187659481088 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   htx_core |   0 |       192395146752 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   1 |       187851848704 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   2 |       187882102784 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   3 |       188006572288 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   4 |       188277435392 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   5 |       187968086528 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   6 |       187707492608 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   7 |       187640442624 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    lrx_ser |   0 |       192323458048 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   1 |       187853726720 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   2 |       187831157248 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   3 |       187926583936 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   4 |        65565884672 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   5 |        80887792768 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   6 |        88091199744 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   7 |        99407718272 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   lrx_core |   0 |       190804909312 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   1 |       187851156480 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   2 |       187867131392 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   3 |       187931940352 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   4 |       192158901504 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   5 |       187747585792 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   6 |       187681574144 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   7 |       187609392640 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   ltx_core |   0 |       187889432064 |         4294967295 |         4294967295 |       4.571803e-02 |       4.571803e-02 |
|   ltx_core |   1 |       187846907392 |         4294967295 |         4294967295 |       4.572838e-02 |       4.572838e-02 |
|   ltx_core |   2 |       187834107904 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   3 |       187978921728 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   4 |       192215073792 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   5 |       187695151872 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   6 |       187650905088 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   7 |       187646716928 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
time taken 13.426603
time taken 13.426613
Example returned success
```
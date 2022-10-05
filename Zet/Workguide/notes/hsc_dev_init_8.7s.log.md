```
HCM-LAB-1006+hcmswlab@HCM-LAB-1006 /cygdrive/c/usr/dutran/example/hsc/lynx/api/examples
$ ./example.exe 127.0.0.1 50006 run_traffic
Connecting to 127.0.0.1:50006
inphi_xmlrpc_open: resolved hostname to 127.0.0.1
run_traffic()
bundle_teardown()-
time taken 0.009194
time taken 0.178306
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
time taken 0.178396
hsc_bundle_init()
done
time taken 0.184229
hsc_bundle_start()
done
time taken 1.162273
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
time taken 1.590402
time taken 1.590416
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 1
time taken 3.689621
done
time taken 3.689640
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
time taken 4.294017
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 1
time taken 4.294053
done
time taken 4.294069
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
       1 |       yes |             yes |       yes | 25.64
       2 |       yes |             yes |       yes | 25.64
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
       4 |       yes |             yes |       yes | 25.96
       5 |       yes |             yes |       yes | 25.96
       6 |       yes |             yes |       yes | 25.64
       7 |       yes |             yes |       yes | 25.96
time taken 6.407810
time taken 6.412861
+---------------------------------------------------------
| Receive Status - BER
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
| Ckr        | Ch# |       Total_Bits   |    Err_Bit_Cnt_MSB |    Err_Bit_Cnt_LSB |       BER_MSB      |       BER_LSB      |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    hrx_ser |   0 |       188235120896 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   1 |       190183121792 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   2 |       192892017152 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   3 |       193049501184 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   4 |        70757496448 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   5 |        78021073152 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   6 |        85398301184 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   7 |        92685443456 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   hrx_core |   0 |       189107260416 |         4294967295 |         4294967295 |       4.542361e-02 |       4.542361e-02 |
|   hrx_core |   1 |       192914690304 |         4294967295 |         4294967295 |       4.452711e-02 |       4.452711e-02 |
|   hrx_core |   2 |       192978807040 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   3 |       193018372864 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   4 |       193387703808 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   5 |       189109026048 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   6 |       189055562496 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   7 |       188960801792 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   htx_core |   0 |       188839421184 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   1 |       192957155584 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   2 |       192962703104 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   3 |       193412740096 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   4 |       193392177152 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   5 |       189065557248 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   6 |       189008545536 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   7 |       188992578048 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    lrx_ser |   0 |       189114415232 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   1 |       192843997056 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   2 |       192950016384 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   3 |       193408187904 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   4 |        30481106048 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   5 |        41880114304 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   6 |        49067684224 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   7 |        60401346176 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   lrx_core |   0 |       189007176192 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   1 |       192949305856 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   2 |       192861668864 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   3 |       193348891904 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   4 |       193384146688 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   5 |       189124135680 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   6 |       188972441344 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   7 |       188929370112 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   ltx_core |   0 |       188967855616 |         4294967295 |         4294967295 |       4.545712e-02 |       4.545712e-02 |
|   ltx_core |   1 |       192919502080 |         4294967295 |         4294967295 |       4.452600e-02 |       4.452600e-02 |
|   ltx_core |   2 |       192861053696 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   3 |       193400789504 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   4 |       193396227840 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   5 |       189088914176 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   6 |       189048258048 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   7 |       188954327296 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
time taken 8.762870
time taken 8.762880
Example returned success
```
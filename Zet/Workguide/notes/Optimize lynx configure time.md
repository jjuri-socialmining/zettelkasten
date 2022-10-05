  
## Dis I2c
Version 888
```
0.0000 reset_all_bundles start
0.7656 reset_all_bundles end
0.7656 hsc_bundle_init start
hsc_bundle_init PASSED
0.7656 hsc_bundle_init end
0.7656 hsc_bundle_start start
hsc_bundle_start PASSED
1.4065 hsc_bundle_start end
```

  
```
0.0000 hsc_dev_init Start
0.0469 hsc_dev_init end
0.0469 hsc_bundle_init start
hsc_bundle_init PASSED
0.0469 hsc_bundle_init end
0.0469 hsc_bundle_start start
hsc_bundle_start PASSED
0.3925 hsc_bundle_start end
```

## En I2c

```
0.0000 reset_all_bundles start
4.4530 reset_all_bundles end
4.4530 hsc_bundle_init start
hsc_bundle_init PASSED
4.4530 hsc_bundle_init end
4.4530 hsc_bundle_start start
hsc_bundle_start PASSED
7.2028 hsc_bundle_start end
```
  
```
0.0000 hsc_dev_init Start
0.2811 hsc_dev_init end
0.2811 hsc_bundle_init start
hsc_bundle_init PASSED
0.2811 hsc_bundle_init end
0.2811 hsc_bundle_start start
hsc_bundle_start PASSED
2.0007 hsc_bundle_start end
```

## XMLRPC
```
run_traffic()
LYNX DEV====
bundle_teardown()-
time taken 0.011593
time taken 0.154354
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
time taken 0.154446
hsc_bundle_init()
done
time taken 0.156614
hsc_bundle_start()
done
time taken 1.315299
```

```
Use Dev_init startup bundle 7.2s -> 2s
run_traffic()
LYNX DEV====
bundle_teardown()-
time taken 0.009108
time taken 2.801472
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
time taken 2.801552
hsc_bundle_init()
done
time taken 2.803741
hsc_bundle_start()
done
time taken 4.975049
```
## Sum
- replace teardown by dev_init
- remove line 1379 (0.5s/13s)
```
 hsc_prbs_chk_status_query(prbs, &prbs_status);
```

```
PASSED tests\universal\test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal_inject_errors[GEARBOX_4_TO_2_28p125G_PAM_DFE1_RC_DFE2_PRBS31]
PASSED tests\universal\test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal[GEARBOX_4_TO_2_25p78125G_NRZ_DFE1_RC_DFE2_PRBS31]
PASSED tests\universal\test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal_squelch[GEARBOX_4_TO_2_25p78125G_NRZ_DFE1_RC_DFE2_PRBS31]
PASSED tests\universal\test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal_inject_errors[GEARBOX_4_TO_2_25p78125G_NRZ_DFE1_RC_DFE2_PRBS31]
SKIPPED [72] fixtures\capella_fixtures.py:198: Test not supported on this current setup/connections
=========== 2 failed, 484 passed, 72 skipped in 1841.20s (0:30:41) ============
(py310_64)
lab@SJCLab-007248 MINGW64 /c/usr/dutran/regression/capella ((eef836688...))
$ python -u -m pytest -s tests/universal/test_universal_prbs.py --bench lynx_400_bench1 --download_fw on_failure --type_of_regression regular
```

```

API Version 0.8.0.837
API Built on 17 Apr 2022 at 21:59:40 -0800
Teardown by device_init

PASSED tests\universal\test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal_inject_errors[GEARBOX_4_TO_2_28p125G_NRZ_DFE1_RC_DFE2_PRBS31]
SKIPPED [72] fixtures\capella_fixtures.py:198: Test not supported on this current setup/connections
=========== 5 failed, 481 passed, 72 skipped in 1892.58s (0:31:32) ============

PASSED tests\universal\test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal_squelch[GEARBOX_4_TO_2_26p5625G_PAM_DFE1_RC_DFE2_PRBS31]
PASSED tests\universal\test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal_inject_errors[GEARBOX_4_TO_2_26p5625G_PAM_DFE1_RC_DFE2_PRBS31]
SKIPPED [72] fixtures\capella_fixtures.py:198: Test not supported on this current setup/connections
=========== 4 failed, 482 passed, 72 skipped in 1836.50s (0:30:36) ============

```

```
SKIPPED [72] fixtures\capella_fixtures.py:198: Test not supported on this current setup/connections
================ 486 passed, 72 skipped in 1837.11s (0:30:37) =================

```

## Example hsc_ate
- [[bundle_teardown_13.5s.log]]
- [[hsc_dev_init_8.7s.log]]

## Olympus log
```
Connecting to 127.0.0.1:2533
run_traffic()
bundle_teardown()-
time taken 0.000758
time taken 0.142409
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
time taken 0.142505
hsc_bundle_init()
done
time taken 0.142857
hsc_bundle_start()
done
time taken 0.387897
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
time taken 0.611560
time taken 0.611572
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 0
time taken 0.611602
bundle_id = 0, Status: 0
time taken 0.611627
bundle_id = 0, Status: 0
time taken 0.611652
done
time taken 0.611669
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
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 4 rx intf
prbs_checker_config(), chn_idx=4, intf=HRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 5 rx intf
prbs_checker_config(), chn_idx=5, intf=HRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 6 rx intf
prbs_checker_config(), chn_idx=6, intf=HRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 7 rx intf
prbs_checker_config(), chn_idx=7, intf=HRX_SERIAL
________ PRBS lrx serial ckr cfg ___________
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 0 rx intf
prbs_checker_config(), chn_idx=0, intf=LRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 1 rx intf
prbs_checker_config(), chn_idx=1, intf=LRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 2 rx intf
prbs_checker_config(), chn_idx=2, intf=LRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 3 rx intf
prbs_checker_config(), chn_idx=3, intf=LRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 4 rx intf
prbs_checker_config(), chn_idx=4, intf=LRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 5 rx intf
prbs_checker_config(), chn_idx=5, intf=LRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 6 rx intf
prbs_checker_config(), chn_idx=6, intf=LRX_SERIAL
[CRITICAL] cpl_prbs_chk_config: Cannot configure the PRBS checker when the RX is in service but not locked
WARNING: Can not enable checker at channel 7 rx intf
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
time taken 0.632786
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 0
time taken 0.632820
bundle_id = 0, Status: 0
time taken 0.632845
bundle_id = 0, Status: 0
time taken 0.632871
done
time taken 0.632882
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
       0 |        no |              no |        no | 0.00
       1 |        no |              no |        no | 0.00
       2 |        no |              no |        no | 0.00
       3 |        no |              no |        no | 0.00
       4 |       yes |             yes |       yes | 26.31
       5 |       yes |             yes |       yes | 26.31
       6 |       yes |             yes |       yes | 25.96
       7 |       yes |             yes |       yes | 26.31
LTX
  chn_id | fw locked
  -------+------------
       0 |        no
       1 |        no
       2 |        no
       3 |        no
       4 |        no
       5 |        no
       6 |        no
       7 |        no
LRX
  chn_id | fw locked | signal detected | dsp ready | SNR(dB)
  -------+-----------+-----------------+-----------+--------
       0 |        no |             yes |       yes | 0.00
       1 |        no |             yes |       yes | 0.00
       2 |        no |             yes |       yes | 0.00
       3 |        no |              no |        no | 0.00
       4 |        no |              no |        no | 0.00
       5 |        no |              no |        no | 0.00
       6 |        no |              no |        no | 0.00
       7 |        no |              no |        no | 0.00
time taken 1.810363
time taken 1.810810
+---------------------------------------------------------
| Receive Status - BER
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
| Ckr        | Ch# |       Total_Bits   |    Err_Bit_Cnt_MSB |    Err_Bit_Cnt_LSB |       BER_MSB      |       BER_LSB      |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    hrx_ser |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   4 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   5 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   6 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   7 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   hrx_core |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   4 |       119981508608 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   5 |       120003766528 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   6 |       120017517824 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   7 |       119925371648 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   htx_core |   0 |       114180679936 |         4294967295 |         4294967295 |       7.523107e-02 |       7.523107e-02 |
|   htx_core |   1 |       114185771264 |         4294967295 |         4294967295 |       7.522771e-02 |       7.522771e-02 |
|   htx_core |   2 |       114414518528 |         4294967295 |         4294967295 |       7.507731e-02 |       7.507731e-02 |
|   htx_core |   3 |     32768354191360 |         4294967295 |         4294967295 |       2.621412e-04 |       2.621412e-04 |
|   htx_core |   4 |     43198126945536 |         4294967295 |         4294967295 |       1.988497e-04 |       1.988497e-04 |
|   htx_core |   5 |     43207836723712 |         4294967295 |         4294967295 |       1.988050e-04 |       1.988050e-04 |
|   htx_core |   6 |     43204348211712 |         4294967295 |         4294967295 |       1.988211e-04 |       1.988211e-04 |
|   htx_core |   7 |     43213923036160 |         4294967295 |         4294967295 |       1.987770e-04 |       1.987770e-04 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    lrx_ser |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   4 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   5 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   6 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   7 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   lrx_core |   0 |       114180566528 |         4294967295 |         4294967295 |       7.523114e-02 |       7.523114e-02 |
|   lrx_core |   1 |       114185831936 |         4294967295 |         4294967295 |       7.522767e-02 |       7.522767e-02 |
|   lrx_core |   2 |       114414068224 |         4294967295 |         4294967295 |       7.507761e-02 |       7.507761e-02 |
|   lrx_core |   3 |       132497430016 |         4294967295 |         4294967295 |       6.483095e-02 |       6.483095e-02 |
|   lrx_core |   4 |        89821479680 |         3052494318 |         4120035371 |       6.796803e-02 |       9.173831e-02 |
|   lrx_core |   5 |        90910103552 |         3070004174 |         4133176249 |       6.753934e-02 |       9.092886e-02 |
|   lrx_core |   6 |        86935531776 |         3087028668 |         4165199324 |       7.101880e-02 |       9.582271e-02 |
|   lrx_core |   7 |        88019632384 |         3032168389 |         4138957839 |       6.889755e-02 |       9.404624e-02 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   ltx_core |   0 |       118533306880 |         4294967295 |         4294967295 |       7.246853e-02 |       7.246853e-02 |
|   ltx_core |   1 |       118494286336 |         4294967295 |         4294967295 |       7.249239e-02 |       7.249239e-02 |
|   ltx_core |   2 |       113886169088 |         4294967295 |         4294967295 |       7.542562e-02 |       7.542562e-02 |
|   ltx_core |   3 |       113853345280 |         4294967295 |         4294967295 |       7.544736e-02 |       7.544736e-02 |
|   ltx_core |   4 |       120003731968 |                264 |                269 |       4.399863e-09 |       4.483194e-09 |
|   ltx_core |   5 |       120003991808 |                274 |                260 |       4.566515e-09 |       4.333189e-09 |
|   ltx_core |   6 |       119925561600 |                221 |                229 |       3.685620e-09 |       3.819036e-09 |
|   ltx_core |   7 |       119937963008 |                220 |                231 |       3.668563e-09 |       3.851991e-09 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
time taken 2.960460
time taken 2.960470
```



## Olympus log 2
```

```

## Relate
- [[Lynx]]
- [[dev_init_log ignore link ready xmlrpc]]
- [[dev_init_log ignore link ready olympus]]
```
$ ./example.exe 127.0.0.1 50000 run_traffic
Connecting to 127.0.0.1:50000
inphi_xmlrpc_open: resolved hostname to 127.0.0.1
run_traffic()
bundle_teardown()-
time taken 0.007743/(0.007745)
time taken 0.154435/(0.162204)
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
time taken 0.000090/(0.162316)
hsc_bundle_init()
done
time taken 0.002155/(0.164482)
hsc_bundle_start()
done
time taken 0.879414/(1.043911)
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
time taken 0.408461/(1.452393)
time taken 0.000000/(1.452412)
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 0
time taken 5.774829/(7.227254)
bundle_id = 0, Status: 0
time taken 6.015360/(13.242635)
bundle_id = 0, Status: 0
time taken 6.156130/(19.398829)
done
time taken 0.000015/(19.398915)
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
time taken 0.447509/(19.846472)
hsc_bundle_link_ready_wait()
bundle_id = 0, Status: 0
time taken 0.000025/(19.846519)
bundle_id = 0, Status: 0
time taken 0.000018/(19.846555)
bundle_id = 0, Status: 0
time taken 0.000019/(19.846590)
done
time taken 0.000004/(19.846608)
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

time taken 0.805867/(20.652490)
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
       6 |       yes |             yes |       yes | 26.31
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
       6 |       yes |             yes |       yes | 26.31
       7 |       yes |             yes |       yes | 26.69
time taken 1.524770/(22.177279)
time taken 0.000001/(22.177296)
time taken 0.004520/(22.181831)
+---------------------------------------------------------
| Receive Status - BER
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
| Ckr        | Ch# |       Total_Bits   |    Err_Bit_Cnt_MSB |    Err_Bit_Cnt_LSB |       BER_MSB      |       BER_LSB      |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    hrx_ser |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   4 |       183889295744 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   5 |       184569272448 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   6 |       183909779072 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    hrx_ser |   7 |       184550337152 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   hrx_core |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   4 |       184043922432 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   5 |       184582496000 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   6 |       183616490752 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   hrx_core |   7 |       184767973120 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   htx_core |   0 |       183056147456 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   1 |       183722201856 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   2 |       183455350528 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   3 |       183019402496 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   4 |       184310722048 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   5 |       184443462656 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   6 |       183666519296 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   htx_core |   7 |       184837507072 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|    lrx_ser |   0 |       183172004864 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   1 |       183737526912 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   2 |       183295513472 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   3 |       183173752448 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   4 |       184510651264 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   5 |       184367741440 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   6 |       183789974656 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|    lrx_ser |   7 |       184866254336 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   lrx_core |   0 |       183600519680 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   1 |       183758513664 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   2 |       183122150400 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   3 |       183504512768 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   4 |       184598532096 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   5 |       184089268736 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   6 |       184375373824 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   lrx_core |   7 |       184933850368 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
|   ltx_core |   0 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   1 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   2 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   3 |                  0 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   4 |       184614100480 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   5 |       183981009664 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   6 |       184465140480 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
|   ltx_core |   7 |       184923137024 |                  0 |                  0 |       0.000000e+00 |       0.000000e+00 |
+------------+-----+--------------------+--------------------+--------------------+--------------------+--------------------+
time taken 2.265372/(24.447222)
time taken 0.000000/(24.447240)

```
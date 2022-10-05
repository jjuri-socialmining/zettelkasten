API Version (Major.Minor.Revision.Build) 0.9.0.601
API Built on 30 Dec 2021 at 00:10:22 -0800
Application Firmware Version (Major.Minor.Revision.Build) 0.8.0.673

Top Rules
  Die                        0x00000000
  Package                    Spica 800G EML Btm
  Operational Mode           MISSION_MODE
  Protocol Mode              400G_4Px53p1_TO_4Px53p1
  Efuse Driver Override      None
  FW Download Timeout        15000 milli-secs
  FW Warn if Mismatched      True
  VDD HTX                    1.150V
  Mon Clk Enable             False
  LRX QC SNR Thresh mm Enter 17 dB  
  LRX QC SNR Thresh mm Exit  16 dB  
  LRX QC SLC Err Limit       50
  HRX QC SNR Thresh mm Enter 17 dB  
  HRX QC SNR Thresh mm Exit  16 dB  
  HRX QC SLC Err Limit       50
  LRX LOS DSRT Ctrl Startup  200 mV
  LRX LOS ASRT Ctrl Startup  100 mV
  HRX LOS DSRT Ctrl Startup  0x4a
  HRX LOS ASRT Ctrl Startup  0x46
  HRX LOS ASRT Ctrl Datamode 0x46
  SFEC Mode                  Disabled
  SFEC Config                4_X_50

Bundle Rules
  Bundle                     0
  Line Ch Map                0x001e
  Host Ch Map                0x001e

FEC Rules
  Enable                     False
  Interface                  ING
  Mode                       FEC_BYPASS
  FEC Type (IN)              KP
  Data Rate (Nominal)        400G
  Number of Channels (IN)    4
  Number of Channels (OUT)   4
  Loopback Input Config      Off
  Loopback Output Config     Off

OTX XBR Rules     |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Source Ch 1     |       1|       2|       3|       4|
  Source Ch 2     |       f|       f|       f|       f|
  Source Ch 3     |       f|       f|       f|       f|
  Source Ch 4     |       f|       f|       f|       f|

MTX XBR Rules     |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Source Ch 1     |       1|       2|       3|       4|
  Interleave      |       0|       0|       0|       0|

OTX CLK XBR Rules |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Clk Source Ch   |       1|       2|       3|       4|

MTX CLK XBR Rules |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Clk Source Ch   |       1|       2|       3|       4|

ORX Ch Rules      |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  Baud Rate (GBd) |    Unkn|    Unkn|    Unkn|    Unkn|
  IEEE Demap      |    True|   False|   False|   False|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  DSP Mode        |  SLC+RC|  SLC+RC|  SLC+RC|  SLC+RC|
  DFE Precoder En |   False|   False|   False|   False|
  AFE Trim        |    Auto|    Auto|    Auto|    Auto|
  MSLD En         |   False|   False|   False|   False|
  VGA Tracking    |   False|   False|   False|   False|
  VGA Threshold   |  Stndrd|  Stndrd|  Stndrd|  Stndrd|
  ADC Startup     |  Stndrd|  Stndrd|  Stndrd|  Stndrd|
  CMI Mode        |      AC|      AC|      AC|      AC|
  DTL Mode        |    Auto|    Auto|    Auto|    Auto|
  PGA Att En      |    True|    True|    True|    True|
  Preamp Bias Ctl |  0x0000|  0x0000|  0x0000|  0x0000|
  ADV FFE Leak    |  0x0004|  0x0004|  0x0004|  0x0004|
  ADV FIR Ad Fc   |   False|   False|   False|   False|
  ADV Gain Ad Fc  |   False|   False|   False|   False|
  ADV DC Ad Fc    |   False|   False|   False|   False|
  ADV Skp DSP F T |   False|   False|   False|   False|

OTX Ch Rules      |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  Baud Rate       |    Unkn|    Unkn|    Unkn|    Unkn|
  Squelch Lock    |    True|    True|   False|    True|
  LUT Mode        | 7TapLIN| 7TapLIN| 7TapLIN| 7TapLIN|
  IEEE Demap      |    True|    True|   False|   False|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  Tx Swing        |   100 %|   100 %|   100 %|   100 %|
  SiPho Swing     |   2.50V|   2.50V|   2.50V|   2.50V|
  SiPho 1Vpp 85 O |   False|   False|   False|   False|
  DFE Precoder En |   False|   False|   False|   False|
  FIR Tap 1       |     -50|     -50|     -50|     -50|
  FIR Tap 2       |     750|     750|     750|     750|
  FIR Tap 3       |      50|      50|      50|      50|
  FIR Tap 4       |       0|       0|       0|       0|
  FIR Tap 5       |       0|       0|       0|       0|
  FIR Tap 6       |       0|       0|       0|       0|
  FIR Tap 7       |       0|       0|       0|       0|
  Inner Eye 1     |    1380|    1380|    1380|    1380|
  Inner Eye 2     |    2230|    2230|    2230|    2230|
  SiPho Amp Cal   |   False|   False|   False|   False|

MRX Ch Rules      |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  IEEE Demap      |   False|   False|    True|    True|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  Baud Rate (GBd) |    Unkn|    Unkn|    Unkn|    Unkn|
  Force Mission M |   False|   False|   False|   False|
  FFE Con Dif En  |    True|    True|    True|    True|
  BW Idx Max      |  0x0006|  0x0006|  0x0006|  0x0006|
  VGA1 Tr Period  |  0x0004|  0x0004|  0x0004|  0x0004|
  Alg1 Dis        |   False|   False|   False|   False|
  Alg2 Dis        |   False|   False|   False|   False|
  Alg3 Dis        |   False|   False|   False|   False|
  Alg4 Dis        |   False|   False|   False|   False|
  Restart LOS Dis |   False|   False|   False|   False|
  Fixed Gamma Dis |   False|   False|   False|   False|
  QC All Dis      |   False|   False|   False|   False|
  QC Hist Dis     |   False|   False|   False|   False|
  QC Slc Dis      |   False|   False|   False|   False|
  QC SNR Dis      |   False|   False|   False|   False|
  Phase Val       |  0x0000|  0x0000|  0x0000|  0x0000|
  Force Phase     |   False|   False|   False|   False|
  Outer Phase Del |  0x0000|  0x0000|  0x0000|  0x0000|
  Inner Phase Del |  0x0000|  0x0000|  0x0000|  0x0000|
  Phase Pre1 Val  |       0|       0|       0|       0|

MTX Ch Rules      |     Ch1|     Ch2|     Ch3|     Ch4|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  Baud Rate       |    Unkn|    Unkn|    Unkn|    Unkn|
  Squelch Lock    |   False|   False|   False|   False|
  LUT Mode        |    4Tap|    4Tap|    4Tap|    4Tap|
  IEEE Demap      |   False|   False|   False|   False|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  Tx Swing        |   100 %|   100 %|   100 %|   100 %|
  Max Swing VDD   |   False|   False|   False|   False|
  DFE Precoder En |   False|   False|   False|   False|
  FIR Tap 1       |     -30|     -30|     -30|     -30|
  FIR Tap 2       |     400|     400|     400|     400|
  FIR Tap 3       |     -30|     -30|     -30|     -30|
  FIR Tap 4       |       0|       0|       0|       0|
  FIR Tap 5       |       0|       0|       0|       0|
  FIR Tap 6       |       0|       0|       0|       0|
  FIR Tap 7       |       0|       0|       0|       0|
  Inner Eye 1     |    1000|    1000|    1000|    1000|
  Inner Eye 2     |    2000|    2000|    2000|    2000|


API Version (Major.Minor.Revision.Build) 0.9.0.601
API Built on 30 Dec 2021 at 00:10:22 -0800
Application Firmware Version (Major.Minor.Revision.Build) 0.8.0.673

Top Rules
  Die                        0x00000000
  Package                    Spica 800G EML Btm
  Operational Mode           MISSION_MODE
  Protocol Mode              400G_4Px53p1_TO_4Px53p1
  Efuse Driver Override      None
  FW Download Timeout        15000 milli-secs
  FW Warn if Mismatched      True
  VDD HTX                    1.150V
  Mon Clk Enable             False
  LRX QC SNR Thresh mm Enter 17 dB  
  LRX QC SNR Thresh mm Exit  16 dB  
  LRX QC SLC Err Limit       50
  HRX QC SNR Thresh mm Enter 17 dB  
  HRX QC SNR Thresh mm Exit  16 dB  
  HRX QC SLC Err Limit       50
  LRX LOS DSRT Ctrl Startup  200 mV
  LRX LOS ASRT Ctrl Startup  100 mV
  HRX LOS DSRT Ctrl Startup  0x4a
  HRX LOS ASRT Ctrl Startup  0x46
  HRX LOS ASRT Ctrl Datamode 0x46
  SFEC Mode                  Disabled
  SFEC Config                4_X_50

Bundle Rules
  Bundle                     1
  Line Ch Map                0x01e0
  Host Ch Map                0x01e0

FEC Rules
  Enable                     False
  Interface                  ING
  Mode                       FEC_BYPASS
  FEC Type (IN)              KP
  Data Rate (Nominal)        400G
  Number of Channels (IN)    4
  Number of Channels (OUT)   4
  Loopback Input Config      Off
  Loopback Output Config     Off

OTX XBR Rules     |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Source Ch 1     |       5|       6|       7|       8|
  Source Ch 2     |       f|       f|       f|       f|
  Source Ch 3     |       f|       f|       f|       f|
  Source Ch 4     |       f|       f|       f|       f|

MTX XBR Rules     |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Source Ch 1     |       5|       6|       7|       8|
  Interleave      |       0|       0|       0|       0|

OTX CLK XBR Rules |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Clk Source Ch   |       5|       6|       7|       8|

MTX CLK XBR Rules |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Clk Source Ch   |       5|       6|       7|       8|

ORX Ch Rules      |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  Baud Rate (GBd) |    Unkn|    Unkn|    Unkn|    Unkn|
  IEEE Demap      |    True|    True|    True|   False|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  DSP Mode        |  SLC+RC|  SLC+RC|  SLC+RC|  SLC+RC|
  DFE Precoder En |   False|   False|   False|   False|
  AFE Trim        |    Auto|    Auto|    Auto|    Auto|
  MSLD En         |   False|   False|   False|   False|
  VGA Tracking    |   False|   False|   False|   False|
  VGA Threshold   |  Stndrd|  Stndrd|  Stndrd|  Stndrd|
  ADC Startup     |  Stndrd|  Stndrd|  Stndrd|  Stndrd|
  CMI Mode        |      AC|      AC|      AC|      AC|
  DTL Mode        |    Auto|    Auto|    Auto|    Auto|
  PGA Att En      |    True|    True|    True|    True|
  Preamp Bias Ctl |  0x0000|  0x0000|  0x0000|  0x0000|
  ADV FFE Leak    |  0x0004|  0x0004|  0x0004|  0x0004|
  ADV FIR Ad Fc   |   False|   False|   False|   False|
  ADV Gain Ad Fc  |   False|   False|   False|   False|
  ADV DC Ad Fc    |   False|   False|   False|   False|
  ADV Skp DSP F T |   False|   False|   False|   False|

OTX Ch Rules      |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  Baud Rate       |    Unkn|    Unkn|    Unkn|    Unkn|
  Squelch Lock    |   False|   False|   False|   False|
  LUT Mode        | 7TapLIN| 7TapLIN| 7TapLIN| 7TapLIN|
  IEEE Demap      |   False|   False|   False|   False|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  Tx Swing        |   100 %|   100 %|   100 %|   100 %|
  SiPho Swing     |   2.50V|   2.75V|   2.75V|   2.50V|
  SiPho 1Vpp 85 O |   False|   False|   False|   False|
  DFE Precoder En |   False|   False|   False|   False|
  FIR Tap 1       |     -50|     -50|     -50|     -50|
  FIR Tap 2       |     750|     750|     750|     750|
  FIR Tap 3       |      50|      50|      50|      50|
  FIR Tap 4       |       0|       0|       0|       0|
  FIR Tap 5       |       0|       0|       0|       0|
  FIR Tap 6       |       0|       0|       0|       0|
  FIR Tap 7       |       0|       0|       0|       0|
  Inner Eye 1     |    1380|    1380|    1380|    1380|
  Inner Eye 2     |    2230|    2230|    2230|    2230|
  SiPho Amp Cal   |   False|   False|   False|   False|

MRX Ch Rules      |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  IEEE Demap      |    True|    True|   False|   False|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  Baud Rate (GBd) |    Unkn|    Unkn|    Unkn|    Unkn|
  Force Mission M |   False|   False|   False|   False|
  FFE Con Dif En  |    True|    True|    True|    True|
  BW Idx Max      |  0x0006|  0x0006|  0x0006|  0x0006|
  VGA1 Tr Period  |  0x0004|  0x0004|  0x0004|  0x0004|
  Alg1 Dis        |   False|   False|   False|   False|
  Alg2 Dis        |   False|   False|   False|   False|
  Alg3 Dis        |   False|   False|   False|   False|
  Alg4 Dis        |   False|   False|   False|   False|
  Restart LOS Dis |   False|   False|   False|   False|
  Fixed Gamma Dis |   False|   False|   False|   False|
  QC All Dis      |   False|   False|   False|   False|
  QC Hist Dis     |   False|   False|   False|   False|
  QC Slc Dis      |   False|   False|   False|   False|
  QC SNR Dis      |   False|   False|   False|   False|
  Phase Val       |  0x0000|  0x0000|  0x0000|  0x0000|
  Force Phase     |   False|   False|   False|   False|
  Outer Phase Del |  0x0000|  0x0000|  0x0000|  0x0000|
  Inner Phase Del |  0x0000|  0x0000|  0x0000|  0x0000|
  Phase Pre1 Val  |       0|       0|       0|       0|

MTX Ch Rules      |     Ch5|     Ch6|     Ch7|     Ch8|
------------------+--------+--------+--------+--------+
  Ch Enable       |    True|    True|    True|    True|
  Signalling      |     PAM|     PAM|     PAM|     PAM|
  Baud Rate       |    Unkn|    Unkn|    Unkn|    Unkn|
  Squelch Lock    |   False|   False|   False|   False|
  LUT Mode        |    4Tap|    4Tap|    4Tap|    4Tap|
  IEEE Demap      |   False|   False|   False|   False|
  Gray Mapping    |    True|    True|    True|    True|
  Invert Ch       |   False|   False|   False|   False|
  Tx Swing        |   100 %|   100 %|   100 %|   100 %|
  Max Swing VDD   |   False|   False|   False|   False|
  DFE Precoder En |   False|   False|   False|   False|
  FIR Tap 1       |     -30|     -30|     -30|     -30|
  FIR Tap 2       |     400|     400|     400|     400|
  FIR Tap 3       |     -30|     -30|     -30|     -30|
  FIR Tap 4       |       0|       0|       0|       0|
  FIR Tap 5       |       0|       0|       0|       0|
  FIR Tap 6       |       0|       0|       0|       0|
  FIR Tap 7       |       0|       0|       0|       0|
  Inner Eye 1     |    1000|    1000|    1000|    1000|
  Inner Eye 2     |    2000|    2000|    2000|    2000|


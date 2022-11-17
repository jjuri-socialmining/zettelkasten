```shell

(C:\Users\lab\anaconda2) C:\Users\lab>activate py37

(py37) C:\Users\lab>ipython -i module.py
Python 3.7.3 (default, Apr 24 2019, 13:20:13) [MSC v.1915 32 bit (Intel)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.
[TerminalIPythonApp] WARNING | File not found: 'module.py'

In [1]: import Olympus as o

In [2]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 1
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 1
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 1
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 1
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [3]: o.gpio('PHYADR0', 0)

In [4]: o.gpio('PHYADR1', 0)

In [5]: o.gpio('PHYADR2', 0)

In [6]: o.gpio('PHYADR3', 0)

In [7]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [8]: o.gpio('I2CSEL', 1)

In [9]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [10]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 1
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 1
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 1
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 1
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [11]: o.gpio('I2CSEL',1)

In [12]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 1
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 1
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 1
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 1
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [13]: o.gpio('PHYADR0',0)

In [14]: o.gpio('PHYADR1',0)

In [15]: o.gpio('PHYADR2',0)

In [16]: o.gpio('PHYADR3',0)

In [17]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [18]: o.ResetTarget()
Out[18]: (1, 1)

In [19]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INfPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [20]: o.SerialInterface(rate=0.1, protocol='I2C', clocktype='Normal')
Out[20]: [0.05, 1, 0]

In [21]: o.rdh(addr=0x80002)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-21-f16fd2172544> in <module>
----> 1 o.rdh(addr=0x80002)

TypeError: rd() missing required argument 'address' (pos 1)

In [22]: o.rdh(address=0x80002)
Out[22]: '0x0210'

In [23]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[23]: [0.05, 15, 2]

In [24]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 1
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 1
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 1
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 1
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 1
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [25]: o.rdh(addr=0x80002)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-25-f16fd2172544> in <module>
----> 1 o.rdh(addr=0x80002)

TypeError: rd() missing required argument 'address' (pos 1)

In [26]: o.rdh(address=0x80002)
Out[26]: '0xFFFF'

In [27]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 1
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 1
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 1
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 1
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 1
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [28]: o.gpio('I2CSEL',1)

In [29]: o.gpio('PHYADR0',0)

In [30]: o.gpio('PHYADR1',0)

In [31]: o.gpio('PHYADR2',0)

In [32]: o.gpio('PHYADR',0)
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
<ipython-input-32-c5347fa9ec4f> in <module>
----> 1 o.gpio('PHYADR',0)

error: gpio(): Invalid GPIO name PHYADR

In [33]: o.gpio('PHYADR3',0)

In [34]: o.rdh(address=0x80002)
Out[34]: '0xFFFF'

In [35]: o.ResetTarget()
Out[35]: (1, 1)

In [36]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[36]: [6.5, 15, 2]

In [37]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [38]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [39]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [40]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [41]: o.gpio('SELF',1)

In [42]: o.ResetTarget()
Out[42]: (1, 1)

In [43]: o.gpio('SELF',1)

In [44]: o.ResetTarget()
Out[44]: (1, 1)

In [45]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 1
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [46]: o.gpio('SELF',0)

In [47]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [48]: o.ResetTarget()
Out[48]: (1, 1)

In [49]: o.gpio('SELF',1)

In [50]: o.ResetTarget()
Out[50]: (1, 1)

In [51]: o.ResetTarget()
Out[51]: (1, 1)

In [52]: o.gpio('SELF', 2)

In [53]: o.ResetTarget(2, 2)
Out[53]: (2, 2)

In [54]: o.ResetTarget()
Out[54]: (1, 1)

In [55]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 INPUT  Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [56]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 INPUT  Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [57]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[57]: [6.5, 15, 2]

In [58]: o.gpio('SELF',1)

In [59]: o.ResetTarget()
Out[59]: (1, 1)

In [60]: o.gpio('SELF',1)

In [61]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[61]: [6.5, 15, 2]

In [62]: o.gpio('SELF',0)

In [63]: o.SerialInterface(rate=6.5, protocol='MDIO', clocktype='Normal')
Out[63]: [6.5, 0, 0]

In [64]: o.gpio('PHYADR0', 1)
    ...: o.gpio('PHYADR1', 1)
    ...: o.gpio('PHYADR2', 1)
    ...: o.gpio('PHYADR3', 1)
    ...: o.gpio('I2CSEL', 0)

In [65]: o.SerialInterface(rate=0.1, protocol='I2C', clocktype='Normal')
Out[65]: [0.05, 1, 0]

In [66]: o.gpio('PHYADR0', 0)
    ...: o.gpio('PHYADR1', 0)
    ...: o.gpio('PHYADR2', 0)
    ...: o.gpio('PHYADR3', 0)
    ...: o.gpio('I2CSEL', 1)

In [67]: o.ResetTarget()
Out[67]: (1, 1)

In [68]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[68]: [0.05, 15, 2]

In [69]: o.gpio('SELF',1)

In [70]: o.SerialInterface(rate=6.5, protocol='MDIO', clocktype='Normal')
Out[70]: [6.5, 0, 0]

In [71]: o.gpio('PHYADR0', 1)
    ...: o.gpio('PHYADR1', 1)
    ...: o.gpio('PHYADR2', 1)
    ...: o.gpio('PHYADR3', 1)
    ...: o.gpio('I2CSEL', 0)

In [72]: o.gpio('SELF',0)

In [73]: o.gpio('SELF',1)

In [74]: o.ResetTarget()
Out[74]: (1, 1)

In [75]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 1
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 1
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 1
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 1
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 1
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [76]: o.gpio('SELF',0)

In [77]: o.gpio('SELF',1)

In [78]: o.SerialInterface(rate=0.1, protocol='I2C', clocktype='Normal')
Out[78]: [0.05, 1, 0]

In [79]: o.gpio('PHYADR0', 0)
    ...: o.gpio('PHYADR1', 0)
    ...: o.gpio('PHYADR2', 0)
    ...: o.gpio('PHYADR3', 0)
    ...: o.gpio('I2CSEL', 1)

In [80]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[80]: [0.05, 15, 2]

In [81]: o.ResetTarget()
Out[81]: (1, 1)

In [82]: o.gpio('SELF',0)

In [83]: o.SerialInterface(rate=6.5, protocol='MDIO', clocktype='Normal')
Out[83]: [6.5, 0, 0]

In [84]: o.gpio('PHYADR0', 1)
    ...: o.gpio('PHYADR1', 1)
    ...: o.gpio('PHYADR2', 1)
    ...: o.gpio('PHYADR3', 1)
    ...: o.gpio('I2CSEL', 0)

In [85]: o.SerialInterface(rate=0.1, protocol='I2C', clocktype='Normal')
Out[85]: [0.05, 1, 0]

In [86]: o.gpio('PHYADR0', 0)
    ...: o.gpio('PHYADR1', 0)
    ...: o.gpio('PHYADR2', 0)
    ...: o.gpio('PHYADR3', 0)
    ...: o.gpio('I2CSEL', 1)

In [87]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[87]: [0.05, 15, 2]

In [88]: o.ResetTarget()
Out[88]: (1, 1)

In [89]: o.gpio('SELF',1)

In [90]: o.SerialInterface(rate=6.5, protocol='MDIO', clocktype='Normal')
Out[90]: [6.5, 0, 0]

In [91]: o.gpio('PHYADR0', 1)
    ...: o.gpio('PHYADR1', 1)
    ...: o.gpio('PHYADR2', 1)
    ...: o.gpio('PHYADR3', 1)
    ...: o.gpio('I2CSEL', 0)

In [92]: o.gpio('SELF',0)

In [93]: o.gpio('SELF',1)

In [94]: o.ResetTarget()
Out[94]: (1, 1)

In [95]: o.SerialInterface(rate=0.1, protocol='I2C', clocktype='Normal')
Out[95]: [0.05, 1, 0]

In [96]: o.gpio('PHYADR0', 0)
    ...: o.gpio('PHYADR1', 0)
    ...: o.gpio('PHYADR2', 0)
    ...: o.gpio('PHYADR3', 0)
    ...: o.gpio('I2CSEL', 1)

In [97]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[97]: [0.05, 15, 2]

In [98]: o.ResetTarget()
Out[98]: (1, 1)

In [99]: o.ResetTarget()
Out[99]: (1, 1)

In [100]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 1
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [101]: o.gpio('SELF',0)

In [102]: o.gpio('SELF',1)

In [103]: o.gpio('SELF',0)

In [104]: o.SerialInterface(rate=0.1, protocol='I2C', clocktype='Normal')
Out[104]: [0.05, 1, 0]

In [105]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 0
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 0
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 0
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 0
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 1
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [106]: o.SerialInterface(rate=6.5, protocol='MDIO', clocktype='Normal')
Out[106]: [6.5, 0, 0]

In [107]: o.gpio('PHYADR0', 1)
     ...: o.gpio('PHYADR1', 1)
     ...: o.gpio('PHYADR2', 1)
     ...: o.gpio('PHYADR3', 1)
     ...: o.gpio('I2CSEL', 0)

In [108]: o.gpio("ListAll")

Available GPIO names for Olympus System Number: 0, S/N: 952, Name: Board 0

    '             PHYADR4' - Port 0 Position  00 OUTPUT Value 0
    '                SELF' - Port 0 Position  01 OUTPUT Value 0
    '             PHYADR0' - Port 0 Position  02 OUTPUT Value 1
    '               GPIO3' - Port 0 Position  03 INPUT  Value 0
    '              WP_N_M' - Port 0 Position  04 INPUT  Value 0
    '               GPIO5' - Port 0 Position  05 INPUT  Value 0
    '               GPIO6' - Port 0 Position  06 INPUT  Value 0
    '               GPIO0' - Port 0 Position  07 INPUT  Value 0
    '             PHYADR2' - Port 0 Position  16 OUTPUT Value 1
    '             PHYADR3' - Port 0 Position  17 OUTPUT Value 1
    '             PHYADR1' - Port 0 Position  18 OUTPUT Value 1
    '              INTR_N' - Port 0 Position  19 INPUT  Value 0
    '                LOL0' - Port 0 Position  20 INPUT  Value 0
    '              I2CSEL' - Port 0 Position  21 OUTPUT Value 0
    '               GPIO2' - Port 0 Position  22 INPUT  Value 0
    '               GPIO1' - Port 0 Position  23 INPUT  Value 0
    '               GPIO4' - Port 0 Position  24 INPUT  Value 0
    '                 G27' - Port 0 Position  27 INPUT  Value 0
    '               ALERT' - Port 0 Position  28 INPUT  Value 0
    '               THERM' - Port 0 Position  29 INPUT  Value 1

    '            JTAG_DIS' - Port 1 Position  00 OUTPUT Value 0
    '              TRST_N' - Port 1 Position  01 INPUT  Value 0

    '             SPI_SEL' - Port 2 Position  00 OUTPUT Value 0
    '          MDIO_SEL_M' - Port 2 Position  03 OUTPUT Value 0
    '             EN5VFAN' - Port 2 Position  04 OUTPUT Value 1
    '              SW_RUN' - Port 2 Position  05 OUTPUT Value 1
    '             VAUXEN0' - Port 2 Position  06 OUTPUT Value 1
    '             VAUXEN2' - Port 2 Position  07 OUTPUT Value 1

In [109]: o.ResetTarget()
Out[109]: (1, 1)

In [110]: o.gpio('SELF',1)

In [111]: o.ResetTarget()
Out[111]: (1, 1)

In [112]: o.gpio('SELF',1)

In [113]: o.SerialInterface(rate=0.1, protocol='I2C', clocktype='Normal')
Out[113]: [0.05, 1, 0]

In [114]: o.gpio('PHYADR0', 0)
     ...: o.gpio('PHYADR1', 0)
     ...: o.gpio('PHYADR2', 0)
     ...: o.gpio('PHYADR3', 0)
     ...: o.gpio('I2CSEL', 1)

In [115]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[115]: [0.05, 15, 2]

In [116]: o.ResetTtarget(2,2)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-116-64deb29f91c1> in <module>
----> 1 o.ResetTtarget(2,2)

AttributeError: module 'Olympus' has no attribute 'ResetTtarget'

In [117]: o.ResetTarget(2,2)
Out[117]: (2, 2)

In [118]: o.SerialInterface(protocol='Disable', clocktype='Tristate')
Out[118]: [0.05, 15, 2]

In [119]: o.ResetTarget()
Out[119]: (1, 1)

In [120]: o.ResetTarget()
Out[120]: (1, 1)

In [121]: o.gpio('SELF',0)

In [122]: o.gpio('SELF',1)

In [123]: o.ResetTarget()
Out[123]: (1, 1)

In [124]: o.ResetTarget(2,2)
Out[124]: (2, 2)

In [125]: o.gpio('SELF',2)

In [126]: o.ResetTarget()
Out[126]: (1, 1)

In [127]:
```
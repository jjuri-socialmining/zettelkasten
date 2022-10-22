```python
# Import register and API
# from spica5n.python27 import spica_registers as reg
# from spica5n.python27 import spica_api as capi
from spica5n.python import spica_registers as reg

#from spica5n.python import spica_api as capi


# SPICA5N Chip ID
die     = 0
lane    = 3
print("SPICA5N LO = 0x%04x on Die %d" % (reg.ODSP_MMD30_DEVICE_ID_LOW__READ(die), die))
print("SPICA5N HI = 0x%04x on Die %d" % (reg.ODSP_MMD30_DEVICE_ID_HIGH__READ(die), die))


print("SPICA5N LO = 0x%04x on Die %d" % (reg.ODSP_MMD30_DEVICE_ID_LOW__READ(die), die))
print("SPICA5N HI = 0x%04x on Die %d" % (reg.ODSP_MMD30_DEVICE_ID_HIGH__READ(die), die))

#Configure PFL
reg.ODSP_MMD30_PFL_EN_MRX0_CFG__WRITE(die, 0x6)
reg.ODSP_MMD30_PFL_EN_MTX0_CFG__WRITE(die, 0x6)

print("read ODSP_MMD30_PFL_EN_MRX0_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MRX0_CFG__READ(die))
print("read ODSP_MMD30_PFL_EN_MTX0_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MTX0_CFG__READ(die))

reg.ODSP_MMD30_PFL_EN_MRX1_CFG__WRITE(die, 0x6)
reg.ODSP_MMD30_PFL_EN_MTX1_CFG__WRITE(die, 0x6)

print("read ODSP_MMD30_PFL_EN_MRX1_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MRX1_CFG__READ(die))
print("read ODSP_MMD30_PFL_EN_MTX1_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MTX1_CFG__READ(die))

reg.ODSP_MMD30_PFL_EN_MRX2_CFG__WRITE(die, 0x6)
reg.ODSP_MMD30_PFL_EN_MTX2_CFG__WRITE(die, 0x6)

print("read ODSP_MMD30_PFL_EN_MRX2_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MRX2_CFG__READ(die))
print("read ODSP_MMD30_PFL_EN_MTX2_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MTX2_CFG__READ(die))

reg.ODSP_MMD30_PFL_EN_MRX3_CFG__WRITE(die, 0x6)
reg.ODSP_MMD30_PFL_EN_MTX3_CFG__WRITE(die, 0x6)

print("read ODSP_MMD30_PFL_EN_MRX3_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MRX3_CFG__READ(die))
print("read ODSP_MMD30_PFL_EN_MTX3_CFG data 0x%04x" % reg.ODSP_MMD30_PFL_EN_MTX3_CFG__READ(die))

## scritture_spica.py is generated from scritture_spica.txt
## from odsp_api import *
## import spica5_registers_private as reg
def one_lane_pmr_setup(die=0, chn=0):
    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_AFE_CTRL1_CFG', hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__ADDRESS), '00017808', hex(0x00008160)))
    reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__WRITE(die, chn, 0x00008160)
    data1 = reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__READ(die, chn)
    if 0x00008160 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__ADDRESS), hex(0x00008160), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x0000c004)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x0000c004)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x0000c004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x0000c004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x00000004)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_TOP_RESET', hex(reg.ODSP_PMR_RX_TOP_RESET__ADDRESS), '00017000', hex(0x00000000)))
    reg.ODSP_PMR_RX_TOP_RESET__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_TOP_RESET__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_TOP_RESET__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_RESET', hex(reg.ODSP_PMR_TX_TX_TOP_RESET__ADDRESS), '00029000', hex(0x00000000)))
    reg.ODSP_PMR_TX_TX_TOP_RESET__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_TX_TOP_RESET__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_RESET__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_TOP_GEN_CFG', hex(reg.ODSP_PMR_RX_TOP_GEN_CFG__ADDRESS), '00017001', hex(0x00000001)))
    reg.ODSP_PMR_RX_TOP_GEN_CFG__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_TOP_GEN_CFG__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_TOP_GEN_CFG__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG', hex(reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__ADDRESS), '00017200', hex(0x00000002)))
    reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__WRITE(die, chn, 0x00000002)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__READ(die, chn)
    if 0x00000002 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__ADDRESS), hex(0x00000002), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), '000172b4', hex(0x00004200)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__WRITE(die, chn, 0x00004200)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__READ(die, chn)
    if 0x00004200 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), hex(0x00004200), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG', hex(reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__ADDRESS), '00017202', hex(0x00000107)))
    reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__WRITE(die, chn, 0x00000107)
    data1 = reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__READ(die, chn)
    if 0x00000107 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__ADDRESS), hex(0x00000107), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG', hex(reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__ADDRESS), '0001720f', hex(0x00000040)))
    reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__WRITE(die, chn, 0x00000040)
    data1 = reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__READ(die, chn)
    if 0x00000040 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__ADDRESS), hex(0x00000040), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG', hex(reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__ADDRESS), '00017265', hex(0x00000027)))
    reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__WRITE(die, chn, 0x00000027)
    data1 = reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__READ(die, chn)
    if 0x00000027 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__ADDRESS), hex(0x00000027), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PAM4_DFE_F1_INITIAL_CFG', hex(reg.ODSP_PMR_RX_DSP_PAM4_DFE_F1_INITIAL_CFG__ADDRESS), '00017256', hex(0x00000000)))
    reg.ODSP_PMR_RX_DSP_PAM4_DFE_F1_INITIAL_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_DSP_PAM4_DFE_F1_INITIAL_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PAM4_DFE_F1_INITIAL_CFG__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG', hex(reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__ADDRESS), '0001723a', hex(0x00000003)))
    reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__WRITE(die, chn, 0x00000003)
    data1 = reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__READ(die, chn)
    if 0x00000003 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__ADDRESS), hex(0x00000003), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_FFE_GAIN_INITIAL_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_FFE_GAIN_INITIAL_CFG__ADDRESS), '00017406', hex(0x0000900d)))
    reg.ODSP_PMR_RX_DSP_STM_FFE_GAIN_INITIAL_CFG__WRITE(die, chn, 0x0000900d)
    data1 = reg.ODSP_PMR_RX_DSP_STM_FFE_GAIN_INITIAL_CFG__READ(die, chn)
    if 0x0000900d != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_FFE_GAIN_INITIAL_CFG__ADDRESS), hex(0x0000900d), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_STM_CFG1', hex(reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__ADDRESS), '00017408', hex(0x00000c00)))
    reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__WRITE(die, chn, 0x00000c00)
    data1 = reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__READ(die, chn)
    if 0x00000c00 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__ADDRESS), hex(0x00000c00), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_GC_CHK_PRBS_CFG', hex(reg.ODSP_PMR_RX_GC_CHK_PRBS_CFG__ADDRESS), '00017500', hex(0x00000001)))
    reg.ODSP_PMR_RX_GC_CHK_PRBS_CFG__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_GC_CHK_PRBS_CFG__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_GC_CHK_PRBS_CFG__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__ADDRESS), '00017730', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__ADDRESS), '0001774f', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__ADDRESS), '00017750', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__ADDRESS), '00017751', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__ADDRESS), '00017752', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__ADDRESS), '00017753', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__ADDRESS), '00017736', hex(0x0000003f)))
    reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__WRITE(die, chn, 0x0000003f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__READ(die, chn)
    if 0x0000003f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__ADDRESS), hex(0x0000003f), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__ADDRESS), '00017737', hex(0x00000030)))
    reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__WRITE(die, chn, 0x00000030)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__READ(die, chn)
    if 0x00000030 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__ADDRESS), hex(0x00000030), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3', hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__ADDRESS), '00017738', hex(0x0000000f)))
    reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__ADDRESS), hex(0x0000000f), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__ADDRESS), '00017755', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__ADDRESS), '00017756', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_TDC_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__ADDRESS), '00017742', hex(0x00000007)))
    reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__WRITE(die, chn, 0x00000007)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__READ(die, chn)
    if 0x00000007 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__ADDRESS), hex(0x00000007), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_VCO_CFG6', hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__ADDRESS), '0001772d', hex(0x00000019)))
    reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__WRITE(die, chn, 0x00000019)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__READ(die, chn)
    if 0x00000019 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__ADDRESS), hex(0x00000019), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_VCO_CFG7', hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__ADDRESS), '0001772e', hex(0x00000099)))
    reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__WRITE(die, chn, 0x00000099)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__READ(die, chn)
    if 0x00000099 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__ADDRESS), hex(0x00000099), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), '000176c9', hex(0x000000cf)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__WRITE(die, chn, 0x000000cf)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__READ(die, chn)
    if 0x000000cf != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), hex(0x000000cf), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), '000176ca', hex(0x000000f3)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__WRITE(die, chn, 0x000000f3)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__READ(die, chn)
    if 0x000000f3 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), hex(0x000000f3), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), '000176cb', hex(0x0000003c)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__WRITE(die, chn, 0x0000003c)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__READ(die, chn)
    if 0x0000003c != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), hex(0x0000003c), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_PIOC_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_PIOC_CFG1__ADDRESS), '000176c7', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_PIOC_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_PIOC_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_PIOC_CFG1__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8', hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__ADDRESS), '00017702', hex(0x00000011)))
    reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__ADDRESS), hex(0x00000011), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__ADDRESS), '0001762e', hex(0x00000013)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__WRITE(die, chn, 0x00000013)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__READ(die, chn)
    if 0x00000013 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__ADDRESS), hex(0x00000013), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__ADDRESS), '00017645', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__ADDRESS), '0001764b', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__ADDRESS), '00017651', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__ADDRESS), '00017656', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__ADDRESS), '00017657', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__ADDRESS), '00017642', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__ADDRESS), '00017648', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__ADDRESS), '0001764e', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__ADDRESS), '00017653', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__ADDRESS), '00017654', hex(0x00000008)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__ADDRESS), hex(0x00000008), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_LD_CNT_TOL_CFG', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__ADDRESS), '0001765c', hex(0x00000011)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__ADDRESS), hex(0x00000011), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_LD_NUM_ITER_CFG', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__ADDRESS), '0001765b', hex(0x00000011)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__ADDRESS), hex(0x00000011), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), '00017607', hex(0x0000000f)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), '00017608', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), '0001760c', hex(0x000000c8)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__WRITE(die, chn, 0x000000c8)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__READ(die, chn)
    if 0x000000c8 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), hex(0x000000c8), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), '0001760d', hex(0x0000005f)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__WRITE(die, chn, 0x0000005f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__READ(die, chn)
    if 0x0000005f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), hex(0x0000005f), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), '00017609', hex(0x000000f9)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__WRITE(die, chn, 0x000000f9)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__READ(die, chn)
    if 0x000000f9 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), hex(0x000000f9), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), '0001760a', hex(0x0000000b)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__WRITE(die, chn, 0x0000000b)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__READ(die, chn)
    if 0x0000000b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), hex(0x0000000b), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), '00017600', hex(0x0000000f)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), '00017601', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL2_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__ADDRESS), '00017812', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__ADDRESS), hex(0x0000ffff), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL3_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__ADDRESS), '00017813', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__ADDRESS), hex(0x0000ffff), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL4_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__ADDRESS), '00017814', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__ADDRESS), hex(0x0000ffff), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL5_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__ADDRESS), '00017815', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__ADDRESS), hex(0x0000ffff), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL6_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__ADDRESS), '00017816', hex(0x0000ff00)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__WRITE(die, chn, 0x0000ff00)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__READ(die, chn)
    if 0x0000ff00 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__ADDRESS), hex(0x0000ff00), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH0', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__ADDRESS), '0002901d', hex(0x00000020)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__WRITE(die, chn, 0x00000020)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__READ(die, chn)
    if 0x00000020 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__ADDRESS), hex(0x00000020), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH1', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__ADDRESS), '0002901e', hex(0x00000001)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH2', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__ADDRESS), '0002901f', hex(0x00008000)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__WRITE(die, chn, 0x00008000)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__READ(die, chn)
    if 0x00008000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__ADDRESS), hex(0x00008000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH3', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__ADDRESS), '00029020', hex(0x00003000)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__WRITE(die, chn, 0x00003000)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__READ(die, chn)
    if 0x00003000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__ADDRESS), hex(0x00003000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__ADDRESS), '00029230', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__ADDRESS), '0002924f', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__ADDRESS), '00029250', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__ADDRESS), '00029251', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__ADDRESS), '00029252', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__ADDRESS), '00029253', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__ADDRESS), hex(0x00000001), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__ADDRESS), '00029236', hex(0x0000003f)))
    reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__WRITE(die, chn, 0x0000003f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__READ(die, chn)
    if 0x0000003f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__ADDRESS), hex(0x0000003f), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__ADDRESS), '00029237', hex(0x00000030)))
    reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__WRITE(die, chn, 0x00000030)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__READ(die, chn)
    if 0x00000030 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__ADDRESS), hex(0x00000030), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3', hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__ADDRESS), '00029238', hex(0x0000000f)))
    reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__ADDRESS), hex(0x0000000f), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__ADDRESS), '00029255', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__ADDRESS), '00029256', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__ADDRESS), hex(0x00000004), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_TDC_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__ADDRESS), '00029242', hex(0x00000007)))
    reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__WRITE(die, chn, 0x00000007)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__READ(die, chn)
    if 0x00000007 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__ADDRESS), hex(0x00000007), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_VCO_CFG6', hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__ADDRESS), '0002922d', hex(0x00000019)))
    reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__WRITE(die, chn, 0x00000019)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__READ(die, chn)
    if 0x00000019 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__ADDRESS), hex(0x00000019), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_VCO_CFG7', hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__ADDRESS), '0002922e', hex(0x00000099)))
    reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__WRITE(die, chn, 0x00000099)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__READ(die, chn)
    if 0x00000099 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__ADDRESS), hex(0x00000099), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), '000291c9', hex(0x000000cf)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__WRITE(die, chn, 0x000000cf)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__READ(die, chn)
    if 0x000000cf != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), hex(0x000000cf), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), '000291ca', hex(0x000000f3)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__WRITE(die, chn, 0x000000f3)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__READ(die, chn)
    if 0x000000f3 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), hex(0x000000f3), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), '000291cb', hex(0x0000003c)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__WRITE(die, chn, 0x0000003c)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__READ(die, chn)
    if 0x0000003c != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), hex(0x0000003c), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_PIOC_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_PIOC_CFG1__ADDRESS), '000291c7', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_PIOC_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_PIOC_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_PIOC_CFG1__ADDRESS), hex(0x00000000), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__ADDRESS), '000291fb', hex(0x000000b0)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__WRITE(die, chn, 0x000000b0)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__READ(die, chn)
    if 0x000000b0 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__ADDRESS), hex(0x000000b0), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__ADDRESS), '00029202', hex(0x00000011)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__ADDRESS), hex(0x00000011), data1))


    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__ADDRESS), '0002912e', hex(0x00000013)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__WRITE(die, chn, 0x00000013)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__READ(die, chn)
    if 0x00000013 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCAL_CODE_INIT_CFG2__ADDRESS), hex(0x00000013), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__ADDRESS), '00029145', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCC_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__ADDRESS), '0002914b', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCF_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__ADDRESS), '00029151', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_FCH_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__ADDRESS), '00029156', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG0__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__ADDRESS), '00029157', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_DIV_INIT_LD_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__ADDRESS), '00029142', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCC_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__ADDRESS), '00029148', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCF_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__ADDRESS), '0002914e', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_FCH_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__ADDRESS), '00029153', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG0__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__ADDRESS), '00029154', hex(0x00000008)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__WRITE(die, chn, 0x00000008)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__READ(die, chn)
    if 0x00000008 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_FCNT_REF_INIT_LD_CFG1__ADDRESS), hex(0x00000008), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_LD_CNT_TOL_CFG', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__ADDRESS), '0002915c', hex(0x00000011)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_CNT_TOL_CFG__ADDRESS), hex(0x00000011), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_LD_NUM_ITER_CFG', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__ADDRESS), '0002915b', hex(0x00000011)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_LD_NUM_ITER_CFG__ADDRESS), hex(0x00000011), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), '00029107', hex(0x0000000f)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), '00029108', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), '0002910c', hex(0x000000c8)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__WRITE(die, chn, 0x000000c8)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__READ(die, chn)
    if 0x000000c8 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), hex(0x000000c8), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), '0002910d', hex(0x0000005f)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__WRITE(die, chn, 0x0000005f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__READ(die, chn)
    if 0x0000005f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), hex(0x0000005f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), '00029109', hex(0x000000f9)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__WRITE(die, chn, 0x000000f9)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__READ(die, chn)
    if 0x000000f9 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), hex(0x000000f9), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), '0002910a', hex(0x0000000b)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__WRITE(die, chn, 0x0000000b)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__READ(die, chn)
    if 0x0000000b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), hex(0x0000000b), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), '00029100', hex(0x0000000f)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), '00029101', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_CLKEN', hex(reg.ODSP_PMR_TX_TXD_CLKEN__ADDRESS), '00029400', hex(0x00002200)))
    reg.ODSP_PMR_TX_TXD_CLKEN__WRITE(die, chn, 0x00002200)
    data1 = reg.ODSP_PMR_TX_TXD_CLKEN__READ(die, chn)
    if 0x00002200 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_CLKEN__ADDRESS), hex(0x00002200), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_CFG', hex(reg.ODSP_PMR_TX_TXD_DSP_CFG__ADDRESS), '0002944d', hex(0x00000001)))
    reg.ODSP_PMR_TX_TXD_DSP_CFG__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_CFG__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_CFG__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_MAP_CFG', hex(reg.ODSP_PMR_TX_TXD_DSP_MAP_CFG__ADDRESS), '0002944e', hex(0x00003120)))
    reg.ODSP_PMR_TX_TXD_DSP_MAP_CFG__WRITE(die, chn, 0x00003120)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_MAP_CFG__READ(die, chn)
    if 0x00003120 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_MAP_CFG__ADDRESS), hex(0x00003120), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_FIFO_CFG0', hex(reg.ODSP_PMR_TX_TXD_FIFO_CFG0__ADDRESS), '00029403', hex(0x00007c11)))
    reg.ODSP_PMR_TX_TXD_FIFO_CFG0__WRITE(die, chn, 0x00007c11)
    data1 = reg.ODSP_PMR_TX_TXD_FIFO_CFG0__READ(die, chn)
    if 0x00007c11 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_FIFO_CFG0__ADDRESS), hex(0x00007c11), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_FIFO_CFG1', hex(reg.ODSP_PMR_TX_TXD_FIFO_CFG1__ADDRESS), '00029404', hex(0x0000f10f)))
    reg.ODSP_PMR_TX_TXD_FIFO_CFG1__WRITE(die, chn, 0x0000f10f)
    data1 = reg.ODSP_PMR_TX_TXD_FIFO_CFG1__READ(die, chn)
    if 0x0000f10f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_FIFO_CFG1__ADDRESS), hex(0x0000f10f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_MISC_CFG', hex(reg.ODSP_PMR_TX_TXD_MISC_CFG__ADDRESS), '00029402', hex(0x0000b401)))
    reg.ODSP_PMR_TX_TXD_MISC_CFG__WRITE(die, chn, 0x0000b401)
    data1 = reg.ODSP_PMR_TX_TXD_MISC_CFG__READ(die, chn)
    if 0x0000b401 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_MISC_CFG__ADDRESS), hex(0x0000b401), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_SQUELCH_EN_CFG', hex(reg.ODSP_PMR_TX_TXD_SQUELCH_EN_CFG__ADDRESS), '0002944b', hex(0x00000000)))
    reg.ODSP_PMR_TX_TXD_SQUELCH_EN_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_TXD_SQUELCH_EN_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_SQUELCH_EN_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_CFG_VERSION', hex(reg.ODSP_PMR_RX_PLL_PLLD_CFG_VERSION__ADDRESS), '0001771d', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_CFG_VERSION__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_CFG_VERSION__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_CFG_VERSION__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8', hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__ADDRESS), '00017702', hex(0x00000011)))
    reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG8__ADDRESS), hex(0x00000011), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG9', hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG9__ADDRESS), '00017703', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG9__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG9__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG9__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG0__ADDRESS), '000176fa', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG0__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG1__ADDRESS), '000176fb', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG1__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG2__ADDRESS), '000176fc', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG2__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG2__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG2__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG3', hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG3__ADDRESS), '000176fd', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG3__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG3__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FBDSM_CFG3__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), '00017600', hex(0x0000000f)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), '00017601', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__ADDRESS), '00017736', hex(0x0000003f)))
    reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__WRITE(die, chn, 0x0000003f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__READ(die, chn)
    if 0x0000003f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG1__ADDRESS), hex(0x0000003f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__ADDRESS), '00017737', hex(0x00000030)))
    reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__WRITE(die, chn, 0x00000030)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__READ(die, chn)
    if 0x00000030 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG2__ADDRESS), hex(0x00000030), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3', hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__ADDRESS), '00017738', hex(0x0000000f)))
    reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PFDCP_CFG3__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), '0001766a', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), '0001766b', hex(0x0000001a)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__WRITE(die, chn, 0x0000001a)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__READ(die, chn)
    if 0x0000001a != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), hex(0x0000001a), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), '0001766a', hex(0x000000f1)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__WRITE(die, chn, 0x000000f1)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__READ(die, chn)
    if 0x000000f1 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), hex(0x000000f1), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), '0001766b', hex(0x0000001b)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__WRITE(die, chn, 0x0000001b)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__READ(die, chn)
    if 0x0000001b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), hex(0x0000001b), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), '000176c9', hex(0x000000cf)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__WRITE(die, chn, 0x000000cf)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__READ(die, chn)
    if 0x000000cf != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), hex(0x000000cf), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), '000176ca', hex(0x000000f3)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__WRITE(die, chn, 0x000000f3)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__READ(die, chn)
    if 0x000000f3 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), hex(0x000000f3), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), '000176cb', hex(0x0000003c)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__WRITE(die, chn, 0x0000003c)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__READ(die, chn)
    if 0x0000003c != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), hex(0x0000003c), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_DLF_LF_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_LF_CFG0__ADDRESS), '000176cc', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLD_DLF_LF_CFG0__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_DLF_LF_CFG0__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_DLF_LF_CFG0__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), '00017609', hex(0x000000f9)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__WRITE(die, chn, 0x000000f9)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__READ(die, chn)
    if 0x000000f9 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), hex(0x000000f9), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), '0001760a', hex(0x0000000b)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__WRITE(die, chn, 0x0000000b)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__READ(die, chn)
    if 0x0000000b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), hex(0x0000000b), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG2__ADDRESS), '0001760b', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG2__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG2__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_START_KI_CFG2__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), '0001760c', hex(0x000000c8)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__WRITE(die, chn, 0x000000c8)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__READ(die, chn)
    if 0x000000c8 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), hex(0x000000c8), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), '0001760d', hex(0x0000005f)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__WRITE(die, chn, 0x0000005f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__READ(die, chn)
    if 0x0000005f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), hex(0x0000005f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__ADDRESS), '0001760e', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), '00017607', hex(0x0000000f)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), '00017608', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_VCO_CFG6', hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__ADDRESS), '0001772d', hex(0x00000019)))
    reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__WRITE(die, chn, 0x00000019)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__READ(die, chn)
    if 0x00000019 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG6__ADDRESS), hex(0x00000019), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_VCO_CFG7', hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__ADDRESS), '0001772e', hex(0x00000099)))
    reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__WRITE(die, chn, 0x00000099)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__READ(die, chn)
    if 0x00000099 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_VCO_CFG7__ADDRESS), hex(0x00000099), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__ADDRESS), '00017730', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_FBDIV_CFG0__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_TDC_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__ADDRESS), '00017742', hex(0x00000007)))
    reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__WRITE(die, chn, 0x00000007)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__READ(die, chn)
    if 0x00000007 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_TDC_CFG1__ADDRESS), hex(0x00000007), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__ADDRESS), '0001774f', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG1__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__ADDRESS), '00017750', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG2__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__ADDRESS), '00017751', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG3__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__ADDRESS), '00017752', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG4__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5', hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__ADDRESS), '00017753', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_LF_P_CFG5__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__ADDRESS), '00017755', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG0__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1', hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__ADDRESS), '00017756', hex(0x00000004)))
    reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLA_PIOC_CFG1__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_RST_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_RST_CFG0__ADDRESS), '00017708', hex(0x00000000)))
    reg.ODSP_PMR_RX_PLL_PLLD_RST_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_RST_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_RST_CFG0__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_INTE', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_INTE__ADDRESS), '000176c3', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_INTE__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_INTE__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_INTE__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_INT', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_INT__ADDRESS), '000176c2', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_INT__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_INT__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_INT__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_PLL_PLLD_FSM_CMD_CFG0', hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_CMD_CFG0__ADDRESS), '00017682', hex(0x00000001)))
    reg.ODSP_PMR_RX_PLL_PLLD_FSM_CMD_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_PLL_PLLD_FSM_CMD_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_PLL_PLLD_FSM_CMD_CFG0__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_CFG_VERSION', hex(reg.ODSP_PMR_TX_PLL_PLLD_CFG_VERSION__ADDRESS), '0002921d', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_CFG_VERSION__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_CFG_VERSION__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_CFG_VERSION__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__ADDRESS), '00029202', hex(0x00000011)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__WRITE(die, chn, 0x00000011)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__READ(die, chn)
    if 0x00000011 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG8__ADDRESS), hex(0x00000011), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG9', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG9__ADDRESS), '00029203', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG9__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG9__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG9__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG0__ADDRESS), '000291fa', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG0__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__ADDRESS), '000291fb', hex(0x000000b0)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__WRITE(die, chn, 0x000000b0)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__READ(die, chn)
    if 0x000000b0 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG1__ADDRESS), hex(0x000000b0), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG2__ADDRESS), '000291fc', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG2__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG2__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG2__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG3', hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG3__ADDRESS), '000291fd', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG3__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG3__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FBDSM_CFG3__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), '00029100', hex(0x0000000f)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), '00029101', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_WAIT_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__ADDRESS), '00029236', hex(0x0000003f)))
    reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__WRITE(die, chn, 0x0000003f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__READ(die, chn)
    if 0x0000003f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG1__ADDRESS), hex(0x0000003f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__ADDRESS), '00029237', hex(0x00000030)))
    reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__WRITE(die, chn, 0x00000030)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__READ(die, chn)
    if 0x00000030 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG2__ADDRESS), hex(0x00000030), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3', hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__ADDRESS), '00029238', hex(0x0000000f)))
    reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PFDCP_CFG3__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), '0002916a', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), '0002916b', hex(0x0000001a)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__WRITE(die, chn, 0x0000001a)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__READ(die, chn)
    if 0x0000001a != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), hex(0x0000001a), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), '0002916a', hex(0x000000f1)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__WRITE(die, chn, 0x000000f1)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__READ(die, chn)
    if 0x000000f1 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG0__ADDRESS), hex(0x000000f1), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), '0002916b', hex(0x0000001b)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__WRITE(die, chn, 0x0000001b)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__READ(die, chn)
    if 0x0000001b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_SKIP_CFG1__ADDRESS), hex(0x0000001b), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), '000291c9', hex(0x000000cf)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__WRITE(die, chn, 0x000000cf)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__READ(die, chn)
    if 0x000000cf != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG1__ADDRESS), hex(0x000000cf), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), '000291ca', hex(0x000000f3)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__WRITE(die, chn, 0x000000f3)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__READ(die, chn)
    if 0x000000f3 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG2__ADDRESS), hex(0x000000f3), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), '000291cb', hex(0x0000003c)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__WRITE(die, chn, 0x0000003c)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__READ(die, chn)
    if 0x0000003c != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_DSMT_CFG3__ADDRESS), hex(0x0000003c), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_DLF_LF_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_LF_CFG0__ADDRESS), '000291cc', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLD_DLF_LF_CFG0__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_DLF_LF_CFG0__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_DLF_LF_CFG0__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), '00029109', hex(0x000000f9)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__WRITE(die, chn, 0x000000f9)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__READ(die, chn)
    if 0x000000f9 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG0__ADDRESS), hex(0x000000f9), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), '0002910a', hex(0x0000000b)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__WRITE(die, chn, 0x0000000b)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__READ(die, chn)
    if 0x0000000b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG1__ADDRESS), hex(0x0000000b), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG2__ADDRESS), '0002910b', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG2__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG2__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_START_KI_CFG2__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), '0002910c', hex(0x000000c8)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__WRITE(die, chn, 0x000000c8)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__READ(die, chn)
    if 0x000000c8 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG0__ADDRESS), hex(0x000000c8), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), '0002910d', hex(0x0000005f)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__WRITE(die, chn, 0x0000005f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__READ(die, chn)
    if 0x0000005f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG1__ADDRESS), hex(0x0000005f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__ADDRESS), '0002910e', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_FINAL_KI_CFG2__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), '00029107', hex(0x0000000f)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG0__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), '00029108', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_TGS_CYCLES_CFG1__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_VCO_CFG6', hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__ADDRESS), '0002922d', hex(0x00000019)))
    reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__WRITE(die, chn, 0x00000019)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__READ(die, chn)
    if 0x00000019 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG6__ADDRESS), hex(0x00000019), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_VCO_CFG7', hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__ADDRESS), '0002922e', hex(0x00000099)))
    reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__WRITE(die, chn, 0x00000099)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__READ(die, chn)
    if 0x00000099 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_VCO_CFG7__ADDRESS), hex(0x00000099), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__ADDRESS), '00029230', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_FBDIV_CFG0__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_TDC_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__ADDRESS), '00029242', hex(0x00000007)))
    reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__WRITE(die, chn, 0x00000007)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__READ(die, chn)
    if 0x00000007 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_TDC_CFG1__ADDRESS), hex(0x00000007), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__ADDRESS), '0002924f', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG1__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__ADDRESS), '00029250', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG2__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__ADDRESS), '00029251', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG3__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__ADDRESS), '00029252', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG4__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5', hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__ADDRESS), '00029253', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_LF_P_CFG5__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__ADDRESS), '00029255', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG0__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1', hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__ADDRESS), '00029256', hex(0x00000004)))
    reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLA_PIOC_CFG1__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_RST_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_RST_CFG0__ADDRESS), '00029208', hex(0x00000000)))
    reg.ODSP_PMR_TX_PLL_PLLD_RST_CFG0__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_RST_CFG0__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_RST_CFG0__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_INTE', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_INTE__ADDRESS), '000291c3', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_INTE__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_INTE__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_INTE__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_INT', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_INT__ADDRESS), '000291c2', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_INT__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_INT__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_INT__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_PLL_PLLD_FSM_CMD_CFG0', hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_CMD_CFG0__ADDRESS), '00029182', hex(0x00000001)))
    reg.ODSP_PMR_TX_PLL_PLLD_FSM_CMD_CFG0__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_PLL_PLLD_FSM_CMD_CFG0__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_PLL_PLLD_FSM_CMD_CFG0__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x00004004)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x00004004)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x00004004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x00004004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x0000c004)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x0000c004)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x0000c004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x0000c004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x00004004)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x00004004)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x00004004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x00004004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x00000004)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_TOP_GEN_CFG', hex(reg.ODSP_PMR_RX_TOP_GEN_CFG__ADDRESS), '00017001', hex(0x00000000)))
    reg.ODSP_PMR_RX_TOP_GEN_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_TOP_GEN_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_TOP_GEN_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG', hex(reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__ADDRESS), '00017265', hex(0x00000027)))
    reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__WRITE(die, chn, 0x00000027)
    data1 = reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__READ(die, chn)
    if 0x00000027 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PAM4_DEMAP_CFG__ADDRESS), hex(0x00000027), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_FFE_TAP_CFG', hex(reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__ADDRESS), '0001720c', hex(0x00001800)))
    reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__WRITE(die, chn, 0x00001800)
    data1 = reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__READ(die, chn)
    if 0x00001800 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__ADDRESS), hex(0x00001800), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG', hex(reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__ADDRESS), '0001720b', hex(0x00000000)))
    reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG', hex(reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__ADDRESS), '0001720f', hex(0x00000040)))
    reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__WRITE(die, chn, 0x00000040)
    data1 = reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__READ(die, chn)
    if 0x00000040 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_FFE_PREC1_0_TAP_INITIAL_CFG__ADDRESS), hex(0x00000040), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_FFE_TAP_CFG', hex(reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__ADDRESS), '0001720c', hex(0x00001800)))
    reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__WRITE(die, chn, 0x00001800)
    data1 = reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__READ(die, chn)
    if 0x00001800 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_FFE_TAP_CFG__ADDRESS), hex(0x00001800), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), '00017267', hex(0x00000000)))
    reg.ODSP_PMR_RX_DSP_STM_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_DSP_STM_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG', hex(reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__ADDRESS), '00017200', hex(0x00000006)))
    reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__WRITE(die, chn, 0x00000006)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__READ(die, chn)
    if 0x00000006 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_CONTROL_CFG__ADDRESS), hex(0x00000006), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG1', hex(reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG1__ADDRESS), '0001726e', hex(0x00001200)))
    reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG1__WRITE(die, chn, 0x00001200)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG1__READ(die, chn)
    if 0x00001200 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG1__ADDRESS), hex(0x00001200), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4', hex(reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__ADDRESS), '00017271', hex(0x00001200)))
    reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__WRITE(die, chn, 0x00001200)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__READ(die, chn)
    if 0x00001200 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__ADDRESS), hex(0x00001200), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), '000172b4', hex(0x00004209)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__WRITE(die, chn, 0x00004209)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__READ(die, chn)
    if 0x00004209 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), hex(0x00004209), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), '000172b5', hex(0x00001804)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__WRITE(die, chn, 0x00001804)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__READ(die, chn)
    if 0x00001804 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), hex(0x00001804), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL6_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__ADDRESS), '00017816', hex(0x0000ff00)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__WRITE(die, chn, 0x0000ff00)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__READ(die, chn)
    if 0x0000ff00 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL6_CFG__ADDRESS), hex(0x0000ff00), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL2_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__ADDRESS), '00017812', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL2_CFG__ADDRESS), hex(0x0000ffff), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL3_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__ADDRESS), '00017813', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL3_CFG__ADDRESS), hex(0x0000ffff), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL4_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__ADDRESS), '00017814', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL4_CFG__ADDRESS), hex(0x0000ffff), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL5_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__ADDRESS), '00017815', hex(0x0000ffff)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL5_CFG__ADDRESS), hex(0x0000ffff), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL1_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__ADDRESS), '00017811', hex(0x00000000)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL1_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__ADDRESS), '00017811', hex(0x00000600)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__WRITE(die, chn, 0x00000600)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__READ(die, chn)
    if 0x00000600 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL1_CFG__ADDRESS), hex(0x00000600), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL0_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__ADDRESS), '00017810', hex(0x00004000)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__WRITE(die, chn, 0x00004000)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__READ(die, chn)
    if 0x00004000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__ADDRESS), hex(0x00004000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL0_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__ADDRESS), '00017810', hex(0x0000c000)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__WRITE(die, chn, 0x0000c000)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__READ(die, chn)
    if 0x0000c000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__ADDRESS), hex(0x0000c000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL0_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__ADDRESS), '00017810', hex(0x00004000)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__WRITE(die, chn, 0x00004000)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__READ(die, chn)
    if 0x00004000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL0_CFG__ADDRESS), hex(0x00004000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_AFE_CTRL4_CFG', hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL4_CFG__ADDRESS), '0001780e', hex(0x00000100)))
    reg.ODSP_PMR_RX_RXA_AFE_CTRL4_CFG__WRITE(die, chn, 0x00000100)
    data1 = reg.ODSP_PMR_RX_RXA_AFE_CTRL4_CFG__READ(die, chn)
    if 0x00000100 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL4_CFG__ADDRESS), hex(0x00000100), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_AFE_CTRL1_CFG', hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__ADDRESS), '00017808', hex(0x00008160)))
    reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__WRITE(die, chn, 0x00008160)
    data1 = reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__READ(die, chn)
    if 0x00008160 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL1_CFG__ADDRESS), hex(0x00008160), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_MISC0', hex(reg.ODSP_PMR_RX_RXA_MISC0__ADDRESS), '00017819', hex(0x00000080)))
    reg.ODSP_PMR_RX_RXA_MISC0__WRITE(die, chn, 0x00000080)
    data1 = reg.ODSP_PMR_RX_RXA_MISC0__READ(die, chn)
    if 0x00000080 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_MISC0__ADDRESS), hex(0x00000080), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_AFE_CTRL2_CFG', hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL2_CFG__ADDRESS), '0001780c', hex(0x00000122)))
    reg.ODSP_PMR_RX_RXA_AFE_CTRL2_CFG__WRITE(die, chn, 0x00000122)
    data1 = reg.ODSP_PMR_RX_RXA_AFE_CTRL2_CFG__READ(die, chn)
    if 0x00000122 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL2_CFG__ADDRESS), hex(0x00000122), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_AFE_CTRL3_CFG', hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL3_CFG__ADDRESS), '0001780d', hex(0x00000118)))
    reg.ODSP_PMR_RX_RXA_AFE_CTRL3_CFG__WRITE(die, chn, 0x00000118)
    data1 = reg.ODSP_PMR_RX_RXA_AFE_CTRL3_CFG__READ(die, chn)
    if 0x00000118 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_AFE_CTRL3_CFG__ADDRESS), hex(0x00000118), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_STM_CFG1', hex(reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__ADDRESS), '00017408', hex(0x00000c00)))
    reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__WRITE(die, chn, 0x00000c00)
    data1 = reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__READ(die, chn)
    if 0x00000c00 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__ADDRESS), hex(0x00000c00), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_STM_CFG1', hex(reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__ADDRESS), '00017408', hex(0x00000c40)))
    reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__WRITE(die, chn, 0x00000c40)
    data1 = reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__READ(die, chn)
    if 0x00000c40 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_STM_CFG1__ADDRESS), hex(0x00000c40), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x0000000c)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x0000000c)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x0000000c != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x0000000c), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_RXA_ADC_CTRL7_CFG', hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), '00017817', hex(0x00000004)))
    reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__WRITE(die, chn, 0x00000004)
    data1 = reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__READ(die, chn)
    if 0x00000004 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_RXA_ADC_CTRL7_CFG__ADDRESS), hex(0x00000004), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), '000172b4', hex(0x00006209)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__WRITE(die, chn, 0x00006209)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__READ(die, chn)
    if 0x00006209 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), hex(0x00006209), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), '000172b4', hex(0x00004209)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__WRITE(die, chn, 0x00004209)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__READ(die, chn)
    if 0x00004209 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), hex(0x00004209), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_TOP_GEN_CFG', hex(reg.ODSP_PMR_RX_TOP_GEN_CFG__ADDRESS), '00017001', hex(0x00000001)))
    reg.ODSP_PMR_RX_TOP_GEN_CFG__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_RX_TOP_GEN_CFG__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_TOP_GEN_CFG__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_CG_CFG', hex(reg.ODSP_PMR_TX_TX_TOP_CG_CFG__ADDRESS), '00029001', hex(0x00000001)))
    reg.ODSP_PMR_TX_TX_TOP_CG_CFG__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_TX_TOP_CG_CFG__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_CG_CFG__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH0', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__ADDRESS), '0002901d', hex(0x00000020)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__WRITE(die, chn, 0x00000020)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__READ(die, chn)
    if 0x00000020 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH0__ADDRESS), hex(0x00000020), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH2', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__ADDRESS), '0002901f', hex(0x00008000)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__WRITE(die, chn, 0x00008000)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__READ(die, chn)
    if 0x00008000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH2__ADDRESS), hex(0x00008000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH3', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__ADDRESS), '00029020', hex(0x00003000)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__WRITE(die, chn, 0x00003000)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__READ(die, chn)
    if 0x00003000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH3__ADDRESS), hex(0x00003000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH1', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__ADDRESS), '0002901e', hex(0x0000000d)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__WRITE(die, chn, 0x0000000d)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__READ(die, chn)
    if 0x0000000d != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__ADDRESS), hex(0x0000000d), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TX_TOP_SCRATCH1', hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__ADDRESS), '0002901e', hex(0x00000001)))
    reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__WRITE(die, chn, 0x00000001)
    data1 = reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__READ(die, chn)
    if 0x00000001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TX_TOP_SCRATCH1__ADDRESS), hex(0x00000001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXA_CK_CTL0_CFG', hex(reg.ODSP_PMR_TX_TXA_CK_CTL0_CFG__ADDRESS), '00029600', hex(0x00000027)))
    reg.ODSP_PMR_TX_TXA_CK_CTL0_CFG__WRITE(die, chn, 0x00000027)
    data1 = reg.ODSP_PMR_TX_TXA_CK_CTL0_CFG__READ(die, chn)
    if 0x00000027 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXA_CK_CTL0_CFG__ADDRESS), hex(0x00000027), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXA_DAC_CTL1_CFG', hex(reg.ODSP_PMR_TX_TXA_DAC_CTL1_CFG__ADDRESS), '00029605', hex(0x00000003)))
    reg.ODSP_PMR_TX_TXA_DAC_CTL1_CFG__WRITE(die, chn, 0x00000003)
    data1 = reg.ODSP_PMR_TX_TXA_DAC_CTL1_CFG__READ(die, chn)
    if 0x00000003 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXA_DAC_CTL1_CFG__ADDRESS), hex(0x00000003), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXA_DAC_CTL0_CFG', hex(reg.ODSP_PMR_TX_TXA_DAC_CTL0_CFG__ADDRESS), '00029604', hex(0x0000000f)))
    reg.ODSP_PMR_TX_TXA_DAC_CTL0_CFG__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_TXA_DAC_CTL0_CFG__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXA_DAC_CTL0_CFG__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXA_DAC_CTL2_CFG', hex(reg.ODSP_PMR_TX_TXA_DAC_CTL2_CFG__ADDRESS), '00029606', hex(0x000000df)))
    reg.ODSP_PMR_TX_TXA_DAC_CTL2_CFG__WRITE(die, chn, 0x000000df)
    data1 = reg.ODSP_PMR_TX_TXA_DAC_CTL2_CFG__READ(die, chn)
    if 0x000000df != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXA_DAC_CTL2_CFG__ADDRESS), hex(0x000000df), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXA_DAC_CTL3_CFG', hex(reg.ODSP_PMR_TX_TXA_DAC_CTL3_CFG__ADDRESS), '00029607', hex(0x0000004d)))
    reg.ODSP_PMR_TX_TXA_DAC_CTL3_CFG__WRITE(die, chn, 0x0000004d)
    data1 = reg.ODSP_PMR_TX_TXA_DAC_CTL3_CFG__READ(die, chn)
    if 0x0000004d != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXA_DAC_CTL3_CFG__ADDRESS), hex(0x0000004d), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXA_DAC_CTL4_CFG', hex(reg.ODSP_PMR_TX_TXA_DAC_CTL4_CFG__ADDRESS), '00029608', hex(0x00000013)))
    reg.ODSP_PMR_TX_TXA_DAC_CTL4_CFG__WRITE(die, chn, 0x00000013)
    data1 = reg.ODSP_PMR_TX_TXA_DAC_CTL4_CFG__READ(die, chn)
    if 0x00000013 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXA_DAC_CTL4_CFG__ADDRESS), hex(0x00000013), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXA_SER_CTL0_CFG', hex(reg.ODSP_PMR_TX_TXA_SER_CTL0_CFG__ADDRESS), '0002960c', hex(0x00000003)))
    reg.ODSP_PMR_TX_TXA_SER_CTL0_CFG__WRITE(die, chn, 0x00000003)
    data1 = reg.ODSP_PMR_TX_TXA_SER_CTL0_CFG__READ(die, chn)
    if 0x00000003 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXA_SER_CTL0_CFG__ADDRESS), hex(0x00000003), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x00000041)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x00000041)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x00000041 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x00000041), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008000)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008000)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x00000041)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x00000041)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x00000041 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x00000041), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008000)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008000)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x0000006b)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x0000006b)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x0000006b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x0000006b), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008001)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008001)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x0000006b)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x0000006b)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x0000006b != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x0000006b), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008001)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008001)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008001 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008001), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x00000015)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x00000015)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x00000015 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x00000015), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008002)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008002)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008002 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008002), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x00000015)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x00000015)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x00000015 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x00000015), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008002)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008002)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008002 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008002), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x0000003f)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x0000003f)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x0000003f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x0000003f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008003)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008003)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008003 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008003), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_WRITE', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), '00029452', hex(0x0000003f)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__WRITE(die, chn, 0x0000003f)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__READ(die, chn)
    if 0x0000003f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_WRITE__ADDRESS), hex(0x0000003f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_DSP_LUT_ACCESS', hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), '00029451', hex(0x00008003)))
    reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__WRITE(die, chn, 0x00008003)
    data1 = reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__READ(die, chn)
    if 0x00008003 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_DSP_LUT_ACCESS__ADDRESS), hex(0x00008003), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_RESET', hex(reg.ODSP_PMR_TX_TXD_RESET__ADDRESS), '00029401', hex(0x000002cd)))
    reg.ODSP_PMR_TX_TXD_RESET__WRITE(die, chn, 0x000002cd)
    data1 = reg.ODSP_PMR_TX_TXD_RESET__READ(die, chn)
    if 0x000002cd != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_RESET__ADDRESS), hex(0x000002cd), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_RESET', hex(reg.ODSP_PMR_TX_TXD_RESET__ADDRESS), '00029401', hex(0x00000000)))
    reg.ODSP_PMR_TX_TXD_RESET__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_TXD_RESET__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_RESET__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_FIFO_CTRL', hex(reg.ODSP_PMR_TX_TXD_FIFO_CTRL__ADDRESS), '00029411', hex(0x0000000f)))
    reg.ODSP_PMR_TX_TXD_FIFO_CTRL__WRITE(die, chn, 0x0000000f)
    data1 = reg.ODSP_PMR_TX_TXD_FIFO_CTRL__READ(die, chn)
    if 0x0000000f != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_FIFO_CTRL__ADDRESS), hex(0x0000000f), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_FIFO_CTRL', hex(reg.ODSP_PMR_TX_TXD_FIFO_CTRL__ADDRESS), '00029411', hex(0x00000000)))
    reg.ODSP_PMR_TX_TXD_FIFO_CTRL__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_TX_TXD_FIFO_CTRL__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_FIFO_CTRL__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_FIFO_INT', hex(reg.ODSP_PMR_TX_TXD_FIFO_INT__ADDRESS), '0002946a', hex(0x0000ffff)))
    reg.ODSP_PMR_TX_TXD_FIFO_INT__WRITE(die, chn, 0x0000ffff)
    data1 = reg.ODSP_PMR_TX_TXD_FIFO_INT__READ(die, chn)
    if 0x0000ffff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_FIFO_INT__ADDRESS), hex(0x0000ffff), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), '000172b5', hex(0x00007804)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__WRITE(die, chn, 0x00007804)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__READ(die, chn)
    if 0x00007804 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), hex(0x00007804), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), '000172b4', hex(0x00005bb9)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__WRITE(die, chn, 0x00005bb9)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__READ(die, chn)
    if 0x00005bb9 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), hex(0x00005bb9), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_LOW_SPEED_TED_CFG', hex(reg.ODSP_PMR_RX_DSP_LOW_SPEED_TED_CFG__ADDRESS), '00017332', hex(0x00000000)))
    reg.ODSP_PMR_RX_DSP_LOW_SPEED_TED_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_DSP_LOW_SPEED_TED_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_LOW_SPEED_TED_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), '000172b4', hex(0x00005bbb)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__WRITE(die, chn, 0x00005bbb)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__READ(die, chn)
    if 0x00005bbb != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG1__ADDRESS), hex(0x00005bbb), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), '000172b5', hex(0x00007f87)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__WRITE(die, chn, 0x00007f87)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__READ(die, chn)
    if 0x00007f87 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), hex(0x00007f87), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), '00017267', hex(0x00000000)))
    reg.ODSP_PMR_RX_DSP_STM_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_DSP_STM_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_PGA_CFG2', hex(reg.ODSP_PMR_RX_DSP_STM_PGA_CFG2__ADDRESS), '0001726a', hex(0x00000078)))
    reg.ODSP_PMR_RX_DSP_STM_PGA_CFG2__WRITE(die, chn, 0x00000078)
    data1 = reg.ODSP_PMR_RX_DSP_STM_PGA_CFG2__READ(die, chn)
    if 0x00000078 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_PGA_CFG2__ADDRESS), hex(0x00000078), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG2', hex(reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG2__ADDRESS), '00017241', hex(0x00007d02)))
    reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG2__WRITE(die, chn, 0x00007d02)
    data1 = reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG2__READ(die, chn)
    if 0x00007d02 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG2__ADDRESS), hex(0x00007d02), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG1', hex(reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG1__ADDRESS), '00017240', hex(0x00000020)))
    reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG1__WRITE(die, chn, 0x00000020)
    data1 = reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG1__READ(die, chn)
    if 0x00000020 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PGA_THRESHOLD_CFG1__ADDRESS), hex(0x00000020), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_PGA_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_PGA_CFG__ADDRESS), '00017269', hex(0x00000414)))
    reg.ODSP_PMR_RX_DSP_STM_PGA_CFG__WRITE(die, chn, 0x00000414)
    data1 = reg.ODSP_PMR_RX_DSP_STM_PGA_CFG__READ(die, chn)
    if 0x00000414 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_PGA_CFG__ADDRESS), hex(0x00000414), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PGA_CODE_CFG', hex(reg.ODSP_PMR_RX_DSP_PGA_CODE_CFG__ADDRESS), '0001723f', hex(0x000003fd)))
    reg.ODSP_PMR_RX_DSP_PGA_CODE_CFG__WRITE(die, chn, 0x000003fd)
    data1 = reg.ODSP_PMR_RX_DSP_PGA_CODE_CFG__READ(die, chn)
    if 0x000003fd != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PGA_CODE_CFG__ADDRESS), hex(0x000003fd), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_MISC_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__ADDRESS), '00017266', hex(0x000000c0)))
    reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__WRITE(die, chn, 0x000000c0)
    data1 = reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__READ(die, chn)
    if 0x000000c0 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__ADDRESS), hex(0x000000c0), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), '00017267', hex(0x00000000)))
    reg.ODSP_PMR_RX_DSP_STM_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_DSP_STM_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DSP_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_DSP_CFG__ADDRESS), '00017402', hex(0x0000f900)))
    reg.ODSP_PMR_RX_DSP_STM_DSP_CFG__WRITE(die, chn, 0x0000f900)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DSP_CFG__READ(die, chn)
    if 0x0000f900 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DSP_CFG__ADDRESS), hex(0x0000f900), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_DTL_CFG', hex(reg.ODSP_PMR_RX_DSP_DTL_CFG__ADDRESS), '00017223', hex(0x00000058)))
    reg.ODSP_PMR_RX_DSP_DTL_CFG__WRITE(die, chn, 0x00000058)
    data1 = reg.ODSP_PMR_RX_DSP_DTL_CFG__READ(die, chn)
    if 0x00000058 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_DTL_CFG__ADDRESS), hex(0x00000058), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DTL_THETA_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_DTL_THETA_CFG__ADDRESS), '00017404', hex(0x00000000)))
    reg.ODSP_PMR_RX_DSP_STM_DTL_THETA_CFG__WRITE(die, chn, 0x00000000)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DTL_THETA_CFG__READ(die, chn)
    if 0x00000000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DTL_THETA_CFG__ADDRESS), hex(0x00000000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_DTL_KP_CFG', hex(reg.ODSP_PMR_RX_DSP_DTL_KP_CFG__ADDRESS), '00017224', hex(0x00000056)))
    reg.ODSP_PMR_RX_DSP_DTL_KP_CFG__WRITE(die, chn, 0x00000056)
    data1 = reg.ODSP_PMR_RX_DSP_DTL_KP_CFG__READ(die, chn)
    if 0x00000056 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_DTL_KP_CFG__ADDRESS), hex(0x00000056), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_DTL_KF_CFG', hex(reg.ODSP_PMR_RX_DSP_DTL_KF_CFG__ADDRESS), '00017225', hex(0x00000108)))
    reg.ODSP_PMR_RX_DSP_DTL_KF_CFG__WRITE(die, chn, 0x00000108)
    data1 = reg.ODSP_PMR_RX_DSP_DTL_KF_CFG__READ(die, chn)
    if 0x00000108 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_DTL_KF_CFG__ADDRESS), hex(0x00000108), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DTS_DTL_KP_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KP_CFG__ADDRESS), '00017276', hex(0x00005656)))
    reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KP_CFG__WRITE(die, chn, 0x00005656)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KP_CFG__READ(die, chn)
    if 0x00005656 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KP_CFG__ADDRESS), hex(0x00005656), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG1', hex(reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG1__ADDRESS), '00017277', hex(0x00000108)))
    reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG1__WRITE(die, chn, 0x00000108)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG1__READ(die, chn)
    if 0x00000108 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG1__ADDRESS), hex(0x00000108), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG2', hex(reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG2__ADDRESS), '00017278', hex(0x00000108)))
    reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG2__WRITE(die, chn, 0x00000108)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG2__READ(die, chn)
    if 0x00000108 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DTS_DTL_KF_CFG2__ADDRESS), hex(0x00000108), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG', hex(reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__ADDRESS), '0001720b', hex(0x00000664)))
    reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__WRITE(die, chn, 0x00000664)
    data1 = reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__READ(die, chn)
    if 0x00000664 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_FFE_GAINDC_MU_CFG__ADDRESS), hex(0x00000664), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4', hex(reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__ADDRESS), '00017271', hex(0x00001202)))
    reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__WRITE(die, chn, 0x00001202)
    data1 = reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__READ(die, chn)
    if 0x00001202 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_DTS_TIMER_CFG4__ADDRESS), hex(0x00001202), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_SIGNAL_DETECT_THRESHOLD_CFG', hex(reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_THRESHOLD_CFG__ADDRESS), '0001723d', hex(0x0000201e)))
    reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_THRESHOLD_CFG__WRITE(die, chn, 0x0000201e)
    data1 = reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_THRESHOLD_CFG__READ(die, chn)
    if 0x0000201e != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_THRESHOLD_CFG__ADDRESS), hex(0x0000201e), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG', hex(reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__ADDRESS), '0001723a', hex(0x00000003)))
    reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__WRITE(die, chn, 0x00000003)
    data1 = reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__READ(die, chn)
    if 0x00000003 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_SIGNAL_DETECT_CFG__ADDRESS), hex(0x00000003), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_PGA_GAIN_INITIAL_CODE_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_PGA_GAIN_INITIAL_CODE_CFG__ADDRESS), '0001726d', hex(0x000001ff)))
    reg.ODSP_PMR_RX_DSP_STM_PGA_GAIN_INITIAL_CODE_CFG__WRITE(die, chn, 0x000001ff)
    data1 = reg.ODSP_PMR_RX_DSP_STM_PGA_GAIN_INITIAL_CODE_CFG__READ(die, chn)
    if 0x000001ff != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_PGA_GAIN_INITIAL_CODE_CFG__ADDRESS), hex(0x000001ff), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), '00017267', hex(0x00000002)))
    reg.ODSP_PMR_RX_DSP_STM_CFG__WRITE(die, chn, 0x00000002)
    data1 = reg.ODSP_PMR_RX_DSP_STM_CFG__READ(die, chn)
    if 0x00000002 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_CFG__ADDRESS), hex(0x00000002), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG', hex(reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__ADDRESS), '00017202', hex(0x00000007)))
    reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__WRITE(die, chn, 0x00000007)
    data1 = reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__READ(die, chn)
    if 0x00000007 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__ADDRESS), hex(0x00000007), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_STM_MISC_CFG', hex(reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__ADDRESS), '00017266', hex(0x000000c1)))
    reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__WRITE(die, chn, 0x000000c1)
    data1 = reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__READ(die, chn)
    if 0x000000c1 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_STM_MISC_CFG__ADDRESS), hex(0x000000c1), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_GEN_CFG', hex(reg.ODSP_PMR_TX_TXD_GEN_CFG__ADDRESS), '0002941c', hex(0x0000c000)))
    reg.ODSP_PMR_TX_TXD_GEN_CFG__WRITE(die, chn, 0x0000c000)
    data1 = reg.ODSP_PMR_TX_TXD_GEN_CFG__READ(die, chn)
    if 0x0000c000 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_GEN_CFG__ADDRESS), hex(0x0000c000), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_TX_TXD_CLKEN', hex(reg.ODSP_PMR_TX_TXD_CLKEN__ADDRESS), '00029400', hex(0x00002220)))
    reg.ODSP_PMR_TX_TXD_CLKEN__WRITE(die, chn, 0x00002220)
    data1 = reg.ODSP_PMR_TX_TXD_CLKEN__READ(die, chn)
    if 0x00002220 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_TX_TXD_CLKEN__ADDRESS), hex(0x00002220), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG', hex(reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__ADDRESS), '00017202', hex(0x00000017)))
    reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__WRITE(die, chn, 0x00000017)
    data1 = reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__READ(die, chn)
    if 0x00000017 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_DSP_MODE_CONTROL_CFG__ADDRESS), hex(0x00000017), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2', hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), '000172b5', hex(0x00007f87)))
    reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__WRITE(die, chn, 0x00007f87)
    data1 = reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__READ(die, chn)
    if 0x00007f87 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_CLOCK_GATING_CFG2__ADDRESS), hex(0x00007f87), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PRBS_CFG1', hex(reg.ODSP_PMR_RX_DSP_PRBS_CFG1__ADDRESS), '000172a5', hex(0x00000410)))
    reg.ODSP_PMR_RX_DSP_PRBS_CFG1__WRITE(die, chn, 0x00000410)
    data1 = reg.ODSP_PMR_RX_DSP_PRBS_CFG1__READ(die, chn)
    if 0x00000410 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PRBS_CFG1__ADDRESS), hex(0x00000410), data1))

    print('   Writing with MDIO(I2C) address: %s; addr %s(0x%s), data %s' % ('ODSP_PMR_RX_DSP_PRBS_CFG2', hex(reg.ODSP_PMR_RX_DSP_PRBS_CFG2__ADDRESS), '000172a6', hex(0x00000188)))
    reg.ODSP_PMR_RX_DSP_PRBS_CFG2__WRITE(die, chn, 0x00000188)
    data1 = reg.ODSP_PMR_RX_DSP_PRBS_CFG2__READ(die, chn)
    if 0x00000188 != data1:
        print('address 0x%s, written value %s, but read value 0x%x' % (hex(reg.ODSP_PMR_RX_DSP_PRBS_CFG2__ADDRESS), hex(0x00000188), data1))

#Per-lane configuration
print("************************************LANE0************************************")
one_lane_pmr_setup(die=0, chn=0)

# Read AFE Registers
print("AFE PDB Status = 0x%04x on Die %d Lane %d" % (reg.ODSP_PMR_RX_DSP_LANE_SEQUENCER_STATUS__AFE_PDB__READ(die, lane), die, lane))
```
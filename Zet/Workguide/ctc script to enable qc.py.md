```python
"""
@brief
Example API script to configure the Capella ASIC in PRBS mode.

"""
from cpl_api import *
# from ctc_api import *
import ctc_registers as creg

import sys
import time

class channel_t(object):
    """\
    This is a helper structure used to manage a list of channels
    across mutiple IP blocks.
    """
    def __init__(self, die, channel, ch_id):
        # The die associated with the Capella IP channel
        self.die     = die
        # The Capella IP channel
        self.channel = channel
        # The channel ID (may not match the channel)
        self.ch_id   = ch_id

def setup_rx_rules(rules, defaults):
    """\
    This is a helper method used to populate the RX rules structure

    @param rules  [I/O] - The rules structure to populate.
    @param defaults [I] - The RX defaults to copy into the rules.
    """

    rules.enable                = True
    rules.baud_rate             = defaults["baud_rate"]
    rules.dsp_mode              = defaults["dsp_mode"]
    rules.signalling            = defaults["signalling"]
    rules.gray_mapping          = defaults["gray_mapping"]
    rules.ieee_demap            = defaults["ieee_demap"]
    rules.dfe_precoder_en       = defaults["dfe_precoder_en"]
    rules.ctle_manual_control   = defaults["ctle_manual_control"]
    rules.ctle                  = defaults["ctle"]
    rules.ctle2                 = defaults["ctle2"]
    rules.invert_chan           = defaults["invert_chan"]
    rules.afe_trim              = defaults["afe_trim"]
    rules.vga_tracking          = defaults["vga_tracking"]
    rules.rc_dual_bank_en       = defaults["rc_dual_bank_en"]
    rules.mlsd_en               = defaults["mlsd_en"]
    rules.pga_att_en            = defaults["pga_att_en"]

def setup_tx_rules(rules, defaults):
    """\
    This is a helper method used to populate the TX rules structure

    @param rules  [I/O] - The rules structure to populate.
    @param defaults [I] - The RX defaults to copy into the rules.
    """
    rules.enable        = True
    rules.baud_rate     = defaults["baud_rate"]
    rules.signalling    = defaults["signalling"]
    rules.gray_mapping  = defaults["gray_mapping"]
    rules.ieee_demap    = defaults["ieee_demap"]
    rules.precoder_en   = defaults["precoder_en"]
    rules.invert_chan   = defaults["invert_chan"]
    rules.lut_mode      = defaults["lut_mode"]
    rules.src           = defaults["src"]
       
    rules.fir_tap       = defaults["fir_tap"]

def wait_for_links_ready(channels, num_channels):
    """\
    This is a helper method used to wait for all RX/TX to lock

    @param channels     [I] - The list of channels to check for RX/TX lock.
    @param num_channels [I] - The number of channels in the list.

    @return INPHI_OK on success, INPHI_ERROR on failure/timeout.
    """

    status = INPHI_OK

    guard = 4000
    channels_ready = 0

    while(channels_ready < num_channels and guard > 0):
        channel = channels[channels_ready].channel
        die     = channels[channels_ready].die

        is_rx_ready = cpl_is_link_ready(die, channel, CPL_INTF_DIR_RX)
        is_tx_ready = cpl_is_link_ready(die, channel, CPL_INTF_DIR_TX)

        if(is_rx_ready and is_tx_ready):
            channels_ready += 1
        else:
            time.sleep(1.0 / 1000)

        guard -= 1

    if(guard <= 0):
        print("Timed out waiting for RX/TX ready\n")
        status |= INPHI_ERROR

    return status

def setup_analog_refclk(channels, num_channels):
    """\
    This method is used to power up the analog reference clock in it's
    default configuration.

    @param channels     [I] - The channel mapping structure containing the
                              list of channels to power up.
    @param num_channels [I] - The number of channels in the list.
    """

    # Setup the clock buffers - this should be done before powering
    # up the LDOs to ensure that buffers aren't overdriven. These are
    # the defaults for CTC but may be different on the target platform.

    current_device = "CapellaB"
    clkbuf = [0] * 4
    if(current_device in ["CapellaB"]):   # CapellaB
        clkbuf[0] = {"vdir": [0,0], "hdir": 0, "vdrv": [7,4], "hdrv": 7}
        clkbuf[1] = {"vdir": [0,0], "hdir": 0, "vdrv": [7,4], "hdrv": 7}
        clkbuf[2] = {"vdir": [1,0], "hdir": 0, "vdrv": [4,4], "hdrv": 7}
        clkbuf[3] = {"vdir": [0,0], "hdir": 0, "vdrv": [7,4], "hdrv": 7}
    else:
        clkbuf[0] = {"vdir": [0,0], "hdir": 0, "vdrv": [5,5], "hdrv": 0}
        clkbuf[1] = {"vdir": [0,0], "hdir": 0, "vdrv": [5,5], "hdrv": 0}
        clkbuf[2] = {"vdir": [1,0], "hdir": 0, "vdrv": [5,5], "hdrv": 0}
        clkbuf[3] = {"vdir": [0,0], "hdir": 0, "vdrv": [5,5], "hdrv": 0}

    for i in range(num_channels):
        if channels[i].channel == 0:
            index = channels[i].die & 0x3

            # Make sure the TX is out of reset to ensure the analog reference clock
            # gets propagated.
            creg.CPL_MMD30_RESET_CFG__TX_SR__RMW(channels[i].die, 0)

            data = creg.CPL_TX_TXA_MRESERVED_CFG__V_DIR__SET(0,      clkbuf[index]["vdir"][0])
            data = creg.CPL_TX_TXA_MRESERVED_CFG__V_DRIVE__SET(data, clkbuf[index]["vdrv"][0])
            data = creg.CPL_TX_TXA_MRESERVED_CFG__H_DIR__SET(data,   clkbuf[index]["hdir"])
            data = creg.CPL_TX_TXA_MRESERVED_CFG__H_DRIVE__SET(data, clkbuf[index]["hdrv"])

            creg.CPL_TX_TXA_MRESERVED_CFG__WRITE(channels[i].die, 0, data)

            data = creg.CPL_TX_TXA_MRESERVED_CFG__V_DIR__SET(0,      clkbuf[index]["vdir"][1])
            data = creg.CPL_TX_TXA_MRESERVED_CFG__V_DRIVE__SET(data, clkbuf[index]["vdrv"][1])
            data = creg.CPL_TX_TXA_MRESERVED_CFG__H_DIR__SET(data,   clkbuf[index]["hdir"])

            if(current_device not in ["CapellaB"]):   # CapellaB
                data = creg.CPL_TX_TXA_MRESERVED_CFG__H_DRIVE__SET(data, clkbuf[index]["hdrv"])

            creg.CPL_TX_TXA_MRESERVED_CFG__WRITE(channels[i].die, 1, data)

def setup_supplies(channels, num_channels):
    """\
    This method demonstrates an example of powering up the Capella IPs
    and putting the supplies in regulated mode.

    @param channels     [I] - The list of channels to check for RX/TX lock.
    @param num_channels [I] - The number of channels in the list.

    @return INPHI_OK on success, INPHI_ERROR on failure.
    """

    status = INPHI_OK

    pwrup_rules = cpl_pwrup_rules_t()
    status |= cpl_pwrup_rules_set_default(pwrup_rules)

    pwrup_rules.eru_die = channels[0].die

    tmp_cpl_dies = [ 0 ] * 32
    index = 0
    for i in range(num_channels):
        if 0 == channels[i].channel:
            tmp_cpl_dies[index] = channels[i].die
            index += 1

    pwrup_rules.cpl_dies         = tmp_cpl_dies
    pwrup_rules.num_cpl_in_chain = index
    pwrup_rules.mode             = CPL_PWRUP_BYPASS_TXRX

    status |= cpl_pwrup_start(pwrup_rules)

    return status

def example_prbs(die,
                 channels,
                 pwrup_regulators,
                 reset_ctc,
                 propagate_refclk,
                 flag_download_firmware,
                 firmware_filename,
                 flag_wait_for_link_ready,
                 flag_generate_prbs,
                 flag_check_prbs
                 ):
    """
    Example API script to configure the Capella ASIC in PRBS mode.

    @return INPHI_OK on success, INPHI_ERROR on failure.
    """
    status = INPHI_OK

    num_channels = len(channels)

    if reset_ctc:
        # Bring the Capella instances out of reset
        creg.CTC_MMD30_RESET_CFG__WRITE(die, 0x0)

        for i in range(4):
            creg.CPL_MMD30_RESET_CFG__WRITE(die + i, 0xffff)
            creg.CPL_MMD30_RESET_CFG__WRITE(die + i, 0x0)

        # Runstall the Core MCU
        creg.CTC_MCU_GEN_CFG__RUNSTALL__RMW(die, 1)

    # Propogate the Analog Reference Clock
    if propagate_refclk:
        setup_analog_refclk(channels, num_channels)

    # Power up the chip
    if pwrup_regulators:
        status |= setup_supplies(channels, num_channels)

    # On CTC need to power up the LDOs that supply the MCU memories
    creg.CTC_MMD30_CAPELLA_MISC_CFG_0__WRITE(die, 0x40)
    creg.CTC_MMD30_CAPELLA_MISC_CFG_1__WRITE(die, 0x40)
    creg.CTC_MMD30_CAPELLA_MISC_CFG_2__WRITE(die, 0x40)
    creg.CTC_MMD30_CAPELLA_MISC_CFG_3__WRITE(die, 0x40)

    if INPHI_OK != status:
        sys.stdout.write("Failed powering up the device\n")
        return status

    # Direct downloading the firmware to the ASIC
    if flag_download_firmware:

        for i in range(num_channels):
            if 0 == channels[i].channel:

                if firmware_filename != "":
                    print("Downloading firmware located at %s\n" % firmware_filename)
                    status |= cpl_mcu_download_firmware_from_file(channels[i].die, firmware_filename, True)
                else:
                    inline_ver = cpl_mcu_get_inline_firmware_version()
                    print("Downloading inline_firmware_version = %d\n" % inline_ver)

                    status |= cpl_mcu_download_firmware(channels[i].die, True)

                if status != INPHI_OK:
                    print("Failed downloading the firmware on die %x\n" % channels[i].die)
                    return status

    # Setup the default rules for the desired application

    baud_rate = CPL_BAUD_RATE_53p125G
    signalling = CPL_SIGNAL_MODE_PAM
    ieee_demap = True

    gray_mapping = (signalling == CPL_SIGNAL_MODE_PAM)

    rx_defaults = {
                  
                  0:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  1:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  3:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  4:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  6:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  7:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  9:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  10:
                      {
                      "dsp_mode"            : CPL_DSP_MODE_SLC1,
                      "signalling"          : signalling,
                      "gray_mapping"        : gray_mapping,
                      "ieee_demap"          : ieee_demap,
                      "dfe_precoder_en"     : False,
                      "ctle_manual_control" : False,
                      "ctle"                : 2,
                      "ctle2"               : 0,
                      "invert_chan"         : False,
                      "afe_trim"            : CPL_AFE_TRIM_AUTO,
                      "vga_tracking"        : True,
                      "baud_rate"           : baud_rate,
                      "rc_dual_bank_en"     : False,
                      "mlsd_en"             : False,
                      "pga_att_en"          : False
                      },
                  
                  }

    tx_defaults = {
                  
                  0:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  1:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  3:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  4:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  6:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  7:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  9:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  10:
                      {
                      "signalling"   : signalling,
                      "gray_mapping" : gray_mapping,
                      "ieee_demap"   : ieee_demap,
                      "precoder_en"  : False,
                      "invert_chan"  : False,
                      "lut_mode"     : CPL_TX_LUT_3TAP,
                      "fir_tap"      : [-50,600,0,0,0,0,0],
                      "src"          : CPL_TX_SRC_PAT_GEN_SERIAL,
                      "baud_rate"    : baud_rate,
                      },
                  
                  }

    # Reset the chip to put it in a known state
    for i in range(num_channels):
        if 0 == channels[i].channel:
            status |= cpl_init(channels[i].die)

    prbs_gen_intf = CPL_INTF_SERIAL_TX
    if flag_generate_prbs:
        # Setup the PRBS generator
        for i in range(num_channels):
            # Setup the PRBS pattern
            gen_rules = cpl_prbs_gen_rules_t()
            cpl_prbs_gen_rules_set_default(gen_rules)

            gen_rules.prbs_mode        = CPL_PRBS_MODE_COMBINED
            gen_rules.prbs_pattern     = CPL_PAT_PRBS31
            gen_rules.prbs_pattern_lsb = CPL_PAT_PRBS31

            # Configure the PRBS generator
            status |= cpl_prbs_gen_config(channels[i].die, channels[i].channel, prbs_gen_intf, gen_rules)

    chk_status = []
    prbs_chk_intf = CPL_INTF_SERIAL_RX
    if flag_check_prbs:
        # Enable the PRBS checker
        for i in range(num_channels):
            # Setup the checker
            chk_rules = cpl_prbs_chk_rules_t()
            cpl_prbs_chk_rules_set_default(chk_rules)

            chk_rules.prbs_mode        = CPL_PRBS_MODE_MSB_LSB
            chk_rules.prbs_pattern     = CPL_PAT_PRBS31
            chk_rules.prbs_pattern_lsb = CPL_PAT_PRBS31

            status |= cpl_prbs_chk_config(channels[i].die, channels[i].channel, prbs_chk_intf, chk_rules)

            # Clear the initial counters
            serial_chk_status = cpl_prbs_chk_status_t()
            chk_status.append(serial_chk_status)
            status |= cpl_prbs_chk_status(channels[i].die, channels[i].channel, prbs_chk_intf, chk_status[i])

    # Configure the RX channels
    for i in range(num_channels):
        rx_rules = cpl_rx_rules_t()
        cpl_rx_rules_set_default(rx_rules)
        setup_rx_rules(rx_rules, rx_defaults[channels[i].ch_id])

        rx_rules.rx_qc.dis = False
        #rx_rules.rx_qc.hist_dis = False   
        rx_rules.rx_qc.data_mode_hist_dis = False            
        rx_rules.rx_qc.data_mode_dis = False  
        rx_rules.rx_qc.mse_min_threshold = 254
        rx_rules.rx_qc.data_mode_mse_min_threshold = 254

        rx_rules.scdr.enable = False            
        rx_rules.scdr.beta_adapt_enable = True
        rx_rules.scdr.coef_sel = 0
        rx_rules.scdr.mul_sel = 3

        cpl_init_rx(channels[i].die, channels[i].channel, rx_rules)

    # Configure the TX channels
    for i in range(num_channels):
        tx_rules = cpl_tx_rules_t()
        cpl_tx_rules_set_default(tx_rules)
        setup_tx_rules(tx_rules, tx_defaults[channels[i].ch_id])
        cpl_init_tx(channels[i].die, channels[i].channel, tx_rules)

    if flag_wait_for_link_ready:
        # Wait for all RX/TX to lock
        status |= wait_for_links_ready(channels, num_channels)
        if status != INPHI_OK:
            print("Timed out waiting for receive link to be ready\n")
            return status

    if flag_check_prbs:
        # Accumulate Traffic
        time.sleep(2.0)

        # Query the Status
        for i in range(num_channels):
            status |= cpl_prbs_chk_status(channels[i].die, channels[i].channel, prbs_chk_intf, chk_status[i])
            status |= cpl_prbs_chk_status_print(channels[i].die, channels[i].channel, prbs_chk_intf, chk_status[i])

    if INPHI_OK != status:
        print("Warning: failed initializing die %x\n" % die)

    return status

if __name__ == "__main__":

    status = INPHI_OK
    verbose = 1

    # The ASIC to initialize. In this we're not using
    # multiple ASICs within the same GUI so it can be set to 0.
    die = __regdb__.get_current_die()

    channels = [                    (die, 0, 0),        (die, 1, 1),        (die+1, 0, 3),        (die+1, 1, 4),        (die+2, 0, 6),        (die+2, 1, 7),        (die+3, 0, 9),        (die+3, 1, 10)    ]                       

    channels_tmp = [ None ] * len(channels)
    for i in range(len(channels_tmp)):
        channels_tmp[i] = channel_t(channels[i][0], channels[i][1], channels[i][2])
    channels = channels_tmp

    num_channels = len(channels)

    pwrup_regulators            = True
    reset_ctc                   = False
    propagate_refclk            = True
    flag_download_firmware      = False
    firmware_filename           = "C:/usr/inphi_explorer/capella/inphi_exp_capella_internal_release_5_1_2960/support/drivers/capella/ucode/b/cplb_release_direct_download_0_11_0_1503.txt"

    flag_wait_for_link_ready    = False
    flag_generate_prbs          = True
    flag_check_prbs             = True

    status |= example_prbs(die,
                           channels,
                           pwrup_regulators,
                           reset_ctc,
                           propagate_refclk,
                           flag_download_firmware,
                           firmware_filename,
                           flag_wait_for_link_ready,
                           flag_generate_prbs,
                           flag_check_prbs
                           )

    if status != INPHI_OK:
        sys.stdout.write("Example failed")
        sys.exit(-1)

```
```python
# Import register and API
from lynx_400.python import hsc_api as api

# Get number of die on this device over API
dev = api.hsc_dev_t()
api.hsc_dev(dev, 0)
num_dies = api.hsc_dev_num_dies(dev)

chip_conf = { 'bundle': [ { 'bundle_id': 0,
                'config_channel': {'default': True},
                'host_baud_rate': api.HSC_BAUD_RATE_26p5625G,
                'host_channel': [0, 1, 2, 3],
                'host_signalling': api.HSC_SIGNAL_MODE_PAM,
                'id': 0,
                'ieee_demap': False,
                'line_attenuation_loss': 0,
                'line_baud_rate': api.HSC_BAUD_RATE_26p5625G,
                'line_channel': [0, 1, 2, 3],
                'line_signalling': api.HSC_SIGNAL_MODE_PAM,
                'mode': api.HSC_OPER_MODE_DUPLEX_RETIMER,
                'show_config': False,
                'show_link_status': False,
                'wait_link_ready': False}],
  'debug': { 'api_debug_en': False,
             'reg_debug_en': False,
             'reset_before_apply': True,
             'soft_reset_en': False},
  'default': { 'host_rx': { 'afe_trim': api.HSC_AFE_TRIM_AUTO,
                            'auto_ctle': True,
                            'bundle_id': 0,
                            'ctle': [0, 0],
                            'dfe_precoder_en': False,
                            'dsp_mode': api.HSC_DSP_MODE_SLC1,
                            'gray_map': True,
                            'id': 0,
                            'invert': False,
                            'mlsd_en': False,
                            'scdr_en': False,
                            'vga_tracking_en': False},
               'host_tx': { 'bundle_id': 0,
                            'dfe_precoder_en': False,
                            'gray_map': True,
                            'id': 0,
                            'inner_eye1': 1000,
                            'inner_eye2': 2000,
                            'invert': False,
                            'lut_mode': api.HSC_TX_LUT_3TAP,
                            'swing': api.HSC_TX_SWING_100p,
                            'taps': [-50, 650, 0, 0, 0, 0, 0]},
               'line_rx': { 'afe_trim': api.HSC_AFE_TRIM_AUTO,
                            'auto_ctle': True,
                            'bundle_id': 0,
                            'ctle': [0, 0],
                            'dfe_precoder_en': False,
                            'dsp_mode': api.HSC_DSP_MODE_SLC1,
                            'gray_map': True,
                            'id': 0,
                            'invert': False,
                            'mlsd_en': False,
                            'scdr_en': False,
                            'vga_tracking_en': False},
               'line_tx': { 'bundle_id': 0,
                            'dfe_precoder_en': False,
                            'gray_map': True,
                            'id': 0,
                            'inner_eye1': 1000,
                            'inner_eye2': 2000,
                            'invert': False,
                            'lut_mode': api.HSC_TX_LUT_3TAP,
                            'swing': api.HSC_TX_SWING_100p,
                            'taps': [-50, 650, 0, 0, 0, 0, 0]}},
  'firmware': { 'download_firmware': False,
                'firmware_path': 'path_to_firmware',
                'is_dnld_from_file': False},
  'i2c_enable': False}



def helper_tx_rules_set(rules, db):
    api.hsc_tx_rules_fir_taps_set(rules, db['lut_mode'], db['taps'])
    api.hsc_tx_rules_polarity_set(rules, db['invert'])
    api.hsc_tx_rules_gray_mapping_enable(rules, db['gray_map'])
    api.hsc_tx_rules_dfe_precoder_enable(rules, db['dfe_precoder_en'])
    api.hsc_tx_rules_eye_set(rules, api.HSC_EYE_LEVEL_LOWER, db['inner_eye1'])
    api.hsc_tx_rules_eye_set(rules, api.HSC_EYE_LEVEL_UPPER, db['inner_eye2'])
    api.hsc_tx_rules_swing_set(rules, db['swing'])


def helper_config_rx_rules(rules, db):
    api.hsc_rx_rules_dsp_mode_set(rules, db['dsp_mode'])
    api.hsc_rx_rules_polarity_set(rules, db['invert'])
    api.hsc_rx_rules_gray_mapping_enable(rules, db['gray_map'])
    api.hsc_rx_rules_dfe_precoder_enable(rules, db['dfe_precoder_en'])
    api.hsc_rx_rules_vga_tracking_enable(rules, db['vga_tracking_en'])
    api.hsc_rx_rules_autoctle_enable(rules, db['auto_ctle'])
    api.hsc_rx_rules_scdr_enable(rules, db['scdr_en'])
    if db['auto_ctle'] == False:
        api.hsc_rx_rules_ctle_code_set(rules, db['ctle'][0], 0)
        api.hsc_rx_rules_ctle_code_set(rules, db['ctle'][1], 1)

    adv_rules = api.hsc_rx_rules_advanced_t()
    adv_rules.mlsd_en = db['mlsd_en']
    adv_rules.afe_trim = db['afe_trim']

    # DEBUG Advanced
    adv_rules.ffe_leakage_eta      = 7
    adv_rules.ffe_fir_adapt_force  = False
    adv_rules.ffe_gain_adapt_force = False
    adv_rules.ffe_dc_adapt_force   = False
    adv_rules.skip_dsp_fine_tune   = False
    
    api.hsc_rx_rules_advanced_set(rules, adv_rules)

def prbs_generator_config(device, db):
    '''
    The following function describes the sequence configuration of example of
    configure prbs generator rules for host/line transmit
    '''

    if not db.get('prbs'):
        return api.HSC_OK

    # Construct generator rules
    gen_rule = api.hsc_prbs_gen_rules_t()
    api.hsc_dev_prbs_gen_rules(device, gen_rule)
    status = api.HSC_OK

    # Config generator rules of line prbs
    if db['prbs']['line_is_generate']:
        helper_config_line_prbs_gen_rules(gen_rule, db['prbs'])
        for idx in range(len(db['line_channel'])):
            chn_id = db['line_channel'][idx]
            prbs = api.hsc_prbs_t()
            api.hsc_dev_prbs(device, chn_id, api.HSC_INTF_LTX, prbs)
            status |= api.hsc_prbs_gen_rules_apply(prbs, gen_rule)

    # Config generator rules of host prbs
    if db['prbs']['host_is_generate']:
        helper_config_host_prbs_gen_rules(gen_rule, db['prbs'])
        for idx in range(len(db['host_channel'])):
            chn_id = db['host_channel'][idx]
            prbs = api.hsc_prbs_t()
            api.hsc_dev_prbs(device, chn_id, api.HSC_INTF_HTX, prbs)
            status |= api.hsc_prbs_gen_rules_apply(prbs, gen_rule)

    return status


def prbs_checker_config_status_show(device, db):
    '''
    The following function describes the sequence configuration of example of
    configure prbs checker rules for host/line receive
    '''

    if not db.get('prbs'):
        return api.HSC_OK

    # Construct checker rules
    chk_rule = api.hsc_prbs_chk_rules_t()
    api.hsc_dev_prbs_chk_rules(device, chk_rule)
    status = api.HSC_OK

    # Config checker rules of line prbs
    if db['prbs']['line_is_check']:
        helper_config_line_prbs_chk_rules(chk_rule, db['prbs'])
        for idx in range(len(db['line_channel'])):
            chn_id = db['line_channel'][idx]
            prbs = api.hsc_prbs_t()
            api.hsc_dev_prbs(device, chn_id, api.HSC_INTF_LRX, prbs)
            status |= api.hsc_prbs_chk_rules_apply(prbs, chk_rule)

            # Clear status/counter right after init checker
            prbs_status = api.hsc_prbs_chk_status_t()
            api.hsc_prbs_chk_status_query(prbs, prbs_status)

    # Config checker rules of host prbs
    if db['prbs']['host_is_check']:
        helper_config_host_prbs_chk_rules(chk_rule, db['prbs'])
        for idx in range(len(db['host_channel'])):
            chn_id = db['host_channel'][idx]
            prbs = api.hsc_prbs_t()
            api.hsc_dev_prbs(device, chn_id, api.HSC_INTF_HRX, prbs)
            status |= api.hsc_prbs_chk_rules_apply(prbs, chk_rule)

            # Clear status/counter right after init checker
            prbs_status = api.hsc_prbs_chk_status_t()
            api.hsc_prbs_chk_status_query(prbs, prbs_status)

    time.sleep(1)

    if db['prbs']['line_is_check']:
        for idx in range(len(db['line_channel'])):
            chn_id = db['line_channel'][idx]
            prbs = api.hsc_prbs_t()
            api.hsc_dev_prbs(device, chn_id, api.HSC_INTF_LRX, prbs)
            api.hsc_prbs_chk_status_show(prbs)

    if db['prbs']['host_is_check']:
        for idx in range(len(db['host_channel'])):
            chn_id = db['host_channel'][idx]
            prbs = api.hsc_prbs_t()
            api.hsc_dev_prbs(device, chn_id, api.HSC_INTF_HRX, prbs)
            api.hsc_prbs_chk_status_show(prbs)

    return status


def helper_an_rules_set(an_rules, db):
    api.hsc_an_rules_enable(an_rules, True)
    api.hsc_an_rules_mode_set(an_rules, db['mode'])
    api.hsc_an_rules_link_time_budget_set(an_rules, db['time_budget'])
    api.hsc_an_rules_pause_ability_set(an_rules, db['pause'])
    api.hsc_an_rules_remote_fault_enable(an_rules, db['rmt_fault'])
    
    cap = api.hsc_an_cap_t()
    cap.advertise = True
    for ad in db['cap']["advertise"]:
        api.hsc_an_rules_cap_ad_set(an_rules, ad, cap)

def helper_lt_rules_set(lt_rules, db):
    api.hsc_lt_rules_enable(lt_rules, True)
    api.hsc_lt_rules_target_snr_set(lt_rules, db['target_snr'])
    api.hsc_lt_rules_fir_walk_enable(lt_rules, db['fir_walk_en'])
    api.hsc_lt_rules_auto_invert_enable(lt_rules, db['auto_inv_en'])
    api.hsc_lt_rules_extended_link_time_set(lt_rules, db['ext_link_time'])



# Bundle Declarations

def helper_bundle_rules_set(dev, bundle_rules, bundle_db):

    # Set baudrate/signalling and channels belong to bundle to bundle rules
    # setup the data rate on each channel
    api.hsc_bundle_rules_baud_rate_set(bundle_rules, bundle_db['host_baud_rate'])
    api.hsc_bundle_rules_signalling_set(bundle_rules, api.HSC_INTF_HOST, bundle_db['host_signalling'])
    api.hsc_bundle_rules_signalling_set(bundle_rules, api.HSC_INTF_LINE, bundle_db['line_signalling'])
    api.hsc_bundle_rules_ieee_demap_enable(bundle_rules, bundle_db['ieee_demap'])

    # use physical channels on the line and host
    # the rules channels field is a bitmask with an enable bit for each channel
    # to bind/associate with the bundle.
    host_mask = 0
    line_mask = 0
    for i in range(len(bundle_db['host_channel'])):
        host_mask |= 1 << (bundle_db['host_channel'][i])
    api.hsc_bundle_rules_chns_mask_set(bundle_rules, api.HSC_INTF_HOST, host_mask)
    for i in range(len(bundle_db['line_channel'])):
        line_mask |= 1 << (bundle_db['line_channel'][i])
    api.hsc_bundle_rules_chns_mask_set(bundle_rules, api.HSC_INTF_LINE, line_mask)


def device_get(asic_id):
    cur_dev = api.hsc_dev_t()
    api.hsc_dev(cur_dev, asic_id)
    return cur_dev


def helper_config_line_prbs_gen_rules(gen_rule, db):
    api.hsc_prbs_gen_rules_mode_set(gen_rule, db['line_generate_mode'])
    api.hsc_prbs_gen_rules_pattern_set(gen_rule, db['line_pattern'])
    api.hsc_prbs_gen_rules_enable(gen_rule, True)


def helper_config_line_prbs_chk_rules(chk_rule, db):
    api.hsc_prbs_chk_rules_mode_set(chk_rule, db['line_check_mode'])
    api.hsc_prbs_chk_rules_pattern_set(chk_rule, db['line_pattern'])
    api.hsc_prbs_chk_rules_enable(chk_rule, True)


def helper_config_host_prbs_gen_rules(gen_rule, db):
    api.hsc_prbs_gen_rules_mode_set(gen_rule, db['host_generate_mode'])
    api.hsc_prbs_gen_rules_pattern_set(gen_rule, db['host_pattern'])
    api.hsc_prbs_gen_rules_enable(gen_rule, True)


def helper_config_host_prbs_chk_rules(chk_rule, db):
    api.hsc_prbs_chk_rules_mode_set(chk_rule, db['host_check_mode'])
    api.hsc_prbs_chk_rules_pattern_set(chk_rule, db['host_pattern'])
    api.hsc_prbs_chk_rules_enable(chk_rule, True)


def bundle_bring_up(bundles, bundle_rules, bundle_id):

    # Initialize the bundle and tear down any resources that may
    # already be allocated.
    status = api.hsc_bundle_init(bundles, bundle_rules)
    if status != api.HSC_OK:
        print("hsc_bundle_init bundle %x FAILED" % bundle_id)

    # Apply rules to ASIC to bring the bundle up.
    status |= api.hsc_bundle_start(bundles, bundle_rules)
    if status != api.HSC_OK:
        print("hsc_bundle_start bundle %x FAILED" % bundle_id)

    return status

def bundle_config(device, bundle_idx, db):
    """
    The following function describes the sequence configuration of example datapath:
    1. Prepare the set of attributes/rules in bundle rules
    - Attributes/rules on bundle layer
    - Attributes/rules transmit, receive,... on channel layer
    2. Applying bundle rules to ASIC to bring bundle up
    """

    bundle_rules_db = db['bundle'][bundle_idx]

    # Allocate bundle base on input database
    # assign a channel to represent the bundle. When
    # dealing with bundles this is always a physical
    # channel from the perspective of the host receiver.
    bundle = api.hsc_bundle_t()
    bundle_id = min(bundle_rules_db['host_channel'] or bundle_rules_db['line_channel'])
    api.hsc_dev_bundle(device, bundle_id, bundle)

    # Construct bundle rules base on the desired application
    # then prepare a set of attributes base on the target application
    bundle_rules = api.hsc_bundle_rules_t()
    api.hsc_dev_bundle_rules(dev, bundle_rules_db['mode'], bundle_rules)

    # Set attributes of bundle layer
    helper_bundle_rules_set(device, bundle_rules, bundle_rules_db)

    # Set attributes of LTX
    for idx in range(len(bundle_rules_db['line_channel'])):
        chn_id = bundle_rules_db['line_channel'][idx]

        # Get the reference to line tx_rules in bundle rules
        # then set tx attributes to bundle rules via tx_rules
        tx_rules = api.hsc_chn_tx_rules(bundle_rules, chn_id, api.HSC_INTF_LINE)
        helper_tx_rules_set(tx_rules, db['default']['line_tx']) if bundle_rules_db['config_channel']['default'] == True else helper_tx_rules_set(tx_rules, db['line_tx'][chn_id])

    # Set attributes of HTX
    for idx in range(len(bundle_rules_db['host_channel'])):
        chn_id = bundle_rules_db['host_channel'][idx]

        # Get the reference to host tx_rules in bundle rules
        # then set tx attributes to bundle rules via tx_rules
        tx_rules = api.hsc_chn_tx_rules(bundle_rules, chn_id, api.HSC_INTF_HOST)
        helper_tx_rules_set(tx_rules, db['default']['host_tx']) if bundle_rules_db['config_channel']['default'] == True else helper_tx_rules_set(tx_rules, db['host_tx'][chn_id])

    # Set attributes of LRX
    for idx in range(len(bundle_rules_db['line_channel'])):
        chn_id = bundle_rules_db['line_channel'][idx]

        # Get reference to line rx_rules in bundle rules
        # then set rx attributes to bundle rules via rx_rules
        rx_rules = api.hsc_chn_rx_rules(bundle_rules, chn_id, api.HSC_INTF_LINE)
        helper_config_rx_rules(rx_rules, db['default']['line_rx']) if bundle_rules_db['config_channel']['default'] == True else helper_config_rx_rules(rx_rules, db['line_rx'][chn_id])

    # Set attributes of HRX
    for idx in range(len(bundle_rules_db['host_channel'])):
        chn_id = bundle_rules_db['host_channel'][idx]

        # Get reference to host rx_rules in bundle rules
        # then set rx attributes to bundle rules via rx_rules
        rx_rules = api.hsc_chn_rx_rules(bundle_rules, chn_id, api.HSC_INTF_HOST)
        helper_config_rx_rules(rx_rules, db['default']['host_rx']) if bundle_rules_db['config_channel']['default'] == True else helper_config_rx_rules(rx_rules, db['host_rx'][chn_id])

    if bundle_rules_db.get('host_an_en') == True:
        an_rules = api.hsc_an_rules(bundle_rules, api.HSC_INTF_HOST)
        helper_an_rules_set(an_rules, bundle_rules_db['host_an'])

    if bundle_rules_db.get('host_lt_en') == True:
        lt_rules = api.hsc_lt_rules(bundle_rules, api.HSC_INTF_HOST)
        helper_lt_rules_set(lt_rules, bundle_rules_db['host_lt'])

    if bundle_rules_db.get('line_an_en') == True:
        an_rules = api.hsc_an_rules(bundle_rules, api.HSC_INTF_LINE)
        helper_an_rules_set(an_rules, bundle_rules_db['line_an'])

    if bundle_rules_db.get('line_lt_en') == True:
        lt_rules = api.hsc_lt_rules(bundle_rules, api.HSC_INTF_LINE)
        helper_lt_rules_set(lt_rules, bundle_rules_db['line_lt'])

    # Bring bundle up by applying bundle rules to ASIC
    status = bundle_bring_up(bundle, bundle_rules, bundle_id)
    print("Bring up bundle_id %d: %s" % (bundle_id, 'SUCCESS' if status == api.HSC_OK else 'FAILED'))

    if bundle_rules_db['show_config']:
        api.hsc_bundle_rules_show(bundle)

    return status


def reset_all_bundles():
    num_bundles = api.hsc_dev_num_chns(dev, api.HSC_INTF_HOST)
    bundles = api.hsc_bundle_t()
    bundle_rules = api.hsc_bundle_rules_t()

    for bundle_id in range(num_bundles):
        api.hsc_dev_bundle_rules(dev, api.HSC_OPER_MODE_DUPLEX_RETIMER, bundle_rules)
        api.hsc_dev_bundle(dev, bundle_id, bundles)
        api.hsc_bundle_rules_chns_mask_set(bundle_rules, api.HSC_INTF_HOST | api.HSC_INTF_LINE, 0)
        status = api.hsc_bundle_init(bundles, bundle_rules)

def main():
    asic_id = 0
    dev = device_get(asic_id)
    status = api.HSC_OK

    api.hsc_dev_i2c_access_enable(dev, chip_conf['i2c_enable'])

    # Delete all bundles
    reset_all_bundles()

    # download fw
    if chip_conf['firmware']['download_firmware']:
        mcu_broadcast_mask = api.HSC_DEV_BROADCAST_MCU_ID
        dnld = api.hsc_dnld_t()
        api.hsc_dev_mcu_dnld(dev, mcu_broadcast_mask, dnld)
            
        if chip_conf['firmware']['is_dnld_from_file']:
            fw_path = chip_conf['firmware']['firmware_path']
            api.hsc_dnld_download_from_file(dnld, fw_path)
        else:
            api.hsc_dnld_download(dnld)# Bring up service


    num_bundles = len(chip_conf.get('bundle', []))
    bundle = api.hsc_bundle_t()

    for bundle_idx in range(num_bundles):
        # Allocate bundle id base on input database
        # assign a channel to represent the interface.
        bundle_id = min(chip_conf['bundle'][bundle_idx]['host_channel'] or chip_conf['bundle'][bundle_idx]['line_channel'])
        api.hsc_dev_bundle(dev, bundle_id, bundle)

        # Apply bundle configure
        status |= bundle_config(dev, bundle_idx, chip_conf)
        if status != api.HSC_OK:
            print("ERROR: Configure bundle FAILED")
            return api.HSC_ERROR

        # Config generator prbs
        status |= prbs_generator_config(dev, chip_conf['bundle'][bundle_idx])

        # Wait for link ready
        if chip_conf['bundle'][bundle_idx]['wait_link_ready']:
            is_ready = api.hsc_bundle_link_ready_wait(bundle, 2000 * 1000)
            if not is_ready:
                status |= api.HSC_ERROR
                print("hsc_bundle_link_ready_wait bundle %x fail" % bundle_id)

        # Config checker prbs and
        status |= prbs_checker_config_status_show(dev, chip_conf['bundle'][bundle_idx])

        if chip_conf['bundle'][bundle_idx]['show_link_status']:
            api.hsc_bundle_status_show(bundle)

    return status

if __name__ == '__main__':
    start_time = time.time()
    status = main()
    print("Finish example", 'SUCCESS' if status == api.HSC_OK else 'FAILED')
    print("--- %s seconds ---" % (time.time() - start_time))

# Pyhon file trail configuration
```

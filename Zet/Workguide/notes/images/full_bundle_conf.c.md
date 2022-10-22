/** @file gen_code_template.c
 ******************************************************************************
 *
 * @brief
 *   Example API script to configure the Lynx ASIC
 *
 ******************************************************************************
 *
 * @author
 *   This file contains information that is proprietary and confidential to
 *   Inphi Corporation.
 *
 *   Copyright (C)  Inphi Corp. All rights reserved.
 *
 ******************************************************************************/
#include "hsc_api.h"
#include <stdlib.h>

#define NUM_CHNS 4
#define CHN_MASK HSC_BIT3_0
#define NUM_FLOWS   (8)
#define STATUS_2_STR(status) status == HSC_OK ? "HSC_OK" : "HSC_ERROR"

#define ARRAY_SIZE(array)  ((uint8_t)(sizeof(array) / sizeof((array)[0])))
#define ARRAY_MASK(array) \
({ \
        int i, mask = 0; \
        for (i = 0; i < ARRAY_SIZE(array); i++) \
            mask |= 1 << array[i]; \
        mask; \
})


uint32_t host_chns_0[] = {0, 1, 2, 3};
uint32_t line_chns_0[] = {0, 1, 2, 3};
uint8_t num_host_chns_0 = ARRAY_SIZE(host_chns_0);
uint8_t num_line_chns_0 = ARRAY_SIZE(line_chns_0);

hsc_bundle_rules_t rules;


#define XBAR_PASSTHROUGH    1
#define XBAR_CROSS          2
#define XBAR_LOOPBACK       3

static uint8_t xbar_cross_mode = XBAR_PASSTHROUGH;

static hsc_status_t xbar_rules_passthrough_set(hsc_xbar_rules_t *xbar_rules)
{
    hsc_status_t status = HSC_OK;
    uint8_t flw_idx;
    uint32_t chn_from, chn_to;
    uint8_t intf_from, intf_to;
    uint32_t flows_passthrough[8][4] = {
            { 0, HSC_INTF_LINE, 0, HSC_INTF_HOST }, /* Define the connection FROM [0, HSC_INTF_LINE] TO [0, HSC_INTF_HOST] */
            { 1, HSC_INTF_LINE, 1, HSC_INTF_HOST }, /* ... */
            { 2, HSC_INTF_LINE, 2, HSC_INTF_HOST },
            { 3, HSC_INTF_LINE, 3, HSC_INTF_HOST },

            { 0, HSC_INTF_HOST, 0, HSC_INTF_LINE },
            { 1, HSC_INTF_HOST, 1, HSC_INTF_LINE },
            { 2, HSC_INTF_HOST, 2, HSC_INTF_LINE },
            { 3, HSC_INTF_HOST, 3, HSC_INTF_LINE }, };

    for (flw_idx = 0; flw_idx < NUM_FLOWS; flw_idx++)
    {
        chn_from = flows_passthrough[flw_idx][0];
        chn_to   = flows_passthrough[flw_idx][2];
        intf_from= flows_passthrough[flw_idx][1];
        intf_to  = flows_passthrough[flw_idx][3];
        status |= hsc_xbar_rules_chn_connect(xbar_rules, chn_from, intf_from, chn_to, intf_to);
    }

    return status;
}

static hsc_status_t xbar_rules_cross_set(hsc_xbar_rules_t *xbar_rules)
{
    hsc_status_t status = HSC_OK;
    uint8_t flw_idx;
    uint32_t chn_from, chn_to;
    uint8_t intf_from, intf_to;
    static uint32_t flows_cross[8][4] = {
            { 0, HSC_INTF_LINE, 3, HSC_INTF_HOST },
            { 1, HSC_INTF_LINE, 2, HSC_INTF_HOST },
            { 2, HSC_INTF_LINE, 1, HSC_INTF_HOST },
            { 3, HSC_INTF_LINE, 0, HSC_INTF_HOST },

            { 0, HSC_INTF_HOST, 3, HSC_INTF_LINE },
            { 1, HSC_INTF_HOST, 2, HSC_INTF_LINE },
            { 2, HSC_INTF_HOST, 1, HSC_INTF_LINE },
            { 3, HSC_INTF_HOST, 0, HSC_INTF_LINE }, };

    for (flw_idx = 0; flw_idx < NUM_FLOWS; flw_idx++)
    {
        chn_from  = flows_cross[flw_idx][0];
        intf_from = flows_cross[flw_idx][1];
        chn_to    = flows_cross[flw_idx][2];
        intf_to   = flows_cross[flw_idx][3];
        status |= hsc_xbar_rules_chn_connect(xbar_rules, chn_from, intf_from, chn_to, intf_to);
    }

    return status;
}

static hsc_status_t xbar_rules_loopback_set(hsc_xbar_rules_t *xbar_rules)
{
    hsc_status_t status = HSC_OK;
    uint8_t flw_idx;
    uint32_t chn_from, chn_to;
    uint8_t intf_from, intf_to;
    uint32_t flows_loopback[8][4] = {
            { 0, HSC_INTF_LINE, 0, HSC_INTF_LINE },
            { 1, HSC_INTF_LINE, 1, HSC_INTF_LINE },
            { 2, HSC_INTF_LINE, 2, HSC_INTF_LINE },
            { 3, HSC_INTF_LINE, 3, HSC_INTF_LINE },

            { 0, HSC_INTF_HOST, 0, HSC_INTF_HOST },
            { 1, HSC_INTF_HOST, 1, HSC_INTF_HOST },
            { 2, HSC_INTF_HOST, 2, HSC_INTF_HOST },
            { 3, HSC_INTF_HOST, 3, HSC_INTF_HOST }, };

    for (flw_idx = 0; flw_idx < NUM_FLOWS; flw_idx++)
    {
        chn_from  = flows_loopback[flw_idx][0];
        intf_from = flows_loopback[flw_idx][1];
        chn_to    = flows_loopback[flw_idx][2];
        intf_to   = flows_loopback[flw_idx][3];
        status |= hsc_xbar_rules_chn_connect(xbar_rules, chn_from, intf_from, chn_to, intf_to);
    }

    return status;
}

static hsc_status_t xbar_rules_configure(hsc_xbar_rules_t *xbar_rules, uint8_t connect_mode)
{
    if (connect_mode == XBAR_PASSTHROUGH)
        return xbar_rules_passthrough_set(xbar_rules);

    if (connect_mode == XBAR_CROSS)
        return xbar_rules_cross_set(xbar_rules);

    if (connect_mode == XBAR_LOOPBACK)
        return xbar_rules_loopback_set(xbar_rules);

    return HSC_ERROR;
}

/**
 *
 * The following example describes the sequence configuration of example datapath
 *
 * @param bundle          [I] - The bundle being accessed.
 *
 * @return HSC_OK on success, HSC_ERROR on failure
 */
hsc_status_t bundle_config_0(hsc_bundle_t *bundle)
{
    /*
     * Below is the bundle rules configuration
     *
     * Channel is activated in bundle:
     * - Host TX channel [0, 1, 2, 3]
     * - Host RX channel [0, 1, 2, 3]
     * - Line TX channel [0, 1, 2, 3]
     * - Line RX channel [0, 1, 2, 3]
     */

    uint32_t chn_idx;
    hsc_status_t status = HSC_OK;
    hsc_dev_t *dev = hsc_bundle_dev_get(bundle);

    /* Default the bundle rules based on the desired application */
    if (hsc_dev_bundle_rules(dev, HSC_OPER_MODE_DUPLEX_RETIMER, &rules) == NULL)
    {
        HSC_CRIT("Failed construct the bundle rule\n");
        return HSC_ERROR;
    }

    /* Setup the data rate on each channel */
    hsc_bundle_rules_baud_rate_set(&rules, HSC_BAUD_RATE_26p5625G);
    hsc_bundle_rules_ieee_demap_enable(&rules, false);

    /* Use physical channels on the Line and host
     * The rules. Channel  bitmask with an enable bit for each channel
     * to bind/associate with the bundle/bundle.
     */

    /* Configure Host channel mask */
    hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_HOST, ARRAY_MASK(host_chns_0));

    /* Configure Line channel mask */
    hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_LINE, ARRAY_MASK(line_chns_0));

    /* Host have to operate in PAM/NRZ mode to get desired data rate per channel */
    hsc_bundle_rules_signalling_set(&rules, HSC_INTF_HOST, HSC_SIGNAL_MODE_PAM);

    /* Line have to operate in PAM/NRZ mode to get desired data rate per channel */
    hsc_bundle_rules_signalling_set(&rules, HSC_INTF_LINE, HSC_SIGNAL_MODE_PAM);

    /* Below is Host TX rules configuration information */
    hsc_tx_rules_t *tx_rules = NULL;
    for (chn_idx = 0; chn_idx < num_host_chns_0; chn_idx++)
    {

        int16_t host_tx_taps[] = {-50, 650, 0, 0, 0, 0, 0};

        /* Configure Host TX rules */
        tx_rules = hsc_chn_tx_rules(&rules, host_chns_0[chn_idx], HSC_INTF_HTX);
        hsc_tx_rules_fir_taps_set(tx_rules, HSC_TX_LUT_3TAP, host_tx_taps);
        hsc_tx_rules_swing_set(tx_rules, HSC_TX_SWING_100p);
        hsc_tx_rules_eye_set(tx_rules, HSC_EYE_LEVEL_LOWER, 1000);
        hsc_tx_rules_eye_set(tx_rules, HSC_EYE_LEVEL_UPPER, 2000);
        hsc_tx_rules_gray_mapping_enable(tx_rules, true);
        hsc_tx_rules_dfe_precoder_enable(tx_rules, false);
        hsc_tx_rules_polarity_set(tx_rules, false);
    }
    
    /* Below is the line TX rules configuration information */
    for (chn_idx = 0; chn_idx < num_line_chns_0; chn_idx++)
    {

        int16_t line_tx_taps[] ={-50, 650, 0, 0, 0, 0, 0};

        /* Line TX rules */
        tx_rules = hsc_chn_tx_rules(&rules, line_chns_0[chn_idx], HSC_INTF_LINE);
        hsc_tx_rules_fir_taps_set(tx_rules, HSC_TX_LUT_3TAP, line_tx_taps);
        hsc_tx_rules_swing_set(tx_rules,  HSC_TX_SWING_100p);
        hsc_tx_rules_eye_set(tx_rules, HSC_EYE_LEVEL_LOWER, 1000);
        hsc_tx_rules_eye_set(tx_rules, HSC_EYE_LEVEL_UPPER, 2000);
        hsc_tx_rules_gray_mapping_enable(tx_rules, true);
        hsc_tx_rules_dfe_precoder_enable(tx_rules, false);
        hsc_tx_rules_polarity_set(tx_rules, false);
    }
    
    /* Below is the host RX rules configuration information */
    hsc_rx_rules_t *rx_rules = NULL;
    hsc_rx_rules_advanced_t host_rx_adv_rules;
    for (chn_idx = 0; chn_idx < num_host_chns_0; chn_idx++)
    {
        uint16_t ctle_host[] = {0, 0};
        host_rx_adv_rules.afe_trim = HSC_AFE_TRIM_AUTO;
        host_rx_adv_rules.mlsd_en = false;

        /* Host RX rules */
        rx_rules = hsc_chn_rx_rules(&rules, host_chns_0[chn_idx], HSC_INTF_HOST);
        hsc_rx_rules_dsp_mode_set(rx_rules, HSC_DSP_MODE_SLC1);
        hsc_rx_rules_autoctle_enable(rx_rules, true);
        hsc_rx_rules_gray_mapping_enable(rx_rules, true);
        hsc_rx_rules_polarity_set(rx_rules, false);
        hsc_rx_rules_advanced_set(rx_rules, &host_rx_adv_rules);
        hsc_rx_rules_vga_tracking_enable(rx_rules, false);
        hsc_rx_rules_dfe_precoder_enable(rx_rules, false);
        hsc_rx_rules_scdr_enable(rx_rules, false);
    }
    
    /* Below is the line RX rules configuration information */
    hsc_rx_rules_advanced_t line_rx_adv_rules;
    for (chn_idx = 0; chn_idx < num_line_chns_0; chn_idx++)
    {
        uint16_t ctle_line[] = {0, 0};
        line_rx_adv_rules.afe_trim = HSC_AFE_TRIM_AUTO;
        line_rx_adv_rules.mlsd_en = false;

        /* Line RX rules */
        rx_rules = hsc_chn_rx_rules(&rules, line_chns_0[chn_idx], HSC_INTF_LINE);
        hsc_rx_rules_dsp_mode_set(rx_rules, HSC_DSP_MODE_SLC1);
        hsc_rx_rules_autoctle_enable(rx_rules, true);
        hsc_rx_rules_gray_mapping_enable(rx_rules, true);
        hsc_rx_rules_polarity_set(rx_rules, false);
        hsc_rx_rules_advanced_set(rx_rules, &line_rx_adv_rules);
        hsc_rx_rules_vga_tracking_enable(rx_rules, false);
        hsc_rx_rules_dfe_precoder_enable(rx_rules, false);
        hsc_rx_rules_scdr_enable(rx_rules, false);
    }
    
    /* Construct XBAR rules handler*/
    hsc_xbar_rules_t* xbar_rules = hsc_xbar_rules(&rules);
    if (xbar_rules == NULL)
    {
        HSC_CRIT("Construct xbar_rules FAIL\n");
        return HSC_ERROR;
    }
    xbar_rules_cross_set(xbar_rules);
    /* Initialize the bundle and tear down any resources that may
     * already be allocated.*/
    status = hsc_bundle_init(bundle, &rules);
    HSC_NOTE("hsc_bundle_init: %s\n", STATUS_2_STR(status));

    /* Bring the bundle up */
    status |= hsc_bundle_start(bundle, &rules);
    HSC_NOTE("hsc_bundle_start: %s\n", STATUS_2_STR(status));
    if (status != HSC_OK)
    {
        HSC_NOTE("Configure bundle: %s\n", STATUS_2_STR(status));
        return HSC_ERROR;
    }

    return status;
}

/**
 * This sample program a teardown all configuration of current bundles
 * @param dev         [I] - The device being accessed.
 *
 * @return HSC_OK on success, HSC_ERROR on failure
 */
static hsc_status_t bundles_teardown(hsc_dev_t *dev)
{
    hsc_status_t status = HSC_OK;
    uint32_t bundle_id = 0;
    uint32_t max_bundle_nums = hsc_dev_num_bundles(dev);

    if (hsc_dev_bundle_rules(dev, HSC_OPER_MODE_DUPLEX_RETIMER, &rules) == NULL)
    {
        HSC_CRIT("Failed construct the bundle rule\n");
        return HSC_ERROR;
    }

    /* Init all 16 bundles */
    for (bundle_id = 0; bundle_id < max_bundle_nums; bundle_id++)
    {
        hsc_bundle_t bundle;

        hsc_dev_bundle(dev, bundle_id, &bundle);
        hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_HOST | HSC_INTF_LINE, 0);
        status |= hsc_bundle_init(&bundle, &rules);
        if (status != HSC_OK)
        {
            HSC_WARN("hsc_bundle_init bundle %d: FAILED\n", bundle_id);
        }
    }
    return status;
}

/**
 * This is the main wrapper method for the example.
 *
 * @param argc [I] - The number of input arguments in argv[]
 * @param argv [I] - The array of input arguments
 *
 * @return The return code to the OS (0 == success, anything else for failure)
 */
int main(int argc, char* argv[])
{
    int rc = EXIT_SUCCESS;
    hsc_status_t status = HSC_OK;
    bool flag_wait_link_ready    = false;
    bool flag_show_link_status   = false;
    bool flag_i2c_enable         = false;

    /* Device handle */
    static hsc_dev_t device;

    /* Connect back to the GUI for register access */
    hsc_gui_connect(argc, argv);

    /* Construct */
    if (hsc_dev(&device, 0 /* asic_id */) == NULL)
    {
        hsc_gui_close();
        return EXIT_FAILURE;
    }

    hsc_dev_i2c_access_enable(&device, flag_i2c_enable);

    /* Teardown all current active bundles */
    bundles_teardown(&device);
    
    /* Configure for bundle 0 */
    hsc_bundle_t bundle_0;
    uint32_t bundle_id_0 = 0;

    hsc_dev_bundle(&device, bundle_id_0, &bundle_0);
    status |= bundle_config_0(&bundle_0);
    

    flag_wait_link_ready    = false;
    if (flag_wait_link_ready)
    {
        /* Wait for the bundle to be ready, timeout = 2s */
        status |= hsc_bundle_link_ready_wait(&bundle_0, 2000*1000) == true ? HSC_OK : HSC_ERROR;
        HSC_NOTE("\nhsc_bundle_link_ready_wait: %s\n", STATUS_2_STR(status));
    }
    flag_show_link_status   = false;
    if (flag_show_link_status)
    {
        hsc_bundle_status_show(&bundle_0);
    }
    
    if(status != HSC_OK)
    {
        HSC_NOTE("Example failed\n");
        rc = EXIT_FAILURE;
    }

    hsc_gui_close();

    return rc;
}
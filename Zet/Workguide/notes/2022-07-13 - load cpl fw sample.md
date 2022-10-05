---
title: load cpl fw sample
created: 2022-Jul-13
tags:
  - 'permanent/common'
---

```c
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

/**
 * This sample program a specific image of the firmware to MCU's RAM from system file.
 * In this case, the API will need OS file system support.
 * @param dev         [I] - The device being accessed.
 *
 * @return HSC_OK on success, HSC_ERROR on failure
 */
static hsc_status_t firmware_download(hsc_dev_t *dev)
{
    hsc_status_t status = HSC_OK;
    hsc_dnld_t dnld;

    const uint32_t core_mcu_id_mask = 0x3C0;
    const char *core_mcu_firmware_filename = "C:/Users/hcmswlab/Downloads/inphi_exp_lynx_internal_nightly_6_1_389/support/drivers/lynx_400/ucode/cpl_direct_download_0_12_0_2345.txt";
    bool is_dnld_from_file = true;

    /* Construct the download handler */
    if (hsc_dev_mcu_dnld(dev, core_mcu_id_mask, &dnld) == NULL)
        return HSC_ERROR;

    /* Disable verifying firmware after download */
    hsc_dnld_verify_enable(&dnld, false);

    /* Download the firmware to the ASIC and jump to the new firmware image */
    if (is_dnld_from_file)
    {   
        status |= hsc_dnld_download_from_file(&dnld, core_mcu_firmware_filename);
    }
    else
    {
        status |= hsc_dnld_download(&dnld);
    }
    if (status != HSC_OK)
        HSC_CRIT("Failed programming the application core mcu firmware\n");

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


    /* Firmware download */
    status |= firmware_download(&device);
    
    hsc_gui_close();

    return rc;
}
```

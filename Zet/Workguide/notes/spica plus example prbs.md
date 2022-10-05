# spica plus dual prbs example

```c
/** $file$
 *****************************************************************************
 *
 * @brief
 *    This module provides an example of configuring the xbars 
 *
 *****************************************************************************
$copy$
 ****************************************************************************/
#include "spica_api.h"

/**
 * @return INPHI_OK on success, INPHI_ERROR on failure
 */
inphi_status_t example_init_dual_prbs(uint32_t die)
{
    inphi_status_t status = INPHI_OK;

    e_spica_operational_mode operational_mode = SPICA_MODE_DUAL_PRBS;
    e_spica_protocol_mode protocol_mode       = SPICA_MODE_200G_4Px26p6_TO_4Px26p6;

    spica_rules_t rules;

    // BUNDLE RULES
    spica_bundle_rules_t bundle_rules;

    // set the bundle defaults
    spica_bundle_default_set(die, &bundle_rules);

    // apply the bundle rules to the bundle overlays
    spica_bundle_cfg(&bundle_rules);

    status |= spica_rules_default_set(die, operational_mode, protocol_mode, &rules);
    if(INPHI_OK != status)
    {
        INPHI_NOTE("Error with spica_rules_default_set\n");
        return status;
    }

    // Chip Init
    status |= spica_init(die, &rules);
    if(INPHI_OK != status)
    {
        INPHI_NOTE("Error with spica_init\n");
        return status;
    }

    // Chip Configuration
    status |= spica_enter_operational_state(die, &rules);
    if(INPHI_OK != status)
    {
        INPHI_NOTE("Error with spica_enter_operational_state\n");
        return status;
    }
        
    if(INPHI_OK != status)
    {
        INPHI_NOTE("Warning: failed initializing die %x\n", die);
    }    
   
    return status;
}
```
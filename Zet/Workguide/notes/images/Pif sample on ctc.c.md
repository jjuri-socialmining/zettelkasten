#include "ctc_api.h"
#include "ctc_gui.h" // Required for Inphi Explorer
#include <stdlib.h>

inphi_status_t your_code_here()
{
    inphi_status_t status = INPHI_OK;

    // Fetch the current die of the active ASIC in the GUI
    uint32_t die = inphi_gui_get_current_die();

    uint16_t dev_id_low = 0;
    uint16_t dev_id_high = 0;
    uint32_t buff[4];
    // Enter your code here
    ctc_mcu_pif_read(die, 0x5ff80000, buff, 4);
    
    INPHI_PRINTF("0x%08x\n0x%08x\n0x%08x\n0x%08x\n", buff[0], buff[1], buff[2], buff[3]);
    
    return status;
}

/**
 * This is the main wrapper method for the example. It connects
 * back to the GUI to perform register reads and writes.
 */
int main(int argc, char* argv[])
{
    int rc = EXIT_SUCCESS;
    inphi_status_t status = INPHI_OK;

    // Connect back to the GUI for register access
    inphi_gui_connect(argc, argv);

    status |= your_code_here();

    if(status != INPHI_OK)
    {
        INPHI_PRINTF("Example failed\n");
        rc = EXIT_FAILURE;
    }

    inphi_gui_close();
    
    return rc;
}

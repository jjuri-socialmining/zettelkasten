
https://dc5lp-vinetx000.marvell.com:8443/etx/
```
user: dutran
pass: 3Kt#71Ib$
```

```
cd firmware/application
make -f build.inc build
```

log
```
bash-4.2$ git checkout users/phnguyen_cpls_775
M       .gitmodules
M       firmware/application/an_lt
Branch users/phnguyen_cpls_775 set up to track remote branch users/phnguyen_cpls_775 from origin.
Switched to a new branch 'users/phnguyen_cpls_775'
bash-4.2$ 
bash-4.2$ make -f build.inc build
/home/dutran/projects/hsc/capella/firmware/application//../../../../bin/make/os.inc:20: "Detected Linux"
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-xcc -c -Wa,--gdwarf-2 -Wa,--text-section-literals -Iinc -DDISABLE_DIAG --xtensa-core=xt11b --xtensa-system=/inphi/hsio/sw/xtensa/RF-2016.4-linux/xt11b/config --xtensa-params="" src/reset-vector.S -o ./build-output/reset-vector.o
Building config header for capella
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-xcc --xtensa-core=xt11b --xtensa-system=/inphi/hsio/sw/xtensa/RF-2016.4-linux/xt11b/config --xtensa-params="" -mlsp=../XtensaInfo/Models/cpl_app_memmap/tiny -Iinc -Ilibwhirl -Iwhirl-gen -Ifw_common/inc -Ian_lt -I. \
            -std=c99 -Os -fmessage-length=0 \
             \
            -DDISABLE_DIAG -Wall -Werror -Wextra -Wpointer-arith -Wcast-align -Wno-unused -fshort-enums -o ./build-output/cpl_fw_app src/main.c src/reg_read_write.c src/reg_channel_map.c src/messaging.c src/cpl_api_intf.c src/cpl_top.c src/cpl_fw.c src/cpl_top_status.c src/efuse.c src/tx_fir.c src/cpl_rules.c src/cpl_vreg_fw.c src/cpl_pll_fw.c src/cpl_interrupt.c src/cpl_rx_ctle.c src/rx_dsp.c src/rx_fw.c src/rx_qc.c src/cpl_rx_histogram_fsm.c src/tx_fw.c src/self_test.c src/tmon.c src/fw_common_hook.c src/sw_intr.c src/refgen.c src/anlt_rules.c src/anlt_api_intf.c an_lt/an_lt_andor/anlt_andor.c an_lt/an_lt_andor/anlt_andor_emu.c an_lt/an_lt_bcst/anlt_bcst.c an_lt/an_lt_bcst/anlt_bcst_hwq_emu.c an_lt/an_lt_msg/anlt_msg.c an_lt/an_lt_msg/anlt_msg_hw_access.c an_lt/an_lt_msg/anlt_msg_hwq.c an_lt/an_lt_msg/anlt_msg_hwq_emu.c an_lt/an_lt_msg/anlt_msg_swq.c an_lt/anlt_timer.c an_lt/anlt_softmux.c an_lt/anlt_tstamp.c an_lt/an_api_intf.c an_lt/an_fsm.c an_lt/an_fw.c an_lt/an_fw_tx.c an_lt/an_lt.c an_lt/an_lt_impl.c an_lt/an_lt_utils.c an_lt/anlt_restart.c an_lt/lt_fsm.c an_lt/lt_fw.c an_lt/lt_fw_tx.c an_lt/rx_pmd_lt.c an_lt/tx_rem_reg_read_write.c fw_common/utils/common_utils.c fw_common/utils/time_utils.c fw_common/utils/logging.c fw_common/utils/exception.c fw_common/utils/ms_timer.c fw_common/utils/math.c src/ted_track/dfe.c src/ted_track/ffe.c src/ted_track/mmted.c src/ted_track/ted_track.c ./build-output/reset-vector.o
make -f build.inc generate_image
make[1]: Entering directory `/home/dutran/projects/hsc/capella/firmware/application'
/home/dutran/projects/hsc/capella/firmware/application//../../../../bin/make/os.inc:20: "Detected Linux"
Generating the Application Code Image
=====================================
python ../bin/gen_metadata.py -m "Alpha firmware release for customer integration\\\n Version: 0.11.0.1948\\\n Build: 15 Feb 2022 at 23:46" -o ./build-output/metadata.txt -l 256
Dumping the IRAM/DRAM for debug
===============================
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-dumpelf --base=0x5ffa0000 --size=0x20000 --no-bss --width=32 --little-endian --default=0x00000000 --sparse ./build-output/cpl_fw_app > ./build-output/iram.data
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-dumpelf --base=0x5ff80000 --size=0x10000 --no-bss --width=32 --little-endian --default=0x00000000 --sparse ./build-output/cpl_fw_app > ./build-output/dram.data
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-dumpelf --base=0x5ffa0000 --size=0x20000 --no-bss --width=32 --little-endian --default=0x00000000 --full ./build-output/cpl_fw_app > ./build-output/iram_full.data
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-dumpelf --base=0x5ff80000 --size=0x10000 --no-bss --width=32 --little-endian --default=0x00000000 --full ./build-output/cpl_fw_app > ./build-output/dram_full.data
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-objcopy --xtensa-core=xt11b --xtensa-system=/inphi/hsio/sw/xtensa/RF-2016.4-linux/xt11b/config --xtensa-params="" -O verilog --only-section ".data"   ./build-output/cpl_fw_app ./build-output/data.data
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-objcopy --xtensa-core=xt11b --xtensa-system=/inphi/hsio/sw/xtensa/RF-2016.4-linux/xt11b/config --xtensa-params="" -O verilog --only-section ".rodata" ./build-output/cpl_fw_app ./build-output/rodata.data
# Dissassemble the application code
/inphi/hsio/sw/xtensa/RF-2016.4-linux/XtensaTools/bin/xt-objdump --xtensa-core=xt11b --xtensa-system=/inphi/hsio/sw/xtensa/RF-2016.4-linux/xt11b/config --xtensa-params="" -rD ./build-output/cpl_fw_app > ./build-output/cpl_fw_app.dis
# Generate a trace file for debugging purposes
python ../bin/gen_trace.py -i ./build-output/cpl_fw_app.dis -o ./build-output/cpl_firmware_0_11_0_1948.trace.txt
cp ./build-output/cpl_firmware_0_11_0_1948.trace.txt ./build-output/trace.txt
# calculate the CRC-32 of the IRAM/DRAM, stuff values in tmp files
python --version
Python 2.7.8
python ../bin/crc_idram.py -i ./build-output/iram_full.data  > ./build-output/iram_crc.txt
python ../bin/crc_idram.py -i ./build-output/dram_full.data  > ./build-output/dram_crc.txt

Dumping the Image for IRAM/DRAM Upgrade
=======================================
# Generate the universal image for upgrading directly to IRAM/DRAM
python ../bin/merge_ram_images.py -f "hex" -c "Capella Firmware Image for Download to the IRAM/DRAM on the ASIC<br>  Version:      0.11.0.1948<br>  Build Date:  15 Feb 2022 at 23:46<br>  Description: Alpha firmware release for customer integration\\\n Version: 0.11.0.1948\\\n Build: 15 Feb 2022 at 23:46" \
                                                                                                                                  -i ./build-output/iram.data -d ./build-output/dram.data --iram_crc ../bin/iram_crc.txt --dram_crc ../bin/dram_crc.txt -o ./build-output/cpl_firmware_debug_direct_download_0_11_0_1948.txt
python ../bin/merge_ram_images.py -f "c" --comment_format="c" -c "Capella Firmware Image for API Development<br>  Version:      0.11.0.1948<br>  Build Date:  15 Feb 2022 at 23:46<br>  Description: Alpha firmware release for customer integration\\\n Version: 0.11.0.1948\\\n Build: 15 Feb 2022 at 23:46" \
                                                                                                                                  -i ./build-output/iram.data -d ./build-output/dram.data --iram_crc ../bin/iram_crc.txt --dram_crc ../bin/dram_crc.txt -o ./build-output/cpl_app_fw_image.h
# @echo ""
# @echo "Dumping the EEPROM image"
# @echo "======================================="
# # Generate the universal image for upgrading directly to IRAM/DRAM
# python ../bin/merge_ram_images.py --comment_format="c" -f "eeprom" -m "./build-output/metadata.txt" -c "Capella Firmware Image for Download to the EEPROM<br>  Version:      0.11.0.1948<br>  Build Date:  15 Feb 2022 at 23:46<br>  Description: Alpha firmware release for customer integration\\\n Version: 0.11.0.1948\\\n Build: 15 Feb 2022 at 23:46" -i ./build-output/iram.data -d ./build-output/dram.data -o ./build-output/cpl_firmware_debug_eeprom_0_11_0_1948.txt
# @echo ""
# @echo "Dumping the Intel Hex Image"
# @echo "==========================="
# # Finally generate the Intel Hex file
# python util/create_intel_hex.py -i "./build-output/cpl_firmware_debug_eeprom_0_11_0_1948.txt" -o "./build-output/cpl_firmware_debug_eeprom_0_11_0_1948.intel.hex"
make[1]: Leaving directory `/home/dutran/projects/hsc/capella/firmware/application'
bash-4.2$ ls
README.md  application_build_impl.sh    application_firmware_tag.sh  build-output  docs   feature.inc  host.ip   inc       merge_an_lt.sh      push_firmware.py  release.sh  util         whirl-gen
an_lt      application_build_impl_2.sh  application_klocwork.sh      build.inc     dv.py  fw_common    hydra.sh  libwhirl  merge_fw_common.sh  reg.py            src         version.inc
bash-4.2$ cd build-output/
```

```
python push_firmware.py
```
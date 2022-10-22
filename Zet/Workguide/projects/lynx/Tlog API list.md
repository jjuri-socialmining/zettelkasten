---
title: Tlog API list
created: 2022-Sep-14
tags:
  - 'tasks/todo'
project: TBD
date:
  - start: 2022-09-14
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Tasks list]]



```c
hsc_status_t hsc_mcu_log_version(hsc_mcu_t *mcu, uint32_t *api_ver, uint32_t *fw_ver);
uint32_t hsc_mcu_log_crc_get(hsc_mcu_t *mcu);
hsc_status_t hsc_mcu_log_flood(hsc_mcu_t *mcu, bool flood);

hsc_status_t hsc_mcu_log_rotation_enable(hsc_mcu_t *mcu, bool enabled);
hsc_status_t hsc_mcu_log_rotation_is_enabled(hsc_mcu_t *mcu, bool *enabled);

uint32_t hsc_mcu_log_nb_bytes_avail(hsc_mcu_t *mcu);
uint32_t hsc_mcu_log_filter_get(hsc_mcu_t *mcu);
hsc_status_t hsc_mcu_log_filter_set(hsc_mcu_t *mcu, uint32_t filter);
hsc_status_t hsc_mcu_log_pop(hsc_mcu_t *mcu, hsc_mcu_log_pop_opts_t opts, const hsc_mcu_log_callback_t *callback, void *ctx);

hsc_status_t hsc_mcu_log_ld_file_set(hsc_mcu_t *mcu, const char *ld_filepath);
const char *hsc_mcu_log_ld_file_get(hsc_mcu_t *mcu);

hsc_status_t hsc_mcu_log_render_entry(
        hsc_mcu_t *mcu, uint8_t *buff, uint16_t buff_size, const hsc_mcu_log_callback_t *callback, void *ctx);

hsc_status_t hsc_mcu_log_brief(hsc_mcu_t *mcu);

```



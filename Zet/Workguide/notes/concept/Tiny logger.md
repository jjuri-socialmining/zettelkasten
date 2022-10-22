---
title: Tiny logger
created: 2022-Jun-28
tags:
  - 'permanent/concept'
aliases:
  - tlog
---

[[Log dictionary]]

[[Producer index]]

[[Consumer index]]


```shell
@echo "Generating log dictionary."
@echo "=========================="
@echo "- First pass : generate checksum on .rodata, .log_entries and .log_texts sections"
@echo "- Second pass: embed the CRC into TLOG back-end"

make -f build.inc ${exe_name} USE_TLOG=true defines="${defines} -DTLOG_CRC=$$(${TLOG_LDICT} show crc "${exe_name}.tld")"
```

### Personal note
- [[Tlog GUI integrate]]
- [[RETCSW-229 - Add unittest for tlog]]
- [[2022-09-01 Final Tlog]]
- Path to set:
	- `C://Users//hcmswlab//Downloads//abcd_6_1_571//support//drivers//lynx_800//ucode//lynx_app_fw.tld`

[[Swig set and store ld file path]]
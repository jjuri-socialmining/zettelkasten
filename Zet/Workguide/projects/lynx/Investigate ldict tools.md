---
title: Investigate ldict tools
created: 2022-Aug-11
tags:
  - 'tasks/todo'
project: TBD
date:
  - start: 2022-08-11
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Tasks list]]

make file use this tool to generate ldict

`firmware\application\build.inc`

```
TLOG_LDICT=${TLOG_DIR}/pytlog/scripts/ldict

log_dict: ${exe_name}
	@echo ""
	@echo "Generating log dictionary."
	@echo "==========================" 
	@echo "- First pass : generate checksum on .rodata, .log_entries and .log_texts sections"
	@echo "- Second pass: embed the CRC into TLOG back-end"
	PYTHONPATH="" && /tools/cad/anaconda3/2019.03/Linux/2019.03/bin/python3 -m venv ${TLOG_DIR}/envs/linux-py3 && \
		PYTHONPATH=${TLOG_DIR}/pytlog source ${TLOG_DIR}/envs/linux-py3/bin/activate && \
		python -m pip install --upgrade pip --quiet && \
		python -m pip install -r ${TLOG_DIR}/pytlog/requirements.txt --quiet --no-cache-dir && \
		touch ${TLOG_DIR}/tlog/src/be/tlog_be.c && \
		make -f build.inc ${exe_name} USE_TLOG=true defines="${defines}" && \
		${TLOG_LDICT} extract --elf ${exe_name} \
						--image-version ${version_code} \
						--tlog-version ${TLOG_DIR}/tlog/inc/tlog_ver.h \
						--ld-file ${exe_name}.tld \
						--desc "Lynx Firmware Log Dictionary.\n${version_desc}" && \
		touch ${TLOG_DIR}/tlog/src/be/tlog_be.c && \
		make -f build.inc ${exe_name} USE_TLOG=true defines="${defines} -DTLOG_CRC=$$(${TLOG_LDICT} show crc "${exe_name}.tld")"

```







---
title: 2022-09-01 Final Tlog
created: 2022-Sep-01
tags:
  - 'permanent/common'
---


![[Pasted image 20220901105738.png]]

python -u make.py get_all --asics capellab ctcb lynx_400 --cplb_fw_version=CAPELLAB_NIGHTLY_2644 --cplb_api_version=CAPELLAB_NIGHTLY_2183 --ctcb_fw_version=CTCB_NIGHTLY_537 --ctcb_api_version=CTCB_NIGHTLY_1964  --lynx_400_fw_version=LYNX_NIGHTLY_720 --lynx_400_api_version=LYNX_NIGHTLY_1231

python -u make.py get_all --asics capellab ctcb lynx_400 --cplb_fw_version=CAPELLAB_NIGHTLY_2644 --cplb_api_version=CAPELLAB_NIGHTLY_2183 --ctcb_fw_version=CTCB_NIGHTLY_537 --ctcb_api_version=CTCB_NIGHTLY_1964  --lynx_400_fw_version=LYNX_NIGHTLY_738 --lynx_400_api_version=LYNX_NIGHTLY_1231

```
python -u -m pytest -s tests/universal/test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal --bench lynx_400_bench1
```


[[cpl tlog render.log]]
[[lynx ctc mcu tlog render.log]]
---
title: Regression test sjc-007892
created: 2022-Aug-09
tags:
  - 'permanent/common'
---
up:: [[HSC Regression test]]

Link: https://odsp-sqa-jenkins.marvell.com/job/lynx.regression/job/nightly/job/lynx_SJCLab-007892/

`--bench lynx_to_por_bench1`

```
python -u -m pytest -s tests/universal/test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal -k 'HOST_PRBS_26p5625G_PAM_SLC1_PRBS31' --bench lynx_to_por_bench1 --download_fw always --type_of_regression regular
```


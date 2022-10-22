---
title: Tlog stress test
created: 2022-Oct-04
tags:
  - 'tasks/done'
project: Lynx
date:
  - start: 2022-10-04
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Tasks list]]

repo: `http://las-gitlab/hsc/regression.git`
branch: `users/dutran/tlog_polling`

Command run on regression test
```shell
python -u -m pytest -s tests/universal/test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal -k 'DUPLEX_RETIMER' --bench lynx_400_bench1 --download_fw on_failure --type_of_regression regular
```
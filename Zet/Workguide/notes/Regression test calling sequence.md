---
title: Regression test calling sequence
created: 2022-Aug-05
tags:
  - 'permanent/common'
---

prbs fixture

|     |                        |                     |                              |
| --- | ---------------------- | ------------------- | ---------------------------- |
| 1   | universal_prbs_fixture | capella_fixtures.py |                              |
| 2   | configs_load           | common_fixtures.py  | then config CTCB and LYNX400 |
| 3   | configure_device       |                     |                              |
|     |                        |                     |                              |

`tests/universal/test_universal_prbs.py::TestPrbsUniversal::test_prbs_universal`

```mermaid
flowchart
	anlt_config_fixture --> configs_load
	anlt_config_fixture --> prbs_config
    anlt_config_fixture --> startup

	anlt_class_fixture --> configs_load
	anlt_class_fixture --> prbs_config
    anlt_class_fixture --> startup

    universal_prbs_fixture --> configs_load
    universal_prbs_fixture --> prbs_config
    universal_prbs_fixture --> startup
    configs_load -- Call to n devices --> configure_device
```

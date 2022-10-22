---
title: Swign Autodoc feature
created: 2022-Oct-19
tags:
  - 'permanent/concept'
aliases:
  -
publish: False
---

`bin/asic_types.i`

```
/* Enable autodoc gen for python function */
%feature("autodoc", "1");
```

result in `odsp_api.py`:
```python
def odsp_rx_rules_autoctle_enable(*args, **kwargs):
  """odsp_rx_rules_autoctle_enable(odsp_rx_rules_s rules, bool enable) -> odsp_status_t"""
  return _odsp_api.odsp_rx_rules_autoctle_enable(*args, **kwargs)
```
---
title: swig feature autodoc
created: 2022-Jun-10
tags:
  - 'permanent/concept'
aliases:
  -
---
up:: [[swig]]

Document in:
https://www.swig.org/Doc3.0/Python.html#Python_nn67

Syntax
```swig
%feature("autodoc", "_level_")
```

There are 4 level of autodoc, the bigger level the more detail of autodoc comment. Level 1 is enough
```swig
%feature("autodoc", "1");
```

The output:
```python
def hsc_rx_qc_rules_enable(rules, en):
    r"""hsc_rx_qc_rules_enable(hsc_rx_qc_rules_s rules, bool en) -> hsc_status_t"""
    return _hsc_api.hsc_rx_qc_rules_enable(rules, en)

def hsc_rx_qc_rules_is_enabled(rules):
    r"""hsc_rx_qc_rules_is_enabled(hsc_rx_qc_rules_s rules) -> bool"""
    return _hsc_api.hsc_rx_qc_rules_is_enabled(rules)

def hsc_rx_qc_rules_data_mode_enable(rules, en):
    r"""hsc_rx_qc_rules_data_mode_enable(hsc_rx_qc_rules_s rules, bool en) -> hsc_status_t"""
    return _hsc_api.hsc_rx_qc_rules_data_mode_enable(rules, en)

def hsc_rx_qc_rules_data_mode_is_enabled(rules):
    r"""hsc_rx_qc_rules_data_mode_is_enabled(hsc_rx_qc_rules_s rules) -> bool"""
    return _hsc_api.hsc_rx_qc_rules_data_mode_is_enabled(rules)
```







## Xbar python Sample

```python
api.hsc_bundle_rules_query(bundle, rules)
xbar_rules = api.hsc_xbar_rules(rules)
api.hsc_xbar_rules_print(xbar_rules)

print(api.hsc_xbar_rules_multi_chns_dst_get(xbar_rules, 0, api.HSC_INTF_LINE))
print(api.hsc_xbar_rules_multi_chns_src_get(xbar_rules, 0, api.HSC_INTF_LINE))

```
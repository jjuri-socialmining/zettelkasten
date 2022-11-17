```python

# Import register and API
from lynx_400.python import lynx_400_registers as creg
from lynx_400.python import hsc_api as api

# Get number of die on this device over API
dev = api.hsc_dev_t()
api.hsc_dev(dev, 0)
num_dies = api.hsc_dev_num_dies(dev)

status = api.HSC_OK
chns_mask = 0xf
chns_num = 4
prbs_pat = api.HSC_PRBS_PAT_PRBS31
status = api.HSC_OK

def prbs_check(cur_dev, chn_id, point):
    chk_rule = api.hsc_prbs_rules_t()
    api.hsc_dev_prbs_chk_rules(cur_dev, chk_rule)
    api.hsc_prbs_rules_pattern_mode_set(chk_rule, api.HSC_PRBS_PATTERN_PRBS)
    api.hsc_prbs_rules_mode_set(chk_rule, api.HSC_PRBS_MODE_MSB_LSB)
    api.hsc_prbs_rules_pattern_set(chk_rule, prbs_pat)
    api.hsc_prbs_rules_pattern_lsb_set(chk_rule, prbs_pat)
    api.hsc_prbs_rules_enable(chk_rule, True)
    api.hsc_prbs_rules_lsb_enable(chk_rule, True)

    prbs = api.hsc_prbs_t()
    api.hsc_dev_prbs(cur_dev, chn_id, point, prbs)
    ret = api.hsc_prbs_chk_rules_apply(prbs, chk_rule)
    print ("hsc_prbs_chk_rules_apply ret = %u" % ret)
    del chk_rule


def prbs_status_get(cur_dev, chn_id, intf):

    prbs_status = api.hsc_prbs_chk_status_t()
    prbs = api.hsc_prbs_t()
    api.hsc_dev_prbs(cur_dev, chn_id, intf, prbs)

    if api.hsc_prbs_chk_status_query(prbs, prbs_status) == api.HSC_OK:
        print(f"Ber msb: {prbs_status.ber}, Ber lsb: {prbs_status.ber_lsb}")


chn_id = 0

prbs_check(dev, chn_id, api.HSC_INTF_LRX)
prbs_status_get(dev, chn_id, api.HSC_INTF_LRX)

```
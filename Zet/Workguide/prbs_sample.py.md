```python

# Import register and API
from spica5n.python import spica5_registers as creg
from spica5n.python.universal import odsp_api as api

dev = api.odsp_dev_t()
api.odsp_dev(dev, 0)
num_dies = api.odsp_dev_num_dies(dev)


status = api.ODSP_OK
chns_mask = 0xf
chns_num = 4
prbs_pat = api.ODSP_PRBS_PAT_PRBS31
status = api.ODSP_OK

# /* Assign a channel to represent the interface. When
#  * dealing with interfaces this is always a physical
#  * channel from the perspective of the host receiver. */
hrx_channel = 0

# status |= api.odsp_bundle_query_enable(True)
# status |= api.odsp_bundle_rules_query(bundle, rules)
# print ("odsp_bundle_rules_query", status == api.ODSP_OK)

def prbs_gen(cur_dev, chn_list, point):
    gen_rule = api.odsp_prbs_rules_t()
    api.odsp_dev_prbs_gen_rules(cur_dev, gen_rule)
    api.odsp_prbs_rules_pattern_mode_set(gen_rule, api.ODSP_PRBS_PATTERN_PRBS)
    api.odsp_prbs_rules_mode_set(gen_rule, api.ODSP_PRBS_MODE_MSB_LSB)
    api.odsp_prbs_rules_pattern_set(gen_rule, prbs_pat)
    api.odsp_prbs_rules_pattern_lsb_set(gen_rule, prbs_pat)
    api.odsp_prbs_rules_enable(gen_rule, True)
    api.odsp_prbs_rules_lsb_enable(gen_rule, True)
    prbs = api.odsp_prbs_t()
    for chn in chn_list:
        api.odsp_dev_prbs(cur_dev, chn, point, prbs)
        ret = api.odsp_prbs_gen_rules_apply(prbs, gen_rule)
        print ("odsp_prbs_gen_rules_apply ret = %u" % ret)
        print ("pattern = %u" % api.odsp_prbs_rules_pattern_get(gen_rule))
    del gen_rule


def prbs_check(cur_dev, chn_list, point):
    chk_rule = api.odsp_prbs_rules_t()
    api.odsp_dev_prbs_chk_rules(cur_dev, chk_rule)
    api.odsp_prbs_rules_pattern_mode_set(chk_rule, api.ODSP_PRBS_PATTERN_PRBS)
    api.odsp_prbs_rules_mode_set(chk_rule, api.ODSP_PRBS_MODE_MSB_LSB)
    api.odsp_prbs_rules_pattern_set(chk_rule, prbs_pat)
    api.odsp_prbs_rules_pattern_lsb_set(chk_rule, prbs_pat)
    api.odsp_prbs_rules_enable(chk_rule, True)
    api.odsp_prbs_rules_lsb_enable(chk_rule, True)
    api.odsp_prbs_rules_chk_autolock_enable(chk_rule, True)
    for chn in chn_list:
        prbs = api.odsp_prbs_t()
        api.odsp_dev_prbs(cur_dev, chn, point, prbs)
        ret = api.odsp_prbs_chk_rules_apply(prbs, chk_rule)
        print ("odsp_prbs_chk_rules_apply ret = %u" % ret)
        ret = api.odsp_prbs_chk_rules_query(prbs, chk_rule)
        print ("pattern msb = %u" % api.odsp_prbs_rules_pattern_get(chk_rule))
        print ("pattern lsb = %u" % api.odsp_prbs_rules_pattern_lsb_get(chk_rule))
        print ("autolock = %u" % api.odsp_prbs_rules_chk_autolock_is_enabled(chk_rule))
        print ("mode = %u" % api.odsp_prbs_rules_mode_get(chk_rules)
        
    del chk_rule


chns_list = [chn for chn in range(chns_num)]
# LINE
# prbs_gen(dev, chns_list, api.ODSP_INTF_LTX)
# HOST
# prbs_gen(dev, chns_list, api.ODSP_INTF_HTX)

prbs_check(dev, chns_list, api.ODSP_INTF_LRX)
prbs_check(dev, chns_list, api.ODSP_INTF_HRX)


```
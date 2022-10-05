---
aliases: 
  - PAN
---
# Next Page

PAN: Prorietary Autoneg Next page

[[PAN là prorietary Autoneg Next page]]
Configure AN mode = `HSC_AN_MODE_PAN_NP`

```c
hsc_an_rules_mode_set(an_rules, HSC_AN_MODE_PAN_NP);
```

```c
/**
 * AN modes
 */
typedef enum
{
    /** IEEE mode */
    CPL_AN_MODE_IEEE = 0,

    /** 50G Consortium Mode */
    CPL_AN_MODE_50G_CONSORTIUM_NP = 1,

    /** Broadcom Next Page Mode */
    CPL_AN_MODE_BROADCOM_NP = 2,

    /** Proprietary AN NEXT PAGE (PAN) Mode */
    CPL_AN_MODE_PAN_NP = 4,
}
e_cpl_anlt_mode;

/**
 * This structure is used to manage PAN (Proprietary AN Next Page) Mode
 *
 * @since 0.15
 */
typedef struct
{
   /** 48 bit raw oui page */
   uint64_t oui_page; 

   /** 48 bit oui mask     */
   uint64_t oui_mask; 

   /** 48 bit ext page     */
   uint64_t ext_page; 

   /** 48 bit ext mask     */
   uint64_t ext_mask; 

   /** 48 bit expectation page */
   uint64_t exp_page; 

   /** Baud Rate -- for NRZ it is same as Bit rate & for PAM4 it is half the bit rate */
   uint32_t baud_rate;

   /** Channels in bundle - user pre-configure data path */
   uint8_t  bundling;

   /** PAM4 / NRZ */
   uint8_t  modulation_mode;

}cpl_anlt_pan_aware_t;

typedef struct {
    ...
    /** PAN capabilities */
    cpl_anlt_pan_aware_t pan;
    ...
}cpl_anlt_an_t;
```

## CPL regression test

in file `regression_common\base_classes\anlt_intf.py`

```python
# If PAN_NP is set in the mask, configure every PAN_NP field
if rules.an.mode & self.device.tr.mode("PAN_NP"):
    print("Configuring PAN rules.")
    rules.an.pan.oui_page = 0x000000789012  # 24 bits of OUI
    rules.an.pan.oui_mask = 0x000000FFFFFF
    rules.an.pan.ext_page = 0x00000011012F
    rules.an.pan.ext_mask = 0x000000FF000F
    rules.an.pan.exp_page = 0x00000011000F
    rules.an.pan.bundling = 1
    rules.an.pan.modulation_mode = int(dict_rules["signalling"] == "PAM")  # 1 for PAM, 0 for NRZ
```

In file `capella\tests\anlt\test_anlt.py`
```python
class TestAnltPanModeSingle(TestAnltSingle):
    rules = {
        "an": {
            "enable": True,
            "probe": False,
            "mode": "PAN_NP",
        },
        "lt": {"enable": True},
        "use_idle_gen": False,
    }
    # PAN_NP cannot run consortium
    invalid_modes = {"25gkr_con", "25gcr_con", "50gkr2", "50gcr2"}
    combined_params = AnltParamUtils.anlt_combinations_single_channel(rules=rules, ignore_modes=invalid_modes)


class TestAnltPanModeMultiple(TestAnltSingle):
    rules = {
        "an": {
            "enable": True,
            "probe": False,
            "mode": "PAN_NP",
        },
        "lt": {"enable": True},
        "use_idle_gen": False,
    }
    invalid_modes = {"25gkr_con", "25gcr_con", "50gkr2", "50gcr2"}
    combined_params = AnltParamUtils.anlt_combinations_multiple_channel(rules=rules, ignore_modes=invalid_modes)
```

## [[Design hsc PAN]]
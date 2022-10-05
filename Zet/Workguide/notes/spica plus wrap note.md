# Spica Plus wrap note

Jira Task list
- https://essjira.marvell.com/browse/SPICSW-27

[[spica plus example prbs]]

### init chip before configure 

| spica api                       | hsc api               |
| ------------------------------- | --------------------- |
| `spica_bundle_cfg`              | Set rules to database |
| `spica_init`                    | `hsc_dev_init`        |
|                                 | `hsc_bundle_init`     |
| `spica_enter_operational_state` | `hsc_bundle_start`    |






```c
/**
 * @h2 ASIC Package and Channel Utilities
 * =======================================================
 *
 * @brief
 * The maximum number of dies inside the ASIC package. When only
 * working on a single die package this can be re-defined to 1 to
 * conserve memory utilization.
 */
#define SPICA_MAX_DIES_IN_PACKAGE 2

/** the maximum number of channels per die */
#define SPICA_NUM_OF_ORX_CHANNELS 4

#define SPICA_NUM_OF_OTX_CHANNELS 4

#define SPICA_NUM_OF_MRX_CHANNELS 4

#define SPICA_NUM_OF_MTX_CHANNELS 4

#define SPICA_NUM_OF_SRX_CHANNELS 8

#define SPICA_NUM_OF_STX_CHANNELS 8

/** The maximum number of line receivers in the ASIC package */
#define SPICA_MAX_ORX_CHANNELS (SPICA_NUM_OF_ORX_CHANNELS * SPICA_MAX_DIES_IN_PACKAGE)

/** The maximum number of line transmitters in the ASIC package */
#define SPICA_MAX_OTX_CHANNELS (SPICA_NUM_OF_OTX_CHANNELS * SPICA_MAX_DIES_IN_PACKAGE)

/** The maximum number of host PMR receivers in the ASIC package */
#define SPICA_MAX_MRX_CHANNELS (SPICA_NUM_OF_MRX_CHANNELS * SPICA_MAX_DIES_IN_PACKAGE)

/** The maximum number of host PMR transmitters in the ASIC package */
#define SPICA_MAX_MTX_CHANNELS (SPICA_NUM_OF_MTX_CHANNELS * SPICA_MAX_DIES_IN_PACKAGE)

/** The maximum number of host PSR receivers in the ASIC package */
#define SPICA_MAX_SRX_CHANNELS (SPICA_NUM_OF_SRX_CHANNELS * 1) // PG4 is only ever single die

/** The maximum number of host PSR transmitters in the ASIC package */
#define SPICA_MAX_STX_CHANNELS (SPICA_NUM_OF_STX_CHANNELS * 1) // PG4 is only ever single die

/** Maximum number of bundles */
#define SPICA_MAX_BUNDLES       8

#if defined(INPHI_HAS_SPICA_PLUS) && (INPHI_HAS_SPICA_PLUS==1)
    spica_orx_rules_t orx[SPICA_MAX_ORX_CHANNELS+1];
#else
    spica_ant_rx_rules_t orx[SPICA_MAX_ORX_CHANNELS+1];
#endif // defined(INPHI_HAS_SPICA_PLUS) && (INPHI_HAS_SPICA_PLUS==1)

    /** MRX Host receive rules */
    spica_ant_rx_rules_t mrx[SPICA_MAX_MRX_CHANNELS+1];

    /** SRX Host receive rules */
    spica_sun_rx_rules_t srx[SPICA_MAX_SRX_CHANNELS+1];

    /** OTX Line transmit rules */
    spica_tx_rules_t otx[SPICA_MAX_OTX_CHANNELS+1];

    /** MTX Host transmit rules */
    spica_tx_rules_t mtx[SPICA_MAX_MTX_CHANNELS+1];

    /** STX Host transmit rules */
    spica_tx_rules_t stx[SPICA_MAX_STX_CHANNELS+1];
```

![](2021-12-16-14-25-44.png)

```c
    /** The POR line side interface */
    SPICA_INTF_POR  = SPICA_INTF_ORX | SPICA_INTF_OTX,
    /** The PMR host side interface */
    SPICA_INTF_PMR  = SPICA_INTF_MRX | SPICA_INTF_MTX,
    /** The PSR host side interface */
    SPICA_INTF_PSR  = SPICA_INTF_SRX | SPICA_INTF_STX,
```
```
Link status in NVLINK_CLX
| INTF   |      1    |      2    |      3    |      4    |      5    |      6    |      7    |      8    |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| MTX    |     0.078 |     0.078 |     0.079 |     0.080 |     0.080 |     0.080 |     0.080 |     0.081 |
| ORX    |     0.081 |     0.081 |     0.081 |     0.081 |     0.082 |     0.082 |     0.082 |     0.082 |
| OTX    |     0.083 |     0.083 |     0.083 |     0.083 |     0.083 |     0.084 |     0.084 |     0.084 |
| MRX    |     0.084 |     0.084 |     0.085 |     0.085 |     0.085 |     0.085 |     0.086 |     0.086 |

Link status in NVLINK_CLX
| INTF   |      1    |      2    |      3    |      4    |      5    |      6    |      7    |      8    |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| MTX    |     0.078 |     0.078 |     0.079 |     0.080 |     0.080 |     0.080 |     0.080 |     0.081 |
| ORX    |     0.081 |     0.081 |     0.081 |     0.081 |     0.082 |     0.082 |     0.082 |     0.082 |
| OTX    |     0.083 |     0.083 |     0.083 |     0.083 |     0.083 |     0.084 |     0.084 |     0.084 |
| MRX    |     0.084 |     0.084 |     0.085 |     0.085 |     0.085 |     0.085 |     0.086 |     0.086 |
```

```
e muon run python script tren cygwin
repo: git@las-gitlab:hsc/lab.git
branch : users/vnguyen/spicap
nvinh@VN-LT3726 /cygdrive/c/Users/nvinh/develop/hsc/lab/users/vnguyen
$ python test_mcu.py
New
10:39
update target.py cho device test + api.py cho python folder import

```

```
gitlab repo: http://las-gitlab/hsc/spicap
api gitlab branch: http://las-gitlab/hsc/capi/-/tree/spica5_capi 
api jenkins jobs: http://dc5lp-vlas-sw-01/jenkins/view/Spica5/job/spicap
release folder: http://dc5lp-vlas-sw-01/projects/sw/spicap
```

You can use 5005 or 5001 in the evenings. Please make sure you reserve the bench before using it:

http://sw.inphi-corp.local/jenkins/view/Spica+/lockable-resources/

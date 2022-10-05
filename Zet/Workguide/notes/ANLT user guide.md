@h1 [[Autoneg Link training, Configuring ANLT Modes]]

[[ANLT]]

@h2 Overview
The following section describes the process of configuring the device
to support Ethernet Auto-Negotiation with Training. AN/LT is supported
only on the serial side of the IP core.

@vl
- AN              | Autonegotiation
- Link Leader     | One channel in the session is designated to carry out
                    autonegotiation. By convention the RX in the RX/TX pair
                    is the link leader. It performs auto negotiation with the
                    link partner and guides the link followers through the
                    link training process to offload the host supervisor.
- HCD             | The highest common denominator rate negotiated during the
                    probe phase.
- Host Supervisor | The end user software which initiates the auto-negotiation
                    process.
- LT              | Link Training
- Link Follower   | In a multiple channel bundle auto-negotiation happens on
                    only on the link leader. The remaining channels only
                    perform Link Training and are designated as Link Followers
                    as they are guided by the Link leader through the link training
                    process.
- PCS             | Physical Coding Sublayer - PCS traffic must be sent from the
                    Host Supervisor to ensure the link with the remote partner
                    stays active to prevent any re-negotiation.


@h2 AN/LT Requirements
- The external crossbar should be configured prior to starting the
  AN/LT sequence.
- The end user must maintain/store the AN/LT bundle structure hsc_bundle_rules_t
  definining the AN/LT session in external memory. The hsc_bundle_rules_t structure
  can be queried from the hardware but the hsc_bundle_rules_t structure cannot
  be queried from the hardware.
- The end user must generate valid PCS traffic toward the Capella Core/Parallel interface
  during AN/LT at the rate required by link training protocol.
- The probe phase is optional and can be skipped. It end user can cycle
  through advertized rates instead.
- If link training fails the device will not attempt to re-try the training
  sequence. The link leader will report error back to the host supervisor and
  it is responsible for re-trying the operation.

@h2 The AN/LT Bundle
The API defines the concept of a bundle to manage an AN/LT session. The RX and TX
of the Link Leader and the Link Followers can be spread across mutiple IP blocks so
they are grouped together into a bundle to simplify management of the AN/LT
session. This tells the API where to look in order to configure individual
channels or fetch status.

The bundle consists of:
- The Link Leader
- Multiple Link Followers

The RX is always designated as the control plane for both the Link Leader
and the Link Followers.

The AN/LT bundle is defined by the hsc_bundle_rules_t structure. 

@h2 Coding guide
The link leader and the link followers is controlled by bundle rules. Each leader/followers
is defined by hsc_anlt_chn_t structure. This hsc_anlt_chn_t structure combine the
tx/rx channel id of device.

@c
/* Example bellow define the bundle with 3 channels 0,1.
 * the tx/rx id of leader are 0.
 * all channels of bundle are set as the link followers.
 * The link followers order or the tx/rx id can modify by default
 * `hsc_bundle_rules_link_folwrs_set(bundle_rules, intf, folwrs)` or
 * `hsc_bundle_rules_link_folwr_by_idx_set(bundle_rules, intf, idx, folwr)`
 */
hsc_bundle_rules_chns_mask_set(bundle_rules, HSC_INTF_HOST, HSC_BIT1_0);
hsc_bundle_rules_chns_mask_set(bundle_rules, HSC_INTF_LINE, HSC_BIT1_0);

hsc_anlt_chn_t anlt_chn;
anlt_chn.tx_chn = 0;
anlt_chn.rx_chn = 0;
hsc_bundle_rules_link_leader_set(bundle_rules, HSC_INTF_LINE, &anlt_chn);
hsc_bundle_rules_link_folwr_by_idx_set(bundle_rules, HSC_INTF_LINE, 0, &anlt_chn)

anlt_chn.tx_chn = 1;
anlt_chn.rx_chn = 1;
hsc_bundle_rules_link_folwr_by_idx_set(bundle_rules, HSC_INTF_LINE, 1, &anlt_chn)

AN rules and LT rules are sub-rule of bundle rules with given interface. To get the 
reference to those sub-rules

@c
/* Assume the bundle rules is a valid reference hsc_bundle_rules_t *bundle_rules
 * example bellow is to get the reference to AN/LT of line interface
 * HSC_INTF_LINE
 */
hsc_an_rules_t *an_rules = hsc_an_rules(bundle_rules, HSC_INTF_LINE);
hsc_lt_rules_t *lt_rules = hsc_an_rules(bundle_rules, HSC_INTF_LINE);
hsc_an_rules_enable(an_rules, true);
hsc_lt_rules_enable(lt_rules, true);

To modify the feature of AN/LT rules, we use the methods name 
`hsc_an_rules_<feature>_set/enable`
`hsc_an_rules_<feature>_get/is_enabled`

@c
hsc_an_cap_t cap;
cap.advertise = true;
hsc_an_rules_cap_ad_set(an_rules, HSC_AN_ABILITY_25GBASE_KR, &cap);
hsc_an_rules_link_time_budget_set(an_rules, 500);

hsc_lt_rules_fir_walk_enable(lt_rules, true);
hsc_lt_rules_target_snr_set(lt_rules, 20000);


@h2 Examples:
@h3 ANLT

@c
hsc_status_t status = HSC_OK;
uint32_t bundle_id = 0;

hsc_dev_t dev;
hsc_dev(&dev, 0 /* asic_id */);

/* Default the bundle rules based on the desired application */
hsc_bundle_rules_t rules;
if (hsc_dev_bundle_rules(&dev, HSC_OPER_MODE_DUPLEX_RETIMER, &rules) == NULL)
{
    HSC_CRIT("Failed construct the bundle rule\n");
    return HSC_ERROR;
}

/* Assign channels/link followers to represent the bundle */
hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_HOST, HSC_BIT3_0);
hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_LINE, HSC_BIT3_0);

hsc_bundle_rules_baud_rate_set(&rules, HSC_BAUD_RATE_25p78125G);

uint32_t intfs = HSC_INTF_HOST | HSC_INTF_LINE;
hsc_bundle_rules_signalling_set(&rules, intfs, HSC_SIGNAL_MODE_NRZ);

/* AN and LT are sub-rules inside bundle rules, get the reference and modify
    * AN/LT configurations via AN rules or lt rules */
hsc_an_rules_t *an_rules = hsc_an_rules(&rules, anlt_intf);
hsc_lt_rules_t *lt_rules = hsc_lt_rules(&rules, anlt_intf);

hsc_an_rules_enable(an_rules, true);
hsc_lt_rules_enable(lt_rules, anlt_mode == AN_PROBE ? false : true);

hsc_anlt_chn_t anlt_chn;
anlt_chn.tx_chn = 0;
anlt_chn.rx_chn = 0;
hsc_bundle_rules_link_leader_set(&rules, anlt_intf, &anlt_chn);

/* Select capabilities to advertise to the remote link partner */
hsc_an_cap_t cap;
cap.advertise = true;
hsc_an_rules_cap_ad_set(an_rules, HSC_AN_ABILITY_100GBASE_KR4, &cap);

/* Initialize the bundle and tear down any resources that may
    * already be allocated. We usually use the min id of the host channel belong to
    * the bundle as bundle id */
hsc_bundle_t bundle;
hsc_dev_bundle(&dev, bundle_id, &bundle);
status |= hsc_bundle_init(&bundle, &rules);

/* Apply bundle rules to ASIC to bring the bundle up */
status |= hsc_bundle_start(&bundle, &rules);

@h3 Autoneg probe

@c
hsc_status_t status = HSC_OK;
uint32_t bundle_id = 0;
uint32_t chn_id = 0;
uint32_t chn_mask = HSC_BIT0 << chn_id;

/* Construct Device */
hsc_dev_t dev;
hsc_dev(&dev, 0 /* asic_id */);

/* Default the channel rules based on the desired application */
hsc_bundle_rules_t rules;
if (hsc_dev_bundle_rules(&dev, HSC_OPER_MODE_DUPLEX_RETIMER, &rules) == NULL)
{
    HSC_CRIT("Failed construct the bundle rule\n");
    return HSC_ERROR;
}

/* Setup the physical channel binding that maps channels
 * to this bundle. The 'mask' is a bitmask with an enabled bit for each
 * channel to bind/associate with the bundle/bundle. 
 */
hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_HOST, chn_mask);
hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_LINE, chn_mask);

/* Specify the data rate for a single channel from the perspective
 * of the host receiver. The line rate is implied based on the
 * selected FEC mode/protocol + signaling mode. In this case
 * each host port is operating at 26.5625Gbps in NRZ mode. */
hsc_bundle_rules_baud_rate_set(&rules, HSC_BAUD_RATE_25p78125G);

uint32_t intfs = HSC_INTF_HOST | HSC_INTF_LINE;
hsc_bundle_rules_signalling_set(&rules, intfs, HSC_SIGNAL_MODE_NRZ);

/* AN and LT are sub-rules inside bundle rules, get the reference and modify
 * AN/LT configurations via AN rules or lt rules */
hsc_an_rules_t *an_rules = hsc_an_rules(&rules, anlt_intf);
hsc_lt_rules_t *lt_rules = hsc_lt_rules(&rules, anlt_intf);

hsc_an_rules_enable(an_rules, true);
hsc_lt_rules_enable(lt_rules, false);

/* Set the link leader to processing correspond to the remote link partner
 * Example the leader id of tx/rx id is 0. */
hsc_anlt_chn_t anlt_chn;
anlt_chn.tx_chn = chn_id;
anlt_chn.rx_chn = chn_id;
hsc_bundle_rules_link_leader_set(&rules, anlt_intf, &anlt_chn);

/* Select capabilities to advertise to the remote link partner */
hsc_an_cap_t cap;
cap.advertise = true;
hsc_an_rules_cap_ad_set(an_rules, HSC_AN_ABILITY_25GBASE_KR, &cap);

/* Initialize the bundle and tear down any resources that may
 * already be allocated. We usually use the min id of the host channel belong to
 * the bundle as bundle id */
hsc_bundle_t bundle;
hsc_dev_bundle(&dev, bundle_id, &bundle);
status |= hsc_bundle_init(&bundle, &rules);

/* Apply bundle rules to ASIC to bring the bundle up */
status |= hsc_bundle_start(&bundle, &rules);

HSC_NOTE("Bundle rules\n");
hsc_bundle_rules_show(&bundle);

HSC_NOTE("Bundle anlt status\n");
status |= anlt_status_show(&bundle, anlt_intf, 10);

@h3 Link training only

@c
hsc_status_t status = HSC_OK;

/* Construct Device */
hsc_dev_t dev;
hsc_dev(&dev, 0 /* asic_id */);

/* Default the channel rules based on the desired application */
hsc_bundle_rules_t rules;
hsc_dev_bundle_rules(&dev, HSC_OPER_MODE_REVERSE_GEARBOX, &rules);

/* Setup the physical channel binding that maps channels
 * to this bundle. The 'mask' is a bitmask with an enable bit for each
 * channel to bind/associate with the bundle/bundle.
 *
 * In this case we're using channels 0-1 on the host side gearboxed to 
 * channels 0-3 on the line side */
hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_HOST, HSC_BIT1_0);
hsc_bundle_rules_chns_mask_set(&rules, HSC_INTF_LINE, HSC_BIT3_0);

/* Specify the data rate for a single channel from the perspective
 * of the host receiver. The line rate is implied based on the
 * selected FEC mode/protocol. In this case each host port is
 * operating at 53.125Gbps (26.5625Gbaud over PAM) */
hsc_bundle_rules_baud_rate_set(&rules, HSC_BAUD_RATE_26p5625G);

/* Setup the signaling for NRZ on the line and PAM on the host */
hsc_bundle_rules_signalling_set(&rules, HSC_INTF_HOST, HSC_SIGNAL_MODE_PAM);
hsc_bundle_rules_signalling_set(&rules, HSC_INTF_LINE, HSC_SIGNAL_MODE_NRZ);

/* Using bundle 0, initialize it to tear down any resources that may already be
 * allocated. */
hsc_bundle_t bundle;
uint32_t bundle_id = 0;
hsc_dev_bundle(&dev, bundle_id, &bundle);
status |= hsc_bundle_init(&bundle, &rules);

/* Bringup the bundle up */
hsc_bundle_start(&bundle, &rules);

/* Wait for up to 1s for the 100G bundle to be ready */
hsc_bundle_link_ready_wait(&bundle, 1000 * 1000);


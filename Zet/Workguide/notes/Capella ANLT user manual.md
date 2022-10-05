[[ANLT]]

@h1 [[ConfiguringKr, Configuring Auto-negotiation and Link Training]]
The following section describes the process of configuring the device
to support Ethernet Auto-Negotiation with Training. AN/LT is supported
only on the serial side of the IP core.

@vl
- AN              | Autonegotiation
- AN Leader       | One channel in the session is designated to carry out
                    autonegotiation. By convention the RX in the RX/TX pair
                    is the AN leader. It performs auto negotiation with the
                    link partner and guides the LT followers through the
                    link training process to offload the host supervisor.
- HCD             | The highest common denominator rate negotiated during the
                    probe phase.
- Host Supervisor | The end user software which initiates the auto-negotiation
                    process.
- LT              | Link Training
- LT Follower     | In a multiple channel bundle auto-negotiotion happens on
                    only on the the AN leader. The remaining channels only
                    perform Link Training and are designated as LT Followers
                    as they are guided by the AN leader through the link training
                    process.
- PCS             | Physical Coding Sublayer - PCS traffic must be sent from the
                    Host Supervisor to ensure the link with the remote partner
                    stays active to prevent any re-negotiation.

@h2 AN/LT Requirements
- The external crossbar should be configured prior to starting the
  AN/LT sequence.
- The end user must maintain/store the AN/LT bundle structure cpl_anlt_bundle_t
  definining the AN/LT session in external memory. The cpl_anlt_rules_t structure
  can be queried from the hardware but the cpl_anlt_bundle_t structure cannot
  be queried from the hardware.
- The end user must generate valid PCS traffic toward the Capella Core/Parallel interface
  during AN/LT at the rate required by link training protocol.
- The probe phase is optional and can be skipped. It end user can cycle
  through advertized rates instead.
- If link training fails the device will not attempt to re-try the training
  sequence. The AN leader will report error back to the host supervisor and
  it is responsible for re-trying the operation.


@h2 The AN/LT Bundle
The API defines the concept of a bundle to manage an AN/LT session. The RX and TX
of the AN Leader and the LT Followers can be spread across mutiple IP blocks so
they are grouped together into a bundle to simplify management of the AN/LT
session. This tells the API where to look in order to configure individual
channels or fetch status.

The bundle consists of:
- The AN Leader
- Multiple LT Followers

The RX is always designated as the control plane for both the AN Leader
and the LT Followers.

The AN/LT bundle is defined by the cpl_anlt_bundle_t structure. The picture
below shows an example of a 4x25 bundle that is spread across two IP blocks
and an example of what the structure looks for this bundle.

@image: src="docs/images/anlt_team.png"

@text
In this case the AN/LT bundle structure would look like:

@c
cpl_anlt_bundle_t bundle = {

    // Setup the AN leader (RX is on die 0, TX is on die 1)
    .an_leader = {
        .rx_die = 0, .rx_channel = 0;
        .tx_die = 1, .tx_channel = 0;
    },

    // The are four LT followers.
    .num_followers = 4,

    // LT[0] - the first LT follower is always the same as the AN leader
    .lt_followers[0] = {
        .rx_die = 0, .rx_channel = 0,
        .tx_die = 1, .tx_channel = 0,
    },

    // LT[1]
    .lt_followers[1] = {
        .rx_die = 1, .rx_channel = 0,
        .tx_die = 0, .tx_channel = 0,
    },
    
    // LT[2]
    .lt_followers[2] = {
        .rx_die = 0, .rx_channel = 1,
        .tx_die = 1, .tx_channel = 1,
    },
    
    // LT[3]
    .lt_followers[3] = {
        .rx_die = 1, .rx_channel = 1,
        .tx_die = 0, .tx_channel = 1,
    },
};


@h2 How AN/LT Works
AN/LT is split into three phases:

@table
- Phase \# | Phase Name                    | Phase Description
- 1        | AN Probe (Optional)           | This is an optional discovery stage where only auto-negotiation occurs in
                                             order to determine the highest common denominator capabilities 
                                             between the local and remote link partners. In this phase training
                                             is disabled.
- 2        | Host Supervisor Configuration | After probing is complete the host supervisor re-configures
                                             the LT followers for the negotiated rate and immediately starts
                                             transmitting PCS idles or traffic.
- 3        | AN/LT                         | After probing and host configuration have completed the host
                                             supervisor restarts the AN/LT sequence at the targeted rate
                                             and waits for the AN leader to complete the full auto-negotiation
                                             and link training process. The AN leader reports AN_GOOD back
                                             to the host supervisor when complete.

@text
The diagram below summarizes how AN/LT works (The link partner is not show for simplicity):

@sequence: title="AN Phases"
- Type    | Source          | Sink            | Name                          | Description
-h Phase 1: AN Probe
- message | Host Supervisor | AN Leader       | Advertize 100GKR4 & 200GKR4   | The host supervisor triggers the probe phase
                                                                                by advertizing the list of rates it supports. In this
                                                                                example it supports 100G KR4 and 200G KR4.
- action  | AN Leader       |                 | Negotiate HCD                 | The AN leader negotiates with the link partner and
                                                                                agrees on the 200G KR4 rate.
- message | AN Leader       | Host Supervisor | Negotiated 200G KR4           | The AN leader reports the negotiated results back
                                                                                to the host supervisor.

-h Phase 2: Host Supervisor Configuration
- message | Host Supervisor | LT[n]           | init rx/tx for 50G PAM        | The host supervisor re-configures the link followers at the negotiated rate
- action  | Host Supervisor |                 | Send PCS                      | The host supervisor then starts transmitting PCS traffic to the
                                                                                AN leader and LT followers. This required to prevent the link partner
                                                                                from seeing a loss of link condition when it finishes link training
                                                                                which would cause a re-negotiation.
-h Phase 3: AN/LT
- message | Host Supervisor | AN Leader       | Re-advertize only 200G KR4    | The host supervisor tells the AN Leader to re-start the
                                                                                negotiation process at the target rate.
- action  | AN Leader       |                 | Renegotiate at target rate    | The AN leader re-negotiates with the link partner
- message | AN Leader       | LT[n]           | Start training at target rate | The AN leader tells each LT follower to start training
- message | LT[n]           | AN Leader       | Training complete             | The LT followers report back to the AN leader when they
                                                                                have completed training.
- message | AN Leader       | Host Supervisor | AN_GOOD                       | AN/LT is complete, AN leader reports AN_GOOD back to the host supervisor.


@h3 Phase 1: AN Probe (Optional)
The AN probe phase is an optional step first performed in order to negotiate
the highest common rate between both link partners. In this
phase training is disabled and it terminates after negotiation
has completed.

@tip
The probe phase is optional. It is possible to attempt phase 2+3 times
iteratively looking for a successful match instead of using the AN probe phase.

@text
The following diagram describes the sequence of events that happen during
the AN probe phase.

@sequence: title="AN Probe" caption="AN Probe"
- Type    | Source          | Sink           | Name                     | Description
-h AN Probe
- message | Host Supervisor | AN Leader.RX   | Initialize AN.RX         | The host supervisor sets up the rules for the PLL and RX of the AN leader
                                                                          for auto-negotiation. It sets up the PLL for the HCD rate.
- message | Host Supervisor | AN Leader.TX   | Initialize AN.TX         | The host supervisor sets up the rules for the TX of the AN leader TX
                                                                          for auto-negotiation. If the PLL is different than the RX it sets up the PLL
                                                                          for the HCD rate.
- message | Host Supervisor | AN Leader.RX   | AN_INIT_REQ              | The host supervisor asserts the CHANNEL_INIT_REQ[n].AN_INIT_REQ and waits
                                                                          for the f/w to assert the CHANNEL_INIT_ACK[n].AN_INIT_ACK indicating the
                                                                          AN sequence has initiated.
- message | AN Leader.RX    | Host Supervisor| AN_INIT_ACK              | The firmware asserts the CHANNEL_INIT_ACK[n].AN_INIT_ACK
- action  | AN Leader.RX    |                | Bringup RX               | The AN leader brings up PLL and RX in order to support auto-negotiation.
                                                                          The PLL is setup to operate at the HCD rate.
- action  | AN Leader.TX    |                | Bringup TX               | The PLL and TX are brought up in the TX of the AN Leader.
- message | AN Leader.TX    | AN Leader.RX   | TX Ready                 | The TX sends a message to the RX to indicate when it is in service.
- message | AN Leader.RX    | AN Leader.TX   | Send DME Page            | The RX sends command to the TX to transmit DME page
- message | AN Leader.TX    | Link Partner   | DME Page                 | The TX sends the DME page to the link partner
- message | Link Partner    | AN Leader.RX   | DME page                 | The Link partner sends the response back to the AN Leader RX
-b ... DME Page Exchange ...
- message | AN Leader.RX    | AN Leader.TX   | Send DME Page            | RX sends command to the TX to transmit DME page
- message | AN Leader.TX    | Link Partner   | DME Page                 | The TX sends the DME page to the link partner
- message | Link Partner    | AN Leader.RX   | DME page                 | The Link partner sends the response back to the AN Leader RX.
- action  | AN Leader.RX    |                | Store AN Results         | The AN leader stores the results of the auto-negotiation sequence.
- message | AN Leader.RX    | Host Supervisor| AN GOOD                  | The AN Leader reports the negotiated results back to the Host Supervisor
- note    | Host Supervisor |                | Phase 2: Configure PCS   | The host supervisor proceeds with re-configuring the lanes to generate
                                                                          PCS traffic at the negotiated rate.

@h3 Phase 2: Host Supervisor Configuration
In this phase the host supervisor re-configures all of the LT
followers to the highest common denominator rate negotiated
during the AN Probe phase. It also configures the upstream
PCS to start generating valid PCS traffic into the core
side of the Capella IP.

@sequence: title="Host Supervisor Configuration"
- Type    | Source          | Sink           | Name             | Description
-h Host Configuration
- message | Host Supervisor | LT[n].RX       | Initialize RX    | Initialize the RX of each LT Follower
                                                                  for the negotiated rate from the probe phase.
- message | Host Supervisor | LT[n].TX       | Initialize TX    | Initialize the TX of each LT Follower
                                                                  for the negotiated rate from the probe phase.
- action  | Host Supervisor |                | Send PCS Traffic | The host supervisor starts sending valid PCS
                                                                  traffic towards the Capella IP Core interface for
                                                                  all RX/TX pairs participating in the AN/LT session.
- note    | Host Supervisor |                | Phase 3: AN+LT   | The host supervisor proceeds to perform AN again.
                                                                  This time only the probed rate is advertized and
                                                                  link training is enabled.

@h3 Phase 3: AN/LT
After probing and configuration are complete the host supervisor
directs the AN leader to re-do AN/LT. This time only the
negotiated rate is advertized and

@sequence: title="AN/LT"
- Type    | Source          | Sink            | Name                         | Description
-h Bundle Initialization
- message | Host Supervisor | AN Leader.RX    | Initialize AN Leader RX      | The host supervisor sets up the rules for PLL and RX of the AN leader
                                                                               for auto-negotiation. It sets up the PLL for the rate negotiated
                                                                               during the probe phase.
- message | Host Supervisor | AN Leader.TX    | Initialize AN Leader TX      | The host supervisor sets up the rules for the TX of the AN leader. If
                                                                               the PLL is different than the RX it sets up the PLL for the HCD rate.
-s Initialize Followers (at Probed Rate)
- message | Host Supervisor | Follower.RX[n]  | Initialize LT Follower RX[n] | The host supervisor sets up the rules for the PLL and RX of the
                                                                               LT followers. It sets up the PLL for the rate negotiated during
                                                                               the probe phase.
- message | Host Supervisor | Follower.TX[n]  | Initialize LT Follower TX[n] | The host supervisor sets up the rules for the TX of the LT followers. If
                                                                               the PLL is different than the RX it sets up the PLL for the HCD rate.
-b ... Wait for Followers ...
- message | Follower.RX[n]  | Host Supervisor | Follower[n].RX Ready         | The LT Follower RX[n] indicates to the host supervisor that it is in service
- message | Follower.TX[n]  | Host Supervisor | Follower[n].TX Ready         | The LT Follower TX[n] indicates to the host supervisor that it is in service

-h Autonegotiation Phase (Advertize Probed Rate)
- message | Host Supervisor | AN Leader.RX    | AN_INIT_REQ                  | The host supervisor asserts the CHANNEL_INIT_REQ[n].AN_INIT_REQ and waits
                                                                               for the f/w to assert the CHANNEL_INIT_ACK[n].AN_INIT_ACK indicating the
                                                                               AN sequence has initiated.
- message | AN Leader.RX    | Host Supervisor | AN_INIT_ACK                  | The AN Leader asserts the CHANNEL_INIT_ACK[n].AN_INIT_ACK bit indicating
                                                                               the AN sequence has started.
- message | AN Leader.TX    | AN Leader.RX    | AN.TX Ready                  | The AN Leader TX sends a message to the AN Leader RX indicating it is in service.
- message | AN Leader.RX    | AN Leader.TX    | Send DME Page                | DME Page Exchange
- message | AN Leader.TX    | Link Partner    | DME Page                     | DME Page Exchange
- message | Link Partner    | AN Leader.RX    | DME page                     | DME Page Exchange
-b ... DME Page Exchange ...
- message | AN Leader.RX    | AN Leader.TX    | DME Page                     | DME Page Exchange
- message | AN Leader.TX    | Link Partner    | DME Page                     | DME Page Exchange
- message | Link Partner    | AN Leader.RX    | DME page                     | DME Page Exchange
- action  | AN Leader.RX    |                 | AN DONE                      | The AN leader reports negotiation finished in a status register and proceeeds
                                                                               to link training.
-h Link Training Sequence
- message | AN Leader.RX    | Follower.RX[n]  | Broadcast LT_MSG.START_LT    | The AN Leader broadcasts a message to the LT followers to start Link Training
- message | Follower.RX[n]  | Follower.TX[n]  | LT command                   | The LT follower RX sends the command to the LT follower TX for transmit to the link partner
- message | Follower.TX[n]  | Link Partner    | LT command                   | The follower TX forwards the message to the link partner.
- message | Link Partner    | Follower.RX[n]  | LT reply                     | The link partner acknowledges the command.
-b ... Training Commands ...
- message | Follower.RX[n]  | Follower.TX[n]  | LT command                   | The LT follower RX sends the command to the LT follower TX for transmit to the link partner
- message | Follower.TX[n]  | Link Partner    | LT command                   | The follower TX forwards the message to the link partner.
- message | Link Partner    | Follower.RX[n]  | LT reply                     | The link partner acknolwedges the command.
-s Training Complete
- message | Follower.RX[n]  | AN Leader.RX    | LT_STATUS.Done               | When complete the LT followers use the LT_STATUS bus to indicate completion back to the AN
                                                                               Leader RX and then start sending PCS traffic from the host supervisor. The
                                                                               host supervisor was previously configured to send PCS traffic into the Capella core interface.

-h AN/LT Complete
- message | AN Leader.RX    | Host Supervisor | AN_GOOD                      | Once all LT followers have triggered completion using the LT_STATUS bus the
                                                                               AN Leader advertizes AN_GOOD back to the Host Supervisor.
- note    | Host Supervisor |                 | Link Ready                   | The link is now ready.

@h2 AN/LT Examples
Please refer to the APIExamples folder for examples on configuring and
monitoring AN/LT.


---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
rx_pmd_top ^nxduPdFN

cpl_rx_histogram_fsm_top ^MviaCkt2

cpl_rx_hist_process_hist ^nXWivYCd

if rx_hist_fsm->user != USER_API
cpl_fw_histogram_request_set_ready_status ^b261j0FG

case: STATE_RX_HIST_PROCESS_HIST ^7ZMYvlWI

set hist_ready ^gevdtNIt

rx_qc_histogram_check ^AFE3bckK

rx_quality_check ^fqUTwbJe

RX_QC_DATA_MODE ^TYO53QCv

rx_quality_check ^DT5EbweC

RX_QC_RUN_MODE ^m0zAO4ap

rx_pmd_state_advance ^j4qW13ms

/** Histogram check if SNR passes */
    if (   (p_rx_qc_rules->qc_status.bf.snr_done)
        && (p_rx_qc_rules->qc_status.bf.snr_pass)
        && (!p_rx_qc_rules->qc_status.bf.hist_done)
        && (   ((RX_QC_RUN_MODE  == qc_mode) && qc_hist_up_enable)
            || ((RX_QC_DATA_MODE == qc_mode) && qc_hist_dn_enable)))
    {
        rx_qc_histogram_check(channel, qc_mode, rx_rules);
    } ^A3Dgnhau

qc_hist_data_mode ~ qc_hist_dn_enable ^sIBtWLIe

RX_QC_DATA_MODE == qc_mode ^X4QoGNfa

syrma ^xyShG0fl

compute_histogram_quality ^v0Be9UVA

case: hist_ready ^g87aHx8H

cpl_rx_histogram_override ^CKg9TeG6

STATE_RX_HIST_INIT_CAPTURE ^s2g8qsfa


# Embedded files
1a0c0649dc61406d12e40ddf232d70eebce61f7c: [[20221116155503_450 ~ RX QC mechanism - histogram.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://excalidraw.com",
	"elements": [
		{
			"type": "text",
			"version": 236,
			"versionNonce": 898264667,
			"isDeleted": false,
			"id": "nxduPdFN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 89.60630798339844,
			"y": -658.8000183105469,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 119,
			"height": 24,
			"seed": 616870459,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "qpnKdJJElsnd672LuEcQx",
					"type": "arrow"
				},
				{
					"id": "bmCi5Aebrp13U1k5UxXYu",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "rx_pmd_top",
			"rawText": "rx_pmd_top",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "rx_pmd_top"
		},
		{
			"type": "text",
			"version": 155,
			"versionNonce": 548708699,
			"isDeleted": false,
			"id": "MviaCkt2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -230.9937286376953,
			"y": -365.4000244140625,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 283,
			"height": 24,
			"seed": 1861052885,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "qpnKdJJElsnd672LuEcQx",
					"type": "arrow"
				},
				{
					"id": "WxQf9jiBwFORljWfO5eS8",
					"type": "arrow"
				},
				{
					"id": "igLBtL1QppDIOi4eBmM2-",
					"type": "arrow"
				}
			],
			"updated": 1668591230991,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "cpl_rx_histogram_fsm_top",
			"rawText": "cpl_rx_histogram_fsm_top",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cpl_rx_histogram_fsm_top"
		},
		{
			"type": "arrow",
			"version": 309,
			"versionNonce": 344058619,
			"isDeleted": false,
			"id": "qpnKdJJElsnd672LuEcQx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 126.49134895716483,
			"y": -630.6000061035156,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 186.28154299988762,
			"height": 253.20001220703125,
			"seed": 2086606645,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "nxduPdFN",
				"focus": 0.15657293091258614,
				"gap": 4.20001220703125
			},
			"endBinding": {
				"elementId": "MviaCkt2",
				"focus": 0.08013476423690793,
				"gap": 11.999969482421875
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-186.28154299988762,
					253.20001220703125
				]
			]
		},
		{
			"type": "arrow",
			"version": 214,
			"versionNonce": 1272231067,
			"isDeleted": false,
			"id": "WxQf9jiBwFORljWfO5eS8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -95.36040300833714,
			"y": -333,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1.9637842752049863,
			"height": 184.800048828125,
			"seed": 1844703253,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590623147,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "MviaCkt2",
				"focus": 0.04295391193382149,
				"gap": 8.4000244140625
			},
			"endBinding": {
				"elementId": "nXWivYCd",
				"focus": -0.06824137143201635,
				"gap": 10.39996337890625
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					1.9637842752049863,
					184.800048828125
				]
			]
		},
		{
			"type": "text",
			"version": 115,
			"versionNonce": 1141985109,
			"isDeleted": false,
			"id": "b261j0FG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -278.9937286376953,
			"y": 87.800048828125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 482,
			"height": 48,
			"seed": 1695833237,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "Tc780bAUXszc3Hq0-zbOb",
					"type": "arrow"
				},
				{
					"id": "7JysqnsTiOblDyzO24gY3",
					"type": "arrow"
				}
			],
			"updated": 1668591242249,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "if rx_hist_fsm->user != USER_API\ncpl_fw_histogram_request_set_ready_status",
			"rawText": "if rx_hist_fsm->user != USER_API\ncpl_fw_histogram_request_set_ready_status",
			"baseline": 43,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "if rx_hist_fsm->user != USER_API\ncpl_fw_histogram_request_set_ready_status"
		},
		{
			"type": "arrow",
			"version": 265,
			"versionNonce": 1848207675,
			"isDeleted": false,
			"id": "Tc780bAUXszc3Hq0-zbOb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -78.11161224519918,
			"y": -72.5999755859375,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0.9232714441020278,
			"height": 150,
			"seed": 745140981,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590623148,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "7ZMYvlWI",
				"focus": 0.01559620998790989,
				"gap": 8
			},
			"endBinding": {
				"elementId": "b261j0FG",
				"focus": -0.16165557999318014,
				"gap": 10.4000244140625
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0.9232714441020278,
					150
				]
			]
		},
		{
			"type": "text",
			"version": 128,
			"versionNonce": 2115610683,
			"isDeleted": false,
			"id": "nXWivYCd",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -224.9937286376953,
			"y": -137.79998779296875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 283,
			"height": 24,
			"seed": 2075309173,
			"groupIds": [
				"kRi5wHt6T9B3sw552UKlr"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "WxQf9jiBwFORljWfO5eS8",
					"type": "arrow"
				},
				{
					"id": "Tc780bAUXszc3Hq0-zbOb",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "cpl_rx_hist_process_hist",
			"rawText": "cpl_rx_hist_process_hist",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cpl_rx_hist_process_hist"
		},
		{
			"type": "text",
			"version": 234,
			"versionNonce": 1205882101,
			"isDeleted": false,
			"id": "7ZMYvlWI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -263.79368591308594,
			"y": -104.5999755859375,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 377,
			"height": 24,
			"seed": 215609915,
			"groupIds": [
				"kRi5wHt6T9B3sw552UKlr"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "Tc780bAUXszc3Hq0-zbOb",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "case: STATE_RX_HIST_PROCESS_HIST",
			"rawText": "case: STATE_RX_HIST_PROCESS_HIST",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "case: STATE_RX_HIST_PROCESS_HIST"
		},
		{
			"type": "text",
			"version": 54,
			"versionNonce": 1590618331,
			"isDeleted": false,
			"id": "gevdtNIt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -132.3937225341797,
			"y": 142.800048828125,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 167,
			"height": 24,
			"seed": 1528841685,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "set hist_ready",
			"rawText": "set hist_ready",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "set hist_ready"
		},
		{
			"type": "text",
			"version": 119,
			"versionNonce": 1062055003,
			"isDeleted": false,
			"id": "AFE3bckK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 334.40614318847656,
			"y": -35.79998779296875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 248,
			"height": 24,
			"seed": 1072997781,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "JdZBP5-OTqQcJSjoYjUs7",
					"type": "arrow"
				},
				{
					"id": "abj4FUQz7fe_omutIQGnc",
					"type": "arrow"
				},
				{
					"id": "uSaMAnD1Te-TfPJnSB7ai",
					"type": "arrow"
				}
			],
			"updated": 1668590157936,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "rx_qc_histogram_check",
			"rawText": "rx_qc_histogram_check",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "rx_qc_histogram_check"
		},
		{
			"type": "text",
			"version": 73,
			"versionNonce": 1146295675,
			"isDeleted": false,
			"id": "fqUTwbJe",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 203.6062469482422,
			"y": -201.20001220703125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 189,
			"height": 24,
			"seed": 1596586357,
			"groupIds": [
				"QaQKAzeobD7NxDOwtLQ4z"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "4LumsUTme6mCAZbAfyXQD",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "rx_quality_check",
			"rawText": "rx_quality_check",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "rx_quality_check"
		},
		{
			"type": "text",
			"version": 89,
			"versionNonce": 774853557,
			"isDeleted": false,
			"id": "TYO53QCv",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 210.99593284216928,
			"y": -171.31974286523916,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 177,
			"height": 24,
			"seed": 1662053915,
			"groupIds": [
				"QaQKAzeobD7NxDOwtLQ4z"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "JdZBP5-OTqQcJSjoYjUs7",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "RX_QC_DATA_MODE",
			"rawText": "RX_QC_DATA_MODE",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "RX_QC_DATA_MODE"
		},
		{
			"type": "text",
			"version": 56,
			"versionNonce": 233352731,
			"isDeleted": false,
			"id": "DT5EbweC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 476.4061737060547,
			"y": -212.20001220703125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 189,
			"height": 24,
			"seed": 755919355,
			"groupIds": [
				"D912ISUq0PGDAOxtX_6eD"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "t7qhInscC02cXKNYiQK7t",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "rx_quality_check",
			"rawText": "rx_quality_check",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "rx_quality_check"
		},
		{
			"type": "text",
			"version": 126,
			"versionNonce": 617944341,
			"isDeleted": false,
			"id": "m0zAO4ap",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 489.9737056246497,
			"y": -180.45132326951227,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 167,
			"height": 24,
			"seed": 915449045,
			"groupIds": [
				"D912ISUq0PGDAOxtX_6eD"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "abj4FUQz7fe_omutIQGnc",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "RX_QC_RUN_MODE",
			"rawText": "RX_QC_RUN_MODE",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "RX_QC_RUN_MODE"
		},
		{
			"type": "text",
			"version": 150,
			"versionNonce": 243413691,
			"isDeleted": false,
			"id": "j4qW13ms",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 313.28147084794807,
			"y": -367.5315632588389,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 236,
			"height": 24,
			"seed": 1563784629,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "4LumsUTme6mCAZbAfyXQD",
					"type": "arrow"
				},
				{
					"id": "t7qhInscC02cXKNYiQK7t",
					"type": "arrow"
				},
				{
					"id": "bmCi5Aebrp13U1k5UxXYu",
					"type": "arrow"
				}
			],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "rx_pmd_state_advance",
			"rawText": "rx_pmd_state_advance",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "rx_pmd_state_advance"
		},
		{
			"type": "arrow",
			"version": 254,
			"versionNonce": 939240053,
			"isDeleted": false,
			"id": "4LumsUTme6mCAZbAfyXQD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 407.9239553860974,
			"y": -338.1315388447764,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 112.94377090287423,
			"height": 126.3314900166514,
			"seed": 280211605,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "j4qW13ms",
				"focus": 0.06060370422044145,
				"gap": 5.4000244140625
			},
			"endBinding": {
				"elementId": "fqUTwbJe",
				"focus": -0.2217188848189193,
				"gap": 10.60003662109375
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-112.94377090287423,
					126.3314900166514
				]
			]
		},
		{
			"type": "arrow",
			"version": 272,
			"versionNonce": 381821787,
			"isDeleted": false,
			"id": "t7qhInscC02cXKNYiQK7t",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 429.4109600237765,
			"y": -336.9315571553233,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 131.26631766691764,
			"height": 119.13156936235453,
			"seed": 969283771,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "j4qW13ms",
				"focus": 0.17044478395705157,
				"gap": 6.600006103515625
			},
			"endBinding": {
				"elementId": "DT5EbweC",
				"focus": 0.08506885118259294,
				"gap": 5.5999755859375
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					131.26631766691764,
					119.13156936235453
				]
			]
		},
		{
			"type": "arrow",
			"version": 238,
			"versionNonce": 1214813141,
			"isDeleted": false,
			"id": "bmCi5Aebrp13U1k5UxXYu",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 142.5594969148296,
			"y": -627.0000152587891,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 284.70543694505665,
			"height": 249.26847031049704,
			"seed": 666531573,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "nxduPdFN",
				"focus": 0.3984510992021368,
				"gap": 7.8000030517578125
			},
			"endBinding": {
				"elementId": "j4qW13ms",
				"focus": 0.16202363706397838,
				"gap": 10.199981689453125
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					284.70543694505665,
					249.26847031049704
				]
			]
		},
		{
			"type": "arrow",
			"version": 121,
			"versionNonce": 1056636923,
			"isDeleted": false,
			"id": "JdZBP5-OTqQcJSjoYjUs7",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 301.85209073162173,
			"y": -141.31974286523916,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 149.26641027418907,
			"height": 93.91977948633291,
			"seed": 1250991611,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "TYO53QCv",
				"focus": 0.24401805841557514,
				"gap": 6
			},
			"endBinding": {
				"elementId": "AFE3bckK",
				"focus": 0.2112210445067549,
				"gap": 11.5999755859375
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					149.26641027418907,
					93.91977948633291
				]
			]
		},
		{
			"type": "arrow",
			"version": 134,
			"versionNonce": 36786485,
			"isDeleted": false,
			"id": "abj4FUQz7fe_omutIQGnc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 577.8426885414962,
			"y": -147.65127444138727,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 117.97872549240708,
			"height": 102.65127444138727,
			"seed": 1797640341,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "m0zAO4ap",
				"focus": -0.3116086571992648,
				"gap": 8.800048828125
			},
			"endBinding": {
				"elementId": "AFE3bckK",
				"focus": -0.16624857004832566,
				"gap": 9.20001220703125
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-117.97872549240708,
					102.65127444138727
				]
			]
		},
		{
			"type": "text",
			"version": 55,
			"versionNonce": 1898924187,
			"isDeleted": false,
			"id": "A3Dgnhau",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 763.4258657282439,
			"y": -553.5809650270688,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 798,
			"height": 216,
			"seed": 1585151387,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "/** Histogram check if SNR passes */\n    if (   (p_rx_qc_rules->qc_status.bf.snr_done)\n        && (p_rx_qc_rules->qc_status.bf.snr_pass)\n        && (!p_rx_qc_rules->qc_status.bf.hist_done)\n        && (   ((RX_QC_RUN_MODE  == qc_mode) && qc_hist_up_enable)\n            || ((RX_QC_DATA_MODE == qc_mode) && qc_hist_dn_enable)))\n    {\n        rx_qc_histogram_check(channel, qc_mode, rx_rules);\n    }",
			"rawText": "/** Histogram check if SNR passes */\n    if (   (p_rx_qc_rules->qc_status.bf.snr_done)\n        && (p_rx_qc_rules->qc_status.bf.snr_pass)\n        && (!p_rx_qc_rules->qc_status.bf.hist_done)\n        && (   ((RX_QC_RUN_MODE  == qc_mode) && qc_hist_up_enable)\n            || ((RX_QC_DATA_MODE == qc_mode) && qc_hist_dn_enable)))\n    {\n        rx_qc_histogram_check(channel, qc_mode, rx_rules);\n    }",
			"baseline": 211,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "/** Histogram check if SNR passes */\n    if (   (p_rx_qc_rules->qc_status.bf.snr_done)\n        && (p_rx_qc_rules->qc_status.bf.snr_pass)\n        && (!p_rx_qc_rules->qc_status.bf.hist_done)\n        && (   ((RX_QC_RUN_MODE  == qc_mode) && qc_hist_up_enable)\n            || ((RX_QC_DATA_MODE == qc_mode) && qc_hist_dn_enable)))\n    {\n        rx_qc_histogram_check(channel, qc_mode, rx_rules);\n    }"
		},
		{
			"type": "text",
			"version": 248,
			"versionNonce": 1924883093,
			"isDeleted": false,
			"id": "sIBtWLIe",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 779.7359546583272,
			"y": -623.8671215657945,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 435,
			"height": 24,
			"seed": 1157583067,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "qc_hist_data_mode ~ qc_hist_dn_enable",
			"rawText": "qc_hist_data_mode ~ qc_hist_dn_enable",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "qc_hist_data_mode ~ qc_hist_dn_enable"
		},
		{
			"type": "text",
			"version": 38,
			"versionNonce": 856784187,
			"isDeleted": false,
			"id": "X4QoGNfa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 788.9878673994758,
			"y": -666.9629716204487,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 307,
			"height": 24,
			"seed": 1924423285,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1668590118556,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "RX_QC_DATA_MODE == qc_mode",
			"rawText": "RX_QC_DATA_MODE == qc_mode",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "RX_QC_DATA_MODE == qc_mode"
		},
		{
			"type": "image",
			"version": 346,
			"versionNonce": 1355972027,
			"isDeleted": false,
			"id": "j7VerBOZdnp2EChTx0zIF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 804.0980269070283,
			"y": -274.4453642043418,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 429,
			"height": 755,
			"seed": 84537653,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590199875,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "1a0c0649dc61406d12e40ddf232d70eebce61f7c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 118,
			"versionNonce": 1027941173,
			"isDeleted": false,
			"id": "xyShG0fl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 911.6562831546278,
			"y": 507.26237630172864,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 108,
			"height": 43,
			"seed": 121950485,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1668591998834,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "syrma",
			"rawText": "syrma",
			"baseline": 35,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "syrma"
		},
		{
			"type": "arrow",
			"version": 226,
			"versionNonce": 1088935803,
			"isDeleted": false,
			"id": "uSaMAnD1Te-TfPJnSB7ai",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 455.3558787650842,
			"y": -5.044317211777525,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 1.9630433494131694,
			"height": 86.90385257737734,
			"seed": 918368923,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668590261139,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "AFE3bckK",
				"focus": 0.027954458222155042,
				"gap": 6.755670581191225
			},
			"endBinding": {
				"elementId": "g87aHx8H",
				"focus": -0.12775300715991103,
				"gap": 9.868173948967126
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					1.9630433494131694,
					86.90385257737734
				]
			]
		},
		{
			"type": "text",
			"version": 45,
			"versionNonce": 934444661,
			"isDeleted": false,
			"id": "v0Be9UVA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 327.1230469112436,
			"y": 121.43739580266543,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 295,
			"height": 24,
			"seed": 344493749,
			"groupIds": [
				"cFX_U5PGyLl__1_W9jPvf"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "uSaMAnD1Te-TfPJnSB7ai",
					"type": "arrow"
				}
			],
			"updated": 1668590266115,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "compute_histogram_quality",
			"rawText": "compute_histogram_quality",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "compute_histogram_quality"
		},
		{
			"type": "text",
			"version": 458,
			"versionNonce": 831688539,
			"isDeleted": false,
			"id": "g87aHx8H",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 375.4201837450255,
			"y": 91.72770931456694,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 189,
			"height": 24,
			"seed": 762688891,
			"groupIds": [
				"coRoqCs5ME1ykUHHMSHXb",
				"cFX_U5PGyLl__1_W9jPvf"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "Tc780bAUXszc3Hq0-zbOb",
					"type": "arrow"
				},
				{
					"id": "uSaMAnD1Te-TfPJnSB7ai",
					"type": "arrow"
				}
			],
			"updated": 1668590266115,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "case: hist_ready",
			"rawText": "case: hist_ready",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "case: hist_ready"
		},
		{
			"type": "text",
			"version": 97,
			"versionNonce": 1828050421,
			"isDeleted": false,
			"id": "CKg9TeG6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -664.9549698081976,
			"y": -141.10491567715667,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 295,
			"height": 24,
			"seed": 740914107,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "igLBtL1QppDIOi4eBmM2-",
					"type": "arrow"
				},
				{
					"id": "7JysqnsTiOblDyzO24gY3",
					"type": "arrow"
				}
			],
			"updated": 1668591242249,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "cpl_rx_histogram_override",
			"rawText": "cpl_rx_histogram_override",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cpl_rx_histogram_override"
		},
		{
			"type": "arrow",
			"version": 49,
			"versionNonce": 1801778645,
			"isDeleted": false,
			"id": "igLBtL1QppDIOi4eBmM2-",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -91.4847890865592,
			"y": -332.0560378029288,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 417.6000976562501,
			"height": 175.2000732421875,
			"seed": 1196982875,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668591230991,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "MviaCkt2",
				"focus": -0.28737714387061164,
				"gap": 9.343986611133687
			},
			"endBinding": {
				"elementId": "CKg9TeG6",
				"focus": -0.3280825855641587,
				"gap": 15.751048883584644
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-417.6000976562501,
					175.2000732421875
				]
			]
		},
		{
			"type": "arrow",
			"version": 130,
			"versionNonce": 786636123,
			"isDeleted": false,
			"id": "7JysqnsTiOblDyzO24gY3",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -506.7370675884182,
			"y": -73.98535909199131,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 420.65592421174597,
			"height": 152.3294677734375,
			"seed": 588924571,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1668591320918,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "s2g8qsfa",
				"focus": 0.3103428390139602,
				"gap": 12.094166475183783
			},
			"endBinding": {
				"elementId": "b261j0FG",
				"focus": 0.14417263188103782,
				"gap": 9.455940146678813
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					420.65592421174597,
					152.3294677734375
				]
			]
		},
		{
			"type": "text",
			"version": 47,
			"versionNonce": 1014091643,
			"isDeleted": false,
			"id": "s2g8qsfa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -668.8495782639491,
			"y": -110.0795255671751,
			"strokeColor": "#364fc7",
			"backgroundColor": "transparent",
			"width": 307,
			"height": 24,
			"seed": 697726235,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "7JysqnsTiOblDyzO24gY3",
					"type": "arrow"
				}
			],
			"updated": 1668591287930,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "STATE_RX_HIST_INIT_CAPTURE",
			"rawText": "STATE_RX_HIST_INIT_CAPTURE",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "STATE_RX_HIST_INIT_CAPTURE"
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#364fc7",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "hachure",
		"currentItemStrokeWidth": 1,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 3,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStrokeSharpness": "sharp",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"currentItemLinearStrokeSharpness": "round",
		"gridSize": null,
		"colorPalette": {}
	},
	"files": {}
}
```
%%
---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Section 2: Basic ^caY4bANg

Advanced C Programming Masterclass - Pointers & Memory in C ^P2M6SjuR

int a;
int *p;
p = &a;
*p = 5; ^LrgHrglC

5 ^qTm7ss6n

a ^V6TuIm4h

p ^cF2KKQbr

address a ^MuuH263n

Pointers Dereferencing ^Wlj8tNj9

printf("%p", p);
printf("%d", *p);

printf("%p", &a); ^qiVOnDmY

Section 3: Pointers Arithmetic ^HdjWrQ2I

20 ^0DxRbv06

50 ^i156YNfr

35 ^9NwqXwEi

address ^iM56KLzd

0x40000 ^C5lHXOD3

0x40001 ^teOiJ2Lb

0x40002 ^oGJZjRFC

0x40003 ^uSYGz5Bg

0x40005 ^FPKeY9TL

0x40006 ^i6EYS0VC

0x40007 ^7FMLy4cf

0x40004 ^8AWlPPRA

arrays[0] ^GQAvUics

arrays[1] ^mLScPP6g

arrays[2] ^Bnmaxe9j

arrays[3] = {20, 50, 35}; ^7eoTX2Gm

printf("%p", &arrays[0]);
printf("%p", arrays); ^XpbJXu0j

printf("%p", &arrays[1]); ^cymedq3y

printf("%p", arrays+1); ^ar2HMtrf

Section 4: Pointers Concept ^kzptkUYY

sizeof(int) = 4 ^r90yDXLU

sizeof(arrays) = 3 * 4 = 12 ^5KuiI4vy

#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int a = 10;
    int b = 20;

    printf("Before: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After:  a = %d, b = %d\n", a, b);

    return 0;
}
 ^OPSIcvtS

void *
Generic pointer ^owtUrdu4

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
			"version": 346,
			"versionNonce": 581215017,
			"isDeleted": false,
			"id": "caY4bANg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -835.9999999999999,
			"y": 92.67447916666674,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 163,
			"height": 25,
			"seed": 1531636473,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "7YJ8Xi-iLmHsCKnGcXFG2",
					"type": "arrow"
				},
				{
					"id": "AtzwNXqe2azDIYVaf1Ap_",
					"type": "arrow"
				}
			],
			"updated": 1666280721411,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Section 2: Basic",
			"rawText": "Section 2: Basic",
			"baseline": 18,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Section 2: Basic"
		},
		{
			"type": "text",
			"version": 36,
			"versionNonce": 281827145,
			"isDeleted": false,
			"id": "P2M6SjuR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -217,
			"y": -352.9921875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 693,
			"height": 24,
			"seed": 363920089,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "AtzwNXqe2azDIYVaf1Ap_",
					"type": "arrow"
				},
				{
					"id": "9ySmmU43ucR4LGMJGv71T",
					"type": "arrow"
				}
			],
			"updated": 1666280753705,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "Advanced C Programming Masterclass - Pointers & Memory in C",
			"rawText": "Advanced C Programming Masterclass - Pointers & Memory in C",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Advanced C Programming Masterclass - Pointers & Memory in C"
		},
		{
			"type": "arrow",
			"version": 718,
			"versionNonce": 173561353,
			"isDeleted": false,
			"id": "7YJ8Xi-iLmHsCKnGcXFG2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -741.5837946761305,
			"y": 125.0637056327162,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0.6948703526218196,
			"height": 22.39848572530849,
			"seed": 2143787031,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666280721413,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "caY4bANg",
				"gap": 7.389226466049421,
				"focus": -0.12198044929034678
			},
			"endBinding": {
				"elementId": "-cN44PoPdeyO_WLL7rl60",
				"gap": 3.641975308641891,
				"focus": -0.5638493194048746
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
					0.6948703526218196,
					22.39848572530849
				]
			]
		},
		{
			"type": "arrow",
			"version": 478,
			"versionNonce": 381395625,
			"isDeleted": false,
			"id": "AtzwNXqe2azDIYVaf1Ap_",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -103.60879132627633,
			"y": -320.56249999999994,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 618.9972716965776,
			"height": 405.00000000000006,
			"seed": 1285874969,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666280749811,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "P2M6SjuR",
				"focus": 0.5093243912925787,
				"gap": 7.429687500000057
			},
			"endBinding": {
				"elementId": "caY4bANg",
				"focus": 0.0019857900618894422,
				"gap": 8.236979166666629
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
					-618.9972716965776,
					405.00000000000006
				]
			]
		},
		{
			"type": "text",
			"version": 124,
			"versionNonce": 990127593,
			"isDeleted": false,
			"id": "LrgHrglC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -734.6666666666665,
			"y": 232.10416666666663,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 96,
			"seed": 828793049,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666280662594,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "int a;\nint *p;\np = &a;\n*p = 5;",
			"rawText": "int a;\nint *p;\np = &a;\n*p = 5;",
			"baseline": 91,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "int a;\nint *p;\np = &a;\n*p = 5;"
		},
		{
			"type": "rectangle",
			"version": 152,
			"versionNonce": 52971815,
			"isDeleted": false,
			"id": "i5vHKGvDG0D_ai2calIcK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -611.5,
			"y": 360.9375,
			"strokeColor": "#5f3dc4",
			"backgroundColor": "transparent",
			"width": 92,
			"height": 77,
			"seed": 2024379705,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"type": "text",
					"id": "qTm7ss6n"
				},
				{
					"id": "L6Aiu6Mr2hYk5Ozt3HUl2",
					"type": "arrow"
				}
			],
			"updated": 1666280662594,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 123,
			"versionNonce": 1496940745,
			"isDeleted": false,
			"id": "qTm7ss6n",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -572.5,
			"y": 387.4375,
			"strokeColor": "#5f3dc4",
			"backgroundColor": "transparent",
			"width": 14,
			"height": 24,
			"seed": 1293691095,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666280662594,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "5",
			"rawText": "5",
			"baseline": 19,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "i5vHKGvDG0D_ai2calIcK",
			"originalText": "5"
		},
		{
			"type": "text",
			"version": 127,
			"versionNonce": 296913991,
			"isDeleted": false,
			"id": "V6TuIm4h",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -569.6666666666666,
			"y": 463.2708333333329,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 14,
			"height": 24,
			"seed": 711748023,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666280662594,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "a",
			"rawText": "a",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "a"
		},
		{
			"type": "text",
			"version": 124,
			"versionNonce": 29392809,
			"isDeleted": false,
			"id": "cF2KKQbr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -781.3333333333331,
			"y": 453.2708333333329,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 14,
			"height": 24,
			"seed": 1516934103,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666280662594,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "p",
			"rawText": "p",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "p"
		},
		{
			"type": "rectangle",
			"version": 211,
			"versionNonce": 1481075559,
			"isDeleted": false,
			"id": "b55A3p1NFQM5QgNSUt4oP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -840.6666666666665,
			"y": 360.9374999999999,
			"strokeColor": "#5f3dc4",
			"backgroundColor": "transparent",
			"width": 137,
			"height": 77,
			"seed": 558370007,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "MuuH263n",
					"type": "text"
				},
				{
					"id": "L6Aiu6Mr2hYk5Ozt3HUl2",
					"type": "arrow"
				}
			],
			"updated": 1666280662595,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 191,
			"versionNonce": 1120182921,
			"isDeleted": false,
			"id": "MuuH263n",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -825.6666666666665,
			"y": 387.4374999999999,
			"strokeColor": "#5f3dc4",
			"backgroundColor": "transparent",
			"width": 107,
			"height": 24,
			"seed": 11341849,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666280662595,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "address a",
			"rawText": "address a",
			"baseline": 19,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "b55A3p1NFQM5QgNSUt4oP",
			"originalText": "address a"
		},
		{
			"type": "arrow",
			"version": 366,
			"versionNonce": 1127486121,
			"isDeleted": false,
			"id": "L6Aiu6Mr2hYk5Ozt3HUl2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -697.9999999999999,
			"y": 399.2789283821088,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 83.33333333333337,
			"height": 1.5206112723917045,
			"seed": 1601318135,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281525183,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "b55A3p1NFQM5QgNSUt4oP",
				"gap": 5.666666666666629,
				"focus": 0.03005721116608666
			},
			"endBinding": {
				"elementId": "i5vHKGvDG0D_ai2calIcK",
				"gap": 3.166666666666515,
				"focus": 0.0654901960784369
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
					83.33333333333337,
					-1.5206112723917045
				]
			]
		},
		{
			"type": "text",
			"version": 119,
			"versionNonce": 1493264745,
			"isDeleted": false,
			"id": "Wlj8tNj9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -807.9999999999999,
			"y": 184.9375,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 260,
			"height": 24,
			"seed": 1524645849,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666280662595,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "Pointers Dereferencing",
			"rawText": "Pointers Dereferencing",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Pointers Dereferencing"
		},
		{
			"type": "rectangle",
			"version": 169,
			"versionNonce": 1093860775,
			"isDeleted": false,
			"id": "-cN44PoPdeyO_WLL7rl60",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -901.3333333333333,
			"y": 151.10416666666663,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 780,
			"height": 393.3333333333333,
			"seed": 1187976887,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "7YJ8Xi-iLmHsCKnGcXFG2",
					"type": "arrow"
				}
			],
			"updated": 1666280662595,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 415,
			"versionNonce": 1573016649,
			"isDeleted": false,
			"id": "qiVOnDmY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -418.11904761904714,
			"y": 282.080357142857,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 201,
			"height": 96,
			"seed": 1632857241,
			"groupIds": [
				"63rQxz_F9zhRFw0_Fqgyn"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666280662595,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "printf(\"%p\", p);\nprintf(\"%d\", *p);\n\nprintf(\"%p\", &a);",
			"rawText": "printf(\"%p\", p);\nprintf(\"%d\", *p);\n\nprintf(\"%p\", &a);",
			"baseline": 91,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "printf(\"%p\", p);\nprintf(\"%d\", *p);\n\nprintf(\"%p\", &a);"
		},
		{
			"type": "arrow",
			"version": 495,
			"versionNonce": 1919116681,
			"isDeleted": false,
			"id": "9ySmmU43ucR4LGMJGv71T",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 70.56890827809416,
			"y": -319.2474732636874,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 174.28922828840115,
			"height": 1066.6666666666663,
			"seed": 1229279847,
			"groupIds": [],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666280749812,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "P2M6SjuR",
				"focus": 0.06970458535751851,
				"gap": 8.744714236312518
			},
			"endBinding": {
				"elementId": "N_ignF0dKJhQZtjKNRzPj",
				"focus": 0.20829946321179044,
				"gap": 9.590981810943958
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
					-174.28922828840115,
					1066.6666666666663
				]
			]
		},
		{
			"type": "text",
			"version": 285,
			"versionNonce": 2047227017,
			"isDeleted": false,
			"id": "HdjWrQ2I",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -524.3214955540163,
			"y": 809.1580675879259,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 354,
			"height": 24,
			"seed": 2145895705,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "10DUc1jkRrJc3Jky1FwDR",
					"type": "arrow"
				}
			],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "Section 3: Pointers Arithmetic",
			"rawText": "Section 3: Pointers Arithmetic",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Section 3: Pointers Arithmetic"
		},
		{
			"type": "rectangle",
			"version": 329,
			"versionNonce": 940307591,
			"isDeleted": false,
			"id": "KNx9rVt953rwdHfI4Dz4t",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -513.0000000000002,
			"y": 955.2434895833331,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 137,
			"height": 382,
			"seed": 274718457,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false
		},
		{
			"type": "freedraw",
			"version": 263,
			"versionNonce": 373341033,
			"isDeleted": false,
			"id": "5h6JIAcZ2rNbyuykqlCH3",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -512.8333333333335,
			"y": 1073.743489583333,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 136.66666666666674,
			"height": 5,
			"seed": 1368454105,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.333333333333485,
					0
				],
				[
					5,
					0
				],
				[
					20,
					0
				],
				[
					25,
					0
				],
				[
					31.666666666666515,
					0
				],
				[
					33.33333333333326,
					0
				],
				[
					40,
					0
				],
				[
					41.666666666666515,
					0
				],
				[
					48.33333333333326,
					0
				],
				[
					50,
					0
				],
				[
					56.666666666666515,
					0
				],
				[
					60,
					0
				],
				[
					63.33333333333326,
					0
				],
				[
					65,
					0
				],
				[
					66.66666666666652,
					0
				],
				[
					68.33333333333326,
					0
				],
				[
					70,
					0
				],
				[
					75,
					0
				],
				[
					76.66666666666652,
					0
				],
				[
					78.33333333333326,
					0
				],
				[
					81.66666666666652,
					0
				],
				[
					84.99999999999977,
					0
				],
				[
					89.99999999999977,
					0
				],
				[
					93.33333333333326,
					0
				],
				[
					94.99999999999977,
					1.6666666666667425
				],
				[
					98.33333333333326,
					1.6666666666667425
				],
				[
					101.66666666666652,
					1.6666666666667425
				],
				[
					103.33333333333326,
					1.6666666666667425
				],
				[
					106.66666666666652,
					1.6666666666667425
				],
				[
					108.33333333333326,
					3.3333333333333712
				],
				[
					109.99999999999977,
					3.3333333333333712
				],
				[
					111.66666666666652,
					3.3333333333333712
				],
				[
					113.33333333333326,
					3.3333333333333712
				],
				[
					114.99999999999977,
					5
				],
				[
					116.66666666666652,
					5
				],
				[
					118.33333333333326,
					5
				],
				[
					121.66666666666652,
					5
				],
				[
					123.33333333333326,
					5
				],
				[
					126.66666666666652,
					5
				],
				[
					128.33333333333326,
					3.3333333333333712
				],
				[
					129.99999999999977,
					3.3333333333333712
				],
				[
					131.66666666666652,
					1.6666666666667425
				],
				[
					133.33333333333326,
					0
				],
				[
					133.33333333333326,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 248,
			"versionNonce": 2009713575,
			"isDeleted": false,
			"id": "hvBBG7Zb6d6FThnRAVtct",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -509.5000000000002,
			"y": 1217.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 120,
			"height": 1.6666666666666288,
			"seed": 347856889,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.3333333333332575,
					0
				],
				[
					13.333333333333258,
					0
				],
				[
					18.333333333333258,
					0
				],
				[
					25,
					0
				],
				[
					33.33333333333326,
					0
				],
				[
					43.33333333333326,
					0
				],
				[
					50,
					0
				],
				[
					55,
					0
				],
				[
					61.66666666666674,
					0
				],
				[
					65,
					0
				],
				[
					70,
					0
				],
				[
					71.66666666666674,
					0
				],
				[
					75,
					0
				],
				[
					81.66666666666652,
					0
				],
				[
					85,
					0
				],
				[
					90,
					0
				],
				[
					91.66666666666652,
					0
				],
				[
					95,
					0
				],
				[
					96.66666666666652,
					0
				],
				[
					101.66666666666652,
					0
				],
				[
					105,
					0
				],
				[
					106.66666666666652,
					0
				],
				[
					110,
					0
				],
				[
					111.66666666666652,
					1.6666666666666288
				],
				[
					115,
					1.6666666666666288
				],
				[
					116.66666666666652,
					1.6666666666666288
				],
				[
					118.33333333333326,
					1.6666666666666288
				],
				[
					120,
					1.6666666666666288
				],
				[
					120,
					1.6666666666666288
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 228,
			"versionNonce": 457664073,
			"isDeleted": false,
			"id": "0DxRbv06",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -451.16666666666697,
			"y": 999.243489583333,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 25,
			"height": 24,
			"seed": 1216323831,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "20",
			"rawText": "20",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "20"
		},
		{
			"type": "text",
			"version": 236,
			"versionNonce": 738180807,
			"isDeleted": false,
			"id": "i156YNfr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -461.16666666666674,
			"y": 1132.5768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 25,
			"height": 24,
			"seed": 255522937,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "50",
			"rawText": "50",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "50"
		},
		{
			"type": "text",
			"version": 220,
			"versionNonce": 1677047081,
			"isDeleted": false,
			"id": "9NwqXwEi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -457.8333333333335,
			"y": 1270.91015625,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 25,
			"height": 24,
			"seed": 502541049,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "35",
			"rawText": "35",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "35"
		},
		{
			"type": "text",
			"version": 239,
			"versionNonce": 1196051943,
			"isDeleted": false,
			"id": "iM56KLzd",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -353.90320302069335,
			"y": 911.592375224714,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 1049740119,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "address",
			"rawText": "address",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "address"
		},
		{
			"type": "freedraw",
			"version": 253,
			"versionNonce": 1672947721,
			"isDeleted": false,
			"id": "oNFW1dHCBGuXVGSwCyLlX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -375.16666666666697,
			"y": 954.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 124,
			"height": 2,
			"seed": 448384247,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1
				],
				[
					2,
					-1
				],
				[
					7,
					-1
				],
				[
					14,
					0
				],
				[
					22,
					1
				],
				[
					26,
					1
				],
				[
					28,
					1
				],
				[
					33,
					1
				],
				[
					39,
					1
				],
				[
					42,
					1
				],
				[
					46,
					1
				],
				[
					49,
					1
				],
				[
					51,
					1
				],
				[
					54,
					1
				],
				[
					59,
					1
				],
				[
					64,
					1
				],
				[
					71,
					1
				],
				[
					75,
					1
				],
				[
					80,
					1
				],
				[
					85,
					1
				],
				[
					88,
					1
				],
				[
					90,
					1
				],
				[
					94,
					1
				],
				[
					99,
					1
				],
				[
					103,
					1
				],
				[
					106,
					1
				],
				[
					109,
					1
				],
				[
					110,
					1
				],
				[
					113,
					1
				],
				[
					117,
					1
				],
				[
					119,
					1
				],
				[
					120,
					1
				],
				[
					122,
					1
				],
				[
					124,
					1
				],
				[
					124,
					1
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 242,
			"versionNonce": 884340999,
			"isDeleted": false,
			"id": "DXlb4r9z6yJlDijY0Yh_c",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -374.16666666666697,
			"y": 1073.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 125,
			"height": 2,
			"seed": 775185849,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					8,
					0
				],
				[
					19,
					1
				],
				[
					23,
					2
				],
				[
					34,
					2
				],
				[
					52,
					2
				],
				[
					61,
					2
				],
				[
					71,
					2
				],
				[
					78,
					2
				],
				[
					82,
					2
				],
				[
					86,
					2
				],
				[
					87,
					2
				],
				[
					88,
					2
				],
				[
					92,
					2
				],
				[
					96,
					2
				],
				[
					103,
					2
				],
				[
					107,
					2
				],
				[
					113,
					2
				],
				[
					116,
					2
				],
				[
					119,
					2
				],
				[
					120,
					2
				],
				[
					122,
					2
				],
				[
					123,
					2
				],
				[
					125,
					2
				],
				[
					125,
					2
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 240,
			"versionNonce": 344407785,
			"isDeleted": false,
			"id": "9eWbrZsusWLcXV4uFqiKf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -373.16666666666697,
			"y": 983.0768229166666,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 111,
			"height": 3,
			"seed": 1137330457,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1
				],
				[
					1,
					1
				],
				[
					5,
					1
				],
				[
					15,
					2
				],
				[
					24,
					2
				],
				[
					34,
					2
				],
				[
					48,
					3
				],
				[
					59,
					3
				],
				[
					67,
					3
				],
				[
					73,
					3
				],
				[
					79,
					3
				],
				[
					84,
					3
				],
				[
					88,
					3
				],
				[
					93,
					3
				],
				[
					95,
					3
				],
				[
					97,
					3
				],
				[
					100,
					3
				],
				[
					104,
					2
				],
				[
					107,
					2
				],
				[
					110,
					2
				],
				[
					111,
					2
				],
				[
					111,
					2
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 243,
			"versionNonce": 1237270567,
			"isDeleted": false,
			"id": "1WsGfKqhMfjceIHzwx2vR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -372.16666666666697,
			"y": 1013.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 86,
			"height": 2,
			"seed": 1476627353,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2,
					0
				],
				[
					3,
					0
				],
				[
					7,
					0
				],
				[
					16,
					0
				],
				[
					20,
					0
				],
				[
					29,
					0
				],
				[
					36,
					0
				],
				[
					43,
					0
				],
				[
					48,
					0
				],
				[
					53,
					0
				],
				[
					60,
					-1
				],
				[
					64,
					-1
				],
				[
					68,
					-1
				],
				[
					69,
					-1
				],
				[
					74,
					-1
				],
				[
					75,
					-1
				],
				[
					77,
					-1
				],
				[
					79,
					-1
				],
				[
					80,
					-2
				],
				[
					82,
					-2
				],
				[
					83,
					-2
				],
				[
					84,
					-2
				],
				[
					85,
					-2
				],
				[
					86,
					-2
				],
				[
					86,
					-2
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 243,
			"versionNonce": 619805129,
			"isDeleted": false,
			"id": "AtjCb018ZidleVlSzgeAp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -377.16666666666697,
			"y": 1040.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 100,
			"height": 0,
			"seed": 1685628183,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1,
					0
				],
				[
					3,
					0
				],
				[
					10,
					0
				],
				[
					19,
					0
				],
				[
					28,
					0
				],
				[
					40,
					0
				],
				[
					50,
					0
				],
				[
					57,
					0
				],
				[
					62,
					0
				],
				[
					68,
					0
				],
				[
					72,
					0
				],
				[
					76,
					0
				],
				[
					81,
					0
				],
				[
					83,
					0
				],
				[
					86,
					0
				],
				[
					88,
					0
				],
				[
					90,
					0
				],
				[
					92,
					0
				],
				[
					95,
					0
				],
				[
					96,
					0
				],
				[
					97,
					0
				],
				[
					98,
					0
				],
				[
					99,
					0
				],
				[
					100,
					0
				],
				[
					100,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 226,
			"versionNonce": 2018681671,
			"isDeleted": false,
			"id": "C5lHXOD3",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -356.16666666666697,
			"y": 955.5768229166665,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 138742585,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40000",
			"rawText": "0x40000",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40000"
		},
		{
			"type": "text",
			"version": 235,
			"versionNonce": 1712412841,
			"isDeleted": false,
			"id": "teOiJ2Lb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -353.16666666666697,
			"y": 987.0768229166666,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 2037168759,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40001",
			"rawText": "0x40001",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40001"
		},
		{
			"type": "text",
			"version": 247,
			"versionNonce": 1087152743,
			"isDeleted": false,
			"id": "oGJZjRFC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -355.16666666666697,
			"y": 1012.0768229166665,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 749440121,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40002",
			"rawText": "0x40002",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40002"
		},
		{
			"type": "text",
			"version": 248,
			"versionNonce": 2039634825,
			"isDeleted": false,
			"id": "uSYGz5Bg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -355.16666666666697,
			"y": 1046.0768229166665,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 1862030231,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40003",
			"rawText": "0x40003",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40003"
		},
		{
			"type": "freedraw",
			"version": 238,
			"versionNonce": 1677311367,
			"isDeleted": false,
			"id": "nhVKrsRl1aHAYEu3JICsW",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -375.16666666666697,
			"y": 1104.076822916666,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 115,
			"height": 4,
			"seed": 1523592375,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2,
					0
				],
				[
					13,
					0
				],
				[
					15,
					0
				],
				[
					25,
					0
				],
				[
					41,
					2
				],
				[
					55,
					3
				],
				[
					67,
					3
				],
				[
					74,
					3
				],
				[
					79,
					3
				],
				[
					87,
					4
				],
				[
					91,
					4
				],
				[
					98,
					4
				],
				[
					104,
					4
				],
				[
					106,
					4
				],
				[
					109,
					4
				],
				[
					111,
					4
				],
				[
					112,
					4
				],
				[
					114,
					4
				],
				[
					115,
					4
				],
				[
					115,
					4
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 236,
			"versionNonce": 1068499561,
			"isDeleted": false,
			"id": "1We_m9w4WfuMKSIPNKzc5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -376.16666666666697,
			"y": 1138.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 102,
			"height": 3,
			"seed": 1539206423,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					4,
					0
				],
				[
					7,
					-1
				],
				[
					15,
					-1
				],
				[
					23,
					-2
				],
				[
					32,
					-2
				],
				[
					48,
					-2
				],
				[
					59,
					-2
				],
				[
					67,
					-2
				],
				[
					76,
					-2
				],
				[
					82,
					-2
				],
				[
					84,
					-2
				],
				[
					87,
					-2
				],
				[
					92,
					-2
				],
				[
					96,
					-2
				],
				[
					99,
					-3
				],
				[
					100,
					-3
				],
				[
					102,
					-3
				],
				[
					102,
					-3
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 233,
			"versionNonce": 1427535015,
			"isDeleted": false,
			"id": "ma0wU6u-0mXSRkxYU5mX6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -375.16666666666697,
			"y": 1173.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 118,
			"height": 8,
			"seed": 1648315479,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1
				],
				[
					3,
					1
				],
				[
					9,
					1
				],
				[
					23,
					1
				],
				[
					48,
					2
				],
				[
					69,
					5
				],
				[
					81,
					7
				],
				[
					90,
					8
				],
				[
					97,
					8
				],
				[
					106,
					8
				],
				[
					111,
					8
				],
				[
					114,
					8
				],
				[
					116,
					8
				],
				[
					118,
					8
				],
				[
					118,
					8
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 233,
			"versionNonce": 87412041,
			"isDeleted": false,
			"id": "yF6LwtsJnQBUMnNGXL5Il",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -374.16666666666697,
			"y": 1214.0768229166665,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 105,
			"height": 0,
			"seed": 1918279577,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1,
					0
				],
				[
					13,
					0
				],
				[
					28,
					0
				],
				[
					46,
					0
				],
				[
					60,
					0
				],
				[
					72,
					0
				],
				[
					85,
					0
				],
				[
					90,
					0
				],
				[
					95,
					0
				],
				[
					99,
					0
				],
				[
					102,
					0
				],
				[
					103,
					0
				],
				[
					104,
					0
				],
				[
					105,
					0
				],
				[
					105,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 277,
			"versionNonce": 1808746439,
			"isDeleted": false,
			"id": "FPKeY9TL",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -353.16666666666697,
			"y": 1108.0768229166665,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 1442478969,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40005",
			"rawText": "0x40005",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40005"
		},
		{
			"type": "text",
			"version": 284,
			"versionNonce": 1904163881,
			"isDeleted": false,
			"id": "i6EYS0VC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -353.16666666666697,
			"y": 1146.0768229166665,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 2039993495,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40006",
			"rawText": "0x40006",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40006"
		},
		{
			"type": "text",
			"version": 287,
			"versionNonce": 1447081703,
			"isDeleted": false,
			"id": "7FMLy4cf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -356.16666666666697,
			"y": 1188.0768229166665,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 1810801753,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40007",
			"rawText": "0x40007",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40007"
		},
		{
			"type": "text",
			"version": 309,
			"versionNonce": 880267017,
			"isDeleted": false,
			"id": "8AWlPPRA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -356.16666666666697,
			"y": 1078.0768229166665,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 84,
			"height": 24,
			"seed": 1217870297,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "XXyCw-qBWmAXt-0vyvLpF",
					"type": "arrow"
				},
				{
					"id": "kBt4Of5wT_OtMrjtadMPy",
					"type": "arrow"
				}
			],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "0x40004",
			"rawText": "0x40004",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0x40004"
		},
		{
			"type": "text",
			"version": 687,
			"versionNonce": 1257718279,
			"isDeleted": false,
			"id": "GQAvUics",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -667.3764096939212,
			"y": 994.1956661129309,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 107,
			"height": 24,
			"seed": 1890227415,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "arrays[0]",
			"rawText": "arrays[0]",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "arrays[0]"
		},
		{
			"type": "text",
			"version": 724,
			"versionNonce": 1956316649,
			"isDeleted": false,
			"id": "mLScPP6g",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -659.1981366456457,
			"y": 1114.4569741142432,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 107,
			"height": 24,
			"seed": 1749190583,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "arrays[1]",
			"rawText": "arrays[1]",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "arrays[1]"
		},
		{
			"type": "text",
			"version": 723,
			"versionNonce": 2062510375,
			"isDeleted": false,
			"id": "Bnmaxe9j",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -657.6322128847255,
			"y": 1239.137999567772,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 107,
			"height": 24,
			"seed": 416559929,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596554,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "arrays[2]",
			"rawText": "arrays[2]",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "arrays[2]"
		},
		{
			"type": "text",
			"version": 727,
			"versionNonce": 2096390345,
			"isDeleted": false,
			"id": "7eoTX2Gm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -715.326152176541,
			"y": 901.4293933380811,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 295,
			"height": 24,
			"seed": 817587575,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "arrays[3] = {20, 50, 35};",
			"rawText": "arrays[3] = {20, 50, 35};",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "arrays[3] = {20, 50, 35};"
		},
		{
			"type": "text",
			"version": 1140,
			"versionNonce": 1133882439,
			"isDeleted": false,
			"id": "XpbJXu0j",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -87.25373711438442,
			"y": 958.7320848507372,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 295,
			"height": 48,
			"seed": 569692345,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "1al4mCb_6MNRlotBOBVe9",
					"type": "arrow"
				}
			],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"fontSize": 20.097311943588505,
			"fontFamily": 3,
			"text": "printf(\"%p\", &arrays[0]);\nprintf(\"%p\", arrays);",
			"rawText": "printf(\"%p\", &arrays[0]);\nprintf(\"%p\", arrays);",
			"baseline": 43,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "printf(\"%p\", &arrays[0]);\nprintf(\"%p\", arrays);"
		},
		{
			"type": "text",
			"version": 369,
			"versionNonce": 723476393,
			"isDeleted": false,
			"id": "cymedq3y",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -114.35888874198713,
			"y": 1134.3372364783395,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 295,
			"height": 24,
			"seed": 110558233,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "XXyCw-qBWmAXt-0vyvLpF",
					"type": "arrow"
				}
			],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "printf(\"%p\", &arrays[1]);",
			"rawText": "printf(\"%p\", &arrays[1]);",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "printf(\"%p\", &arrays[1]);"
		},
		{
			"type": "arrow",
			"version": 756,
			"versionNonce": 549882727,
			"isDeleted": false,
			"id": "XXyCw-qBWmAXt-0vyvLpF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -107.73992189260002,
			"y": 1124.7325476461542,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 153.43349614136037,
			"height": 30.396430084093026,
			"seed": 967232919,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "cymedq3y",
				"focus": -0.15295607662810778,
				"gap": 9.604688832185275
			},
			"endBinding": {
				"elementId": "8AWlPPRA",
				"focus": -0.30703417069324884,
				"gap": 10.993248632706582
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
					-153.43349614136037,
					-30.396430084093026
				]
			]
		},
		{
			"type": "arrow",
			"version": 686,
			"versionNonce": 491225737,
			"isDeleted": false,
			"id": "1al4mCb_6MNRlotBOBVe9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -96.52160948221444,
			"y": 963.5106745086256,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 159.16341493335426,
			"height": 3.430556608772889,
			"seed": 1892503161,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "XpbJXu0j",
				"focus": 0.8315315212269885,
				"gap": 9.267872367830023
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-159.16341493335426,
					3.430556608772889
				]
			]
		},
		{
			"type": "text",
			"version": 464,
			"versionNonce": 1590593159,
			"isDeleted": false,
			"id": "ar2HMtrf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -102.6954738086331,
			"y": 1050.9881194392497,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 272,
			"height": 24,
			"seed": 332065303,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "XXyCw-qBWmAXt-0vyvLpF",
					"type": "arrow"
				},
				{
					"id": "kBt4Of5wT_OtMrjtadMPy",
					"type": "arrow"
				},
				{
					"id": "10DUc1jkRrJc3Jky1FwDR",
					"type": "arrow"
				}
			],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "printf(\"%p\", arrays+1);",
			"rawText": "printf(\"%p\", arrays+1);",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "printf(\"%p\", arrays+1);"
		},
		{
			"type": "arrow",
			"version": 688,
			"versionNonce": 539511145,
			"isDeleted": false,
			"id": "kBt4Of5wT_OtMrjtadMPy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -112.9867903373895,
			"y": 1064.3602178438477,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 145.44243088737494,
			"height": 23.325672878163914,
			"seed": 369267161,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ar2HMtrf",
				"focus": 0.6533230887559881,
				"gap": 10.291316528756397
			},
			"endBinding": {
				"elementId": "8AWlPPRA",
				"focus": 0.3494953473710621,
				"gap": 13.737445441902537
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
					-145.44243088737494,
					23.325672878163914
				]
			]
		},
		{
			"type": "arrow",
			"version": 715,
			"versionNonce": 208280999,
			"isDeleted": false,
			"id": "10DUc1jkRrJc3Jky1FwDR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -226.87095791901334,
			"y": 842.0802762989915,
			"strokeColor": "#5f3dc4",
			"backgroundColor": "transparent",
			"width": 311.4663378437185,
			"height": 196.21007185749664,
			"seed": 1125176249,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "HdjWrQ2I",
				"focus": -0.44498253983925534,
				"gap": 8.92220871106565
			},
			"endBinding": {
				"elementId": "ar2HMtrf",
				"focus": 0.5836634568398993,
				"gap": 12.69777128276155
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
					311.4663378437185,
					196.21007185749664
				]
			]
		},
		{
			"type": "rectangle",
			"version": 273,
			"versionNonce": 1561146441,
			"isDeleted": false,
			"id": "N_ignF0dKJhQZtjKNRzPj",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -785.3150085903501,
			"y": 757.0101752139229,
			"strokeColor": "#5f3dc4",
			"backgroundColor": "transparent",
			"width": 1023.5854098300179,
			"height": 624.3047740920349,
			"seed": 685545239,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [
				{
					"id": "9ySmmU43ucR4LGMJGv71T",
					"type": "arrow"
				}
			],
			"updated": 1666281596555,
			"link": null,
			"locked": false
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 751161543,
			"isDeleted": false,
			"id": "GFjvfqWG0BhnrATOfSLt0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -519.698132713499,
			"y": 955.7525267363123,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 26.666666666666742,
			"height": 106.66666666666652,
			"seed": 580045415,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.6666666666667425,
					-1.6666666666667425
				],
				[
					-3.333333333333485,
					-1.6666666666667425
				],
				[
					-5,
					-1.6666666666667425
				],
				[
					-5,
					0
				],
				[
					-10,
					5
				],
				[
					-13.333333333333485,
					6.666666666666629
				],
				[
					-15,
					6.666666666666629
				],
				[
					-15,
					8.333333333333258
				],
				[
					-16.666666666666742,
					10
				],
				[
					-18.333333333333485,
					11.666666666666629
				],
				[
					-18.333333333333485,
					13.333333333333258
				],
				[
					-20,
					15
				],
				[
					-20,
					18.333333333333258
				],
				[
					-20,
					20
				],
				[
					-20,
					23.333333333333258
				],
				[
					-20,
					25
				],
				[
					-20,
					26.66666666666663
				],
				[
					-20,
					28.333333333333258
				],
				[
					-20,
					30
				],
				[
					-20,
					31.66666666666663
				],
				[
					-20,
					35
				],
				[
					-20,
					36.66666666666663
				],
				[
					-20,
					38.33333333333326
				],
				[
					-20,
					40
				],
				[
					-18.333333333333485,
					41.66666666666663
				],
				[
					-18.333333333333485,
					43.33333333333326
				],
				[
					-18.333333333333485,
					45
				],
				[
					-20,
					46.66666666666663
				],
				[
					-21.666666666666742,
					46.66666666666663
				],
				[
					-23.333333333333485,
					46.66666666666663
				],
				[
					-25,
					46.66666666666663
				],
				[
					-26.666666666666742,
					46.66666666666663
				],
				[
					-26.666666666666742,
					48.33333333333326
				],
				[
					-25,
					50
				],
				[
					-25,
					51.66666666666663
				],
				[
					-23.333333333333485,
					53.33333333333326
				],
				[
					-21.666666666666742,
					55
				],
				[
					-21.666666666666742,
					56.66666666666663
				],
				[
					-20,
					56.66666666666663
				],
				[
					-20,
					58.33333333333326
				],
				[
					-20,
					59.999999999999886
				],
				[
					-20,
					61.66666666666663
				],
				[
					-20,
					63.33333333333337
				],
				[
					-20,
					64.99999999999989
				],
				[
					-20,
					66.66666666666663
				],
				[
					-20,
					68.33333333333326
				],
				[
					-20,
					69.99999999999977
				],
				[
					-20,
					73.33333333333326
				],
				[
					-20,
					74.99999999999977
				],
				[
					-21.666666666666742,
					76.66666666666674
				],
				[
					-21.666666666666742,
					78.33333333333326
				],
				[
					-21.666666666666742,
					79.99999999999977
				],
				[
					-21.666666666666742,
					81.66666666666674
				],
				[
					-21.666666666666742,
					83.33333333333326
				],
				[
					-21.666666666666742,
					86.66666666666674
				],
				[
					-21.666666666666742,
					89.99999999999977
				],
				[
					-21.666666666666742,
					91.66666666666674
				],
				[
					-21.666666666666742,
					93.33333333333326
				],
				[
					-21.666666666666742,
					94.99999999999977
				],
				[
					-21.666666666666742,
					96.66666666666674
				],
				[
					-20,
					98.33333333333326
				],
				[
					-18.333333333333485,
					99.99999999999977
				],
				[
					-16.666666666666742,
					99.99999999999977
				],
				[
					-15,
					99.99999999999977
				],
				[
					-13.333333333333485,
					99.99999999999977
				],
				[
					-10,
					99.99999999999977
				],
				[
					-8.333333333333485,
					101.66666666666674
				],
				[
					-6.6666666666667425,
					103.33333333333326
				],
				[
					-5,
					103.33333333333326
				],
				[
					-3.333333333333485,
					104.99999999999977
				],
				[
					-3.333333333333485,
					104.99999999999977
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "arrow",
			"version": 57,
			"versionNonce": 1204929321,
			"isDeleted": false,
			"id": "ddmVb9RZhorVbBEEgCz1R",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -729.6981327134991,
			"y": 1234.0858600696456,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 181.66666666666663,
			"height": 191.66666666666652,
			"seed": 920175369,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "round",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					181.66666666666663,
					-191.66666666666652
				]
			]
		},
		{
			"type": "text",
			"version": 21,
			"versionNonce": 696131559,
			"isDeleted": false,
			"id": "r90yDXLU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -763.0314660468324,
			"y": 1264.5858600696456,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 178,
			"height": 24,
			"seed": 988156519,
			"groupIds": [
				"5J6WiqZ15YOu8MFBoKP0d",
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "sizeof(int) = 4",
			"rawText": "sizeof(int) = 4",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "sizeof(int) = 4"
		},
		{
			"id": "5KuiI4vy",
			"type": "text",
			"x": -217.34906635674952,
			"y": 1289.6809121529789,
			"width": 318,
			"height": 24,
			"angle": 0,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"isZivEgN6ZO63FUYy2TiH"
			],
			"strokeSharpness": "sharp",
			"seed": 1482238153,
			"version": 73,
			"versionNonce": 1289844233,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1666281596555,
			"link": null,
			"locked": false,
			"text": "sizeof(arrays) = 3 * 4 = 12",
			"rawText": "sizeof(arrays) = 3 * 4 = 12",
			"fontSize": 20,
			"fontFamily": 3,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 19,
			"containerId": null,
			"originalText": "sizeof(arrays) = 3 * 4 = 12"
		},
		{
			"type": "text",
			"version": 30,
			"versionNonce": 475227399,
			"isDeleted": false,
			"id": "kzptkUYY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 718.635200619834,
			"y": 277.91919340297903,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"width": 318,
			"height": 24,
			"seed": 887284521,
			"groupIds": [
				"cxWuIUImJXZG-EJZ2Kny1"
			],
			"strokeSharpness": "sharp",
			"boundElements": [],
			"updated": 1666282062818,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "Section 4: Pointers Concept",
			"rawText": "Section 4: Pointers Concept",
			"baseline": 19,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Section 4: Pointers Concept"
		},
		{
			"id": "OPSIcvtS",
			"type": "text",
			"x": 729.317600309917,
			"y": 337.18091215297886,
			"width": 528,
			"height": 504,
			"angle": 0,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"cxWuIUImJXZG-EJZ2Kny1"
			],
			"strokeSharpness": "sharp",
			"seed": 1149220167,
			"version": 52,
			"versionNonce": 281449193,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1666282062818,
			"link": null,
			"locked": false,
			"text": "#include <stdio.h>\n\nvoid swap(int *a, int *b)\n{\n    int temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nint main()\n{\n    int a = 10;\n    int b = 20;\n\n    printf(\"Before: a = %d, b = %d\\n\", a, b);\n    swap(&a, &b);\n    printf(\"After:  a = %d, b = %d\\n\", a, b);\n\n    return 0;\n}\n",
			"rawText": "#include <stdio.h>\n\nvoid swap(int *a, int *b)\n{\n    int temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nint main()\n{\n    int a = 10;\n    int b = 20;\n\n    printf(\"Before: a = %d, b = %d\\n\", a, b);\n    swap(&a, &b);\n    printf(\"After:  a = %d, b = %d\\n\", a, b);\n\n    return 0;\n}\n",
			"fontSize": 20,
			"fontFamily": 3,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 499,
			"containerId": null,
			"originalText": "#include <stdio.h>\n\nvoid swap(int *a, int *b)\n{\n    int temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nint main()\n{\n    int a = 10;\n    int b = 20;\n\n    printf(\"Before: a = %d, b = %d\\n\", a, b);\n    swap(&a, &b);\n    printf(\"After:  a = %d, b = %d\\n\", a, b);\n\n    return 0;\n}\n"
		},
		{
			"id": "N29pRpnJIDwklAHGfOBQF",
			"type": "rectangle",
			"x": 682.6509336432505,
			"y": 250.84757881964543,
			"width": 654.6666666666667,
			"height": 635,
			"angle": 0,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"cxWuIUImJXZG-EJZ2Kny1"
			],
			"strokeSharpness": "sharp",
			"seed": 83222313,
			"version": 66,
			"versionNonce": 852438055,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1666282062818,
			"link": null,
			"locked": false
		},
		{
			"id": "owtUrdu4",
			"type": "text",
			"x": 699.492133488292,
			"y": 42.67700590297886,
			"width": 178,
			"height": 48,
			"angle": 0,
			"strokeColor": "#495057",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"strokeSharpness": "sharp",
			"seed": 1904979113,
			"version": 40,
			"versionNonce": 1093125575,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1666282219347,
			"link": null,
			"locked": false,
			"text": "void *\nGeneric pointer",
			"rawText": "void *\nGeneric pointer",
			"fontSize": 20,
			"fontFamily": 3,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 43,
			"containerId": null,
			"originalText": "void *\nGeneric pointer"
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#495057",
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
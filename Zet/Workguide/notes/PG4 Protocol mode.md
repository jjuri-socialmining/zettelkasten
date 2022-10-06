---
title: PG4 Protocol mode
created: 2022-May-27
tags:
  - 'permanent/definition'
---

Bảng protocol mode của [[Porrima Gen4|PG4]]

| Type    | Protocol mode | HSC protocol                      | PG4 Protocol                   | NOTE    |
| ------- | ------------- | --------------------------------- | ------------------------------ | ------- |
| Retimer | 4x25gN-4x25gN | HSC_MODE_100G_4Nx25p8_TO_4Nx25p8  | POR_MODE_100G_PCS4_TO_PCS4     | R       |
|         | 4x26gP-4x26gP | HSC_MODE_200G_4Px26p6_TO_4Px26p6  | POR_MODE_200G_KP4_TO_KP4       | R       |
| Gearbox | 4x25gN-2x25gP | HSC_MODE_100G_4Nx25p8_TO_2Px25p8  | POR_MODE_100G_PCS4_TO_KP2      | R       |
|         | 4x26gP-2x53gP | HSC_MODE_200G_4Px26p6_TO_2Px53p1  | POR_MODE_200G_KP4_TO_KP2       | R       |
|         | 2x26gP-1x53gP | HSC_MODE_100G_2Px26p6_TO_1Px53p1  | POR_MODE_100G_KP2_TO_KP1       | R       |
|         | 4x26gN-1x53gP | HSC_MODE_100G_4Nx26p6_TO_1Px53p1  | POR_MODE_100G_KP4_TO_KP1       | R       |
|         | 8x26gP-4x53gP | HSC_MODE_400G_8Px26p6_TO_4Px53p1  | POR_MODE_400G_KP8_TO_KP4       | GUI     |
|         | 8x26gN-4x26gP | HSC_MODE_200G_8Nx26p6_TO_4Px26p6  | POR_MODE_200G_KP8_TO_KP4       | GUI     |
| New     | 8-4           | HSC_MODE_400G_8Px27p95_TO_4Px55p9 | POR_MODE_400G_FOIC8_TO_FOIC4   | API+GUI |
|         | 8-4           | HSC_MODE_400G_8Px26p63_TO_4Px53p2 | POR_MODE_400G_FOICE8_TO_FOICE4 | API+GUI |
|         | 8-4           | HSC_MODE_400G_8Px28p1_TO_4Px56p2  | POR_MODE_400G_OTLC8_TO_OTLC4   | API+GUI |

Description tương ứng với baudrate tại đây [[Baudrate name in PG4]]

Personal notes:
- [[@2022-05-27]]
	- **R**eady in GUI Gen2
	- API+GUI: Mis on API and GUI
	- **GUI**: mis on PG4 GUI Gen2





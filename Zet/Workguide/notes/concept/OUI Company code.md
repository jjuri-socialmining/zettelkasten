---
title: OUI Company code
created: 2022-Oct-24
tags:
  - 'permanent/concept'
aliases:
  - OUI Code
  - OUI
publish: False
---

[[Inphi]]:     0x0021B8
[[Marvell]]: 0x005043

Description of [MMD08_DEVICE_ID_LOW](http://sw.inphi-corp.local:8086/browser?chip=spica5&die=0x0&name=MMD08_DEVICE_ID_LOW&preview=0x210)

```
Registers 30.2 and 30.3 provide a 32-bit value, which may constitute a unique identifier for a particular type of PMA/PMD. The identifier is composed of the 3rd through 24th bits of the Organizationally Unique Identifier (OUI) assigned to the device manufacturer by the IEEE, plus a six-bit model number, plus a four-bit revision number. OUI is 00:50:43
```

The OUI code that read from register must be converted
```c
static uint32_t oui_msb_convert(uint32_t bit3_18, uint32_t bit19_24)
{
    uint32_t val_24 = 0;
    uint32_t oui_code = 0;
    uint8_t oct, bit, bit_id;

    ODSP_FIELD_SET(&val_24, ODSP_BIT21_6, 6, bit3_18);
    ODSP_FIELD_SET(&val_24, ODSP_BIT5_0, 0, bit19_24);

    /* Example: 10.20.13 -> 08.04.C8 */
    for (oct = 0; oct < 3; oct++)
    {
        for (bit_id = 0; bit_id < 8; bit_id++)
        {
            uint32_t offset = (oct * 8) + bit_id;
            uint32_t offset_code = (oct * 8) + 7 - bit_id;
            ODSP_FIELD_GET(val_24, ODSP_BIT0 << offset, offset, uint8_t, &bit);
            ODSP_FIELD_SET(&oui_code, ODSP_BIT0 << offset_code, offset_code, bit);
        }
    }

    return oui_code;
}
```
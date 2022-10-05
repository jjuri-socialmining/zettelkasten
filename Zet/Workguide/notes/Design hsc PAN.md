# Design hsc PAN

## Option 1
```c
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

}hsc_an_pan_aware_t;
```

hsc_an_pan_oui_mask


## Reference
- [[Next page]]
- [[802.3-2015_SECTION5.pdf]] 
- [[802.3 - Clause 73]] (73.6.9)
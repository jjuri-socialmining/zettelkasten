# Gui access die 2


![](../images/2021-12-03-14-46-08.png)

![](../images/2021-12-03-14-47-37.png)
files Artemis3EVB.py

```python
def set_capella_address(self, quiet=False):
    phy = self.address_upper

    if debug:
        if not self.quiet:
            print ('Capella upper die - setting PHYAD')
    o.wr(mb=self.zeus_sn, address=0x1e0068, data=0x410, phy=phy)  #MMD30_LINE_CONFIG_01 PHYADR_01->4 BANKADR_01->0
    o.wr(mb=self.zeus_sn, address=0x1e0069, data=0x2510, phy=phy) #MMD30_LINE_CONFIG_23 PHYADR_01->5 BANKADR_01->1
    o.wr(mb=self.zeus_sn, address=0x1e006e, data=0x610, phy=phy)  #MMD30_HOST_CONFIG_01 PHYADR_01->6 BANKADR_01->0
    o.wr(mb=self.zeus_sn, address=0x1e006f, data=0x2710, phy=phy) #MMD30_HOST_CONFIG_23 PHYADR_01->7 BANKADR_01->1
```

ctc_remap.py
```python

def addr_remap_callback(die, addr):
    """This is a default callback method that is used to remap the die
       and address for CTC EVBs.
    """
    mb = die >> 16
    
    ctc_instance = 0
    if(die & 0x1000):
        ctc_instance = 1
        
    bus = 0
    
    if(ctc_instance != 0):
        cpl_base = 4
        ctc_base = 0x10
    else:
        cpl_base = 0
        ctc_base = 0

    # Core registers
    if(addr < 0x63400000):
        # prtad = 0xe + ctc_base
        prtad = 0xf + ctc_base
        devad = addr >> 16
        
    # Capella Registers
    else:
        # Host[1]
        if(addr >= 0x63460000):
            prtad = 3 + cpl_base 
            devad = 1
        # Host[0]
        elif(addr >= 0x63440000):
            prtad = 2 + cpl_base 
            devad = 0
        # Line[1]
        elif(addr >= 0x63420000):
            prtad = 1 + cpl_base 
            devad = 1
        else:
            prtad = 0 + cpl_base 
            devad = 0
          
    addr &= 0xffff
        
    #print("mb=%x, bus=%d, prtad=%x, devad=%x, addr=%x" % (mb, bus, prtad, devad, addr))
    return (mb, bus, prtad, devad, addr)
```
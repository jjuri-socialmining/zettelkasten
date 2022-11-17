o.SerialInterface(protocol='MDIO', clocktype='Normal')
o.ResetTarget()
o.ResetTarget(mb=952)
o.rd(address=0x80002)
## I2C
Host app can access Core CTC direct register via I2C. To access IP, Host app need indirect I2C to read/write IP register (I2C tunnel from Core to IP APB)

![[Pasted image 20220301134106.png]]

Lynx firmware access to Capella IP via APB I2C.

## MDIO

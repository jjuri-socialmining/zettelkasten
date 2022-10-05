---
title: ottlab bench remote reboot
created: 2022-Jun-20
tags:
  - 'permanent/howto'
---

link: https://ewiki.marvell.com/pages/viewpage.action?spaceKey=ODSP&title=Ottawa+Lab

```
User Name: admin
Password: 1234
```

The DNS has now been updated for all PC’s so you should be able to connect to them using their PC name instead of the direct IP addresses I listed earlier.

New lab setup has been documented here: [https://ewiki.marvell.com/display/ODSP/Ottawa+Lab](https://ewiki.marvell.com/display/ODSP/Ottawa+Lab)

Each shelf has a powerbar that can have individual outlets switched on or off remotely.

To remotely control the powerbars, log into the powerbar you want to access by writing it’s IP into a browser (IP’s for powerbars and their corresponding setups are found here: [https://ewiki.marvell.com/display/ODSP/Ottawa+Lab](https://ewiki.marvell.com/display/ODSP/Ottawa+Lab)).

The credentials for all powerbars are:

User Name: admin

Password: 1234

![[power.png]]
![[Pasted image 20220620114735.png]]

Once logged in you’ll be able to switch outlets on and off using the web interface.

The powerbars are named by Rack number and shelf they power.

Outlets are named by what board they are powering with a corresponding MB number.

![[Pasted image 20220620114748.png]]


Relate:
- [[How to control The Remote Power Unit RPU to reset EVB (sjclab)]]
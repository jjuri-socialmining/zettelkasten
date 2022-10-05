
---
title: Change app in cygwin
created: 2021-Dec-24
tags:
  - 'permanent/howto'
---

Change default a version of application in [[Cygwin]]

Example
Current verion of python is python3.8 and you want to change to 2.7

```
$ ls -l python
lrwxrwxrwx 1 dutran Domain Users 18 Dec 24 10:59 python -> /usr/bin/python3.8
$cd /usr/bin
$ls -a 
...
 cyggcrypt-20.dll                     cygwrap-0.dll                            python
 cyggdbm_compat-4.dll                 cygX11-6.dll                             python2
 cyggdbm-4.dll                        cygX11-xcb-1.dll                         python2.7.exe
 cyggdbm-6.dll                        cygXau-6.dll                             python2.7-config
 cyggdk_pixbuf-2.0-0.dll              cygXaw-7.dll                             python2-config
 cyggdk-3-0.dll                       cygxcb-1.dll                             python3
 cyggdk-x11-2.0-0.dll                 cygxcb-composite-0.dll                   python3.8.exe
...
$rm -r python
$ln -s /usr/bin/python2.7 python
```

```
$ ls -l python
lrwxrwxrwx 1 dutran Domain Users 18 Dec 24 10:55 python -> /usr/bin/python2.7

$ ls -l | grep "python ->"
lrwxrwxrwx    1 XXXX Domain Users       XXXXX python -> /usr/bin/python2.7

$ python
Python 2.7.18 (default, Jan  2 2021, 09:22:32)
[GCC 10.2.0] on cygwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
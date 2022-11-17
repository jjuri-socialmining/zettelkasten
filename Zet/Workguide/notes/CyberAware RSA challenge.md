---
title: CyberAware RSA challenge
created: 2022-Nov-04
tags:
  - 'permanent/common'
publish: False
---

calculate modulus n and e from public key
```shell
openssl rsa -pubin -in key.pem -text -noout
```

```shell
$ openssl rsa -pubin -in key.pem -text -noout
RSA Public-Key: (2047 bit)
Modulus:
    40:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:00:00:1c:a2:23:4d:85:71:5f:e9:1e:59:
    cf:d6:a3:be:cb:36:21:bd:f0:44:d6:df:4d:c4:83:
    6d:06:95:99:5e:db:14:36:bc:14:cd:4f:5a:97:e1:
    12:5d:6d:0b:4b:71:8e:83:29:31:97:2b:e0:de:e4:
    6a:06:54:e3:78:86:69:65:00:00:03:33:dd:9d:90:
    26:d7:59:52:6f:78:26:6c:61:78:8e:68:c2:ef:c0:
    42:52:df:77:97:25:30:e2:66:54:8e:2b:f2:9e:04:
    2c:50:a8:92:32:e4:17:85:33:2f:12:85:41:76:4c:
    ef:be:be:1f:ab:81:c8:8c:cb:ae:ec:84:0d:5e:f0:
    7c:6e:c7:af:da:a8:2b:55:88:89:4c:e6:af:da:28:
    c5:68:e2:b9:06:24:8e:cd:26:a7:a9:30:98:cb:57:
    50:07:f9:68:3c:7c:a2:11:05:22:17:e1:e8:e3:d5:
    1f:cc:5b:14:34:32:48:f0:e4:f9:89:1c:86:71:eb:
    c9
Exponent: 65537 (0x10001)
```


```

```

![[CyberAware RSA challenge 2022-11-05 00.54.48.excalidraw]]
---
title: All usefull command for spicap
created: 2022-Jun-23
tags:
  - 'permanent/common'
---


# Make source code

```shell
make legacy PROJECT_PREFIX=spicap PRODUCTS=spicap
```

## Unittest

OLYMPUS
```shell
make target=olympus -C tests PROJECT_PREFIX=spicap PRODUCTS=spicap
```

XMLRPC
```shell
make target=xmlrpc -C tests PROJECT_PREFIX=spicap PRODUCTS=spicap
```

RUN simulate
```shell
build-output/tests/tests.exe --ip 127.0.0.1 --port 2632 --product lynx --testcases version,test_dev,test_all_gpios,test_all_eeproms,test_tx_rules,test_rx_rules
```

```shell
build-output/tests/tests.exe --ip 127.0.0.1 --port 60008 --product spicap --testcases all
```

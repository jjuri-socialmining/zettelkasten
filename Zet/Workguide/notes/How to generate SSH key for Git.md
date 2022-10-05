---
title: How to generate SSH key for Git
created: 2022-May-23
tags:
  - 'permanent/howto'
---

run command
```shell
ssh-keygen -t rsa -b 2048 -C "dutran@marvell.com"
```

copy key
```shell
cat /home/dutran/.ssh/id_rsa.pub
```

paste to git server


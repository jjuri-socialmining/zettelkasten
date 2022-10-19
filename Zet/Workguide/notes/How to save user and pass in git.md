---
title: How to save user and pass in git
created: 2022-May-19
tags:
  - 'permanent/howto'
---
up:: [[Git-SCM]]

This method saves the credentials in **plaintext** on your PC's disk, it may access by everyone.

```shell
git config --global credential.helper store
git pull
```





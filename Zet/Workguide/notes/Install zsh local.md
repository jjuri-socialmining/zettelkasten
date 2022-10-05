---
title: Install zsh local
created: 2022-Sep-22
tags:
  - 'permanent/howto'
---
up::[[Compile linux source]]

Download zsh with:

```bash
wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
mkdir zsh && unxz zsh.tar.xz && tar -xvf zsh.tar -C zsh --strip-components 1
cd zsh
```

You can compile zsh yourself, for example:

```bash
./configure --prefix=$HOME
make
make install
```
and then start it explicitly, or programmatically from your current shell's startup file (put `exec $HOME/bin/zsh -l` in the right spot).

## Source
- https://stackoverflow.com/questions/15293406/install-zsh-without-root-access
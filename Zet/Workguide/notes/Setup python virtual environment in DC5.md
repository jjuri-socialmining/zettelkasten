---
title: Setup python virtual environment in DC5
created: 2022-Sep-22
tags:
  - 'permanent/howto'
---

up::[[Python virtual environment]]

```bash
mkdir ~/python3_venv
cd ~/python3_venv

virtualenv -p /tools/cad/python3.9.12/bin/python3.9 venv
```

## Activate 

```bash
source ~/python3_venv/venv/bin/activate.csh
```

if the error happen
```
bash-4.2$ source venv/bin/activate.csh
bash: alias: deactivate: not found
bash: alias: `test $?_OLD_VIRTUAL_PATH !': invalid alias name
bash: deactivate: command not found
bash: setenv: command not found
bash: setenv: command not found
bash: venv/bin/activate.csh: line 37: syntax error: unexpected end of file
```

Try command below:
```
csh venv/bin/activate.csh
```
---
title: Linux command to show folder structure
created: 2022-Nov-07
tags:
  - 'permanent/common'
publish: False
---
`-d` show directory only
`-L level`: Show upto level 

```
bash-4.2$ tree -d -L 4
.
|-- bin
|   `-- swig
|-- build-output
|   |-- amalgamated
|   |   |-- platform
|   |   |   |-- inc
|   |   |   `-- src
|   |   `-- products
|   |       `-- lynx
|   |-- docs
|   |   |-- license
|   |   `-- user_guide
|   |-- events
|   |-- examples
|   |   |-- debug
|   |   |   |-- hmux
|   |   |   `-- ip
|   |   |-- diagnostics
|   |   |-- initialization
|   |   |-- olympus
|   |   |   `-- lib
|   |   |-- products
|   |   |   |-- ctc3
|   |   |   `-- lynx
|   |   `-- py
|   |       |-- ctc3
|   |       |-- lynx
|   |       |-- lynx_400
|   |       |-- part_screening
```

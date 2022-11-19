---
title: Setup vscode for development C
tags:
  - 'created/2022/Oct/29'
  - 'tasks/done'
is_done: True
---
## Notes:
1. Install [[Visual Studio Code]]
2. Install [[Cygwin]] or [[Mingwin]]
3. Install `C/C++` and `Code Runner` vscode Plugin

## Common issues:
---
1. Could not find source file when run debuging

![[20221029215549 ~ c vscode debuging could not find source file.png]]

Reason: due to Cygwin do not use mapping like window, so it mapping path
![[20221029215849.png]]
instead of `c:/Users/...`

Solution: update `.vscode\launch.json`, add attribute `sourceFileMap` to convert cygwin maping to window mapping file

```
{
  "version": "0.2.0",
  "configurations": [
  
    {
      "name": "C/C++ Runner: Debug Session",
      "type": "cppdbg",
      "request": "launch",
      "args": [],
      "stopAtEntry": true,
      "externalConsole": true,
      "cwd": "${workspaceFolder}",
      "sourceFileMap": { "c:/cygwin64/bin/C/": "c:\\" },
      "program": "c:/Users/ADMIN/workspace/c_projects/assert.exe",
      "MIMode": "gdb",
      "miDebuggerPath": "C:/cygwin64/bin/gdb.exe",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ]
    }
  ]
}
```
See more [[launch.json file]]

---

## Subtask:
- [ ] [[$ 221029 - Khi run debug c trên vscode, có các field CPU, Segs, FPU, SSE. Các field này là gì 🔎]] #tasks/todo 
- [ ] [[$ 221029 - Mô tả cách gdb hoạt động để debug trên code c 🔎]] #tasks/todo 
- [ ] [[$ 221029 - Để debug python thì dùng tool gì, và setup ntn 🔎]] #tasks/todo 



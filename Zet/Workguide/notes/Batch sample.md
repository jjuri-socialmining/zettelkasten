---
title: Batch sample
created: 2022-Nov-03
tags:
  - 'permanent/common'
publish: False
---

- start vscode to browse folder `C:\Users\dutran\`
```batch
start /d "C:\Users\dutran\AppData\Local\Programs\Microsoft VS Code" code.exe "C:\Users\dutran\"
```

- find python and run
```batch
where python > list.txt
set /p texte=< list.txt  

%texte% hello.py
```

- [[Comment in batch script]]


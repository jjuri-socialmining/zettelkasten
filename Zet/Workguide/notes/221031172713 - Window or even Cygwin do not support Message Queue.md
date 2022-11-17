---
title: Window or even Cygwin do not support Message Queue
UID: 221031172713
created: 31-Oct-2022
tags:
  - 'created/2022/Oct/31'
  - 'evergreen'
  - 'permanent/fact'
aliases: '221031172713'
publish: False
---
## Notes:
Window or even [[index/Cygwin]] do not support [[Message Queue]]

When trying to run on Cygwin with below code
```c
   if ((msqid = msgget(key, PERMS | IPC_CREAT)) == -1) {
      perror("msgget");
      exit(1);
   }
```

The error below will be print out
```
$ ./send.exe 
msgget: Function not implemented
```

source:: https://stackoverflow.com/questions/47582180/creating-a-message-queue-using-msgget-in-linux-in-a-c-file-receiving-function-n
## Relate:
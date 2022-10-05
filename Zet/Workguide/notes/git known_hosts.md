---
title: git known_hosts
created: 2022-Jun-14
tags:
  - 'permanent/fact'
---

```
$ git clone git@las-gitlab:hsc/capi.git
Cloning into 'capi'...
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:0ap1MVq08aYkUpyl9xXwDXZl54lmYInH6oI7qfgCkzk.
Please contact your system administrator.
Add correct host key in /c/Users/dutran/.ssh/known_hosts to get rid of this message.
Offending RSA key in /c/Users/dutran/.ssh/known_hosts:1
RSA host key for las-gitlab has changed and you have requested strict checking.
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Clear /c/Users/dutran/.ssh/known_hosts, then fetch, clone again
```
$ git fetch
The authenticity of host 'las-gitlab (10.69.84.60)' can't be established.
ECDSA key fingerprint is SHA256:yveyXedp3FnERhHNyN6umKNBES3sUcItg/3ok7+OUNo.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'las-gitlab,10.69.84.60' (ECDSA) to the list of known hosts.
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 11 (delta 7), reused 4 (delta 0), pack-reused 0
Unpacking objects: 100% (11/11), done.
From las-gitlab:hsc/capi
 * [new branch]        users/ldinh/api_universal_1mcu -> origin/users/ldinh/api_universal_1mcu
   96acb477..5b432071  users/thuongtran/unittest_lynx -> origin/users/thuongtran/unittest_lynx
```


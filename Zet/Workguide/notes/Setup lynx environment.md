# Lynx setup environment

Add ssh key on gitlab
```
ssh-keygen -t rsa -b 2048 -C "dutran@marvell.com"
cat /user/dutran/.ssh/id_rsa.pub
```

Clone project
```bash
git clone git@las-gitlab:hsc/lynx.git
cd lynx/
git submodule init
git submodule update
```
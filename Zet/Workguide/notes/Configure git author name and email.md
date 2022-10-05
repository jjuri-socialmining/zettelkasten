---
title: Configure git author name and email
created: 2022-Jul-18
tags:
  - 'permanent/howto'
---

### To set your global username/email configuration:
1.  Open the command line.
2.  Set your username:
	```
	git config --global user.name "FIRST_NAME LAST_NAME"
	```
3.  Set your email address:  
	```
	git config --global user.email "MY_NAME@example.com"
	```

### To set repository-specific username/email configuration:
1.  From the command line, change into the repository directory.
2.  Set your username:
	```
    git config user.name "FIRST_NAME LAST_NAME"
	```
3.  Set your email address:  
	```
    git config user.email "MY_NAME@example.com"
	```
1.  Verify your configuration by displaying your configuration file:  
	```
    cat .git/config
	```

```
git config user.name "Dung Tran"
git config user.email "dutran@marvell.com"
```

## Relate:
- [[Git commit with author info]]
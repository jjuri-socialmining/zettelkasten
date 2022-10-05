---
title: How to add new product to register browser
tags:
  - 'tasks/done'
start: 2022-05-11
end: 2022-05-11
---

- Task
	- https://essjira.marvell.com/browse/RETCSW-105
	- http://dc5lp-vlas-reg-01/reg?db=/home/cnguyen/public_html/ctc_reg.db
	- http://sw.inphi-corp.local:8086/


- Guide
	- https://sw.inphi-corp.local/bookstack/books/infrastructure/page/register-web-browser

- Step by step
	- Clone repo `git clone git@las-gitlab:hsc/inf/register_web_browser.git`

	- register db download at
		- http://sw/~cnguyen/
		- http://dc5lp-vlas-sw-01/~cnguyen/

	- Create new folder and copy ctc_reg.db

	- install `sqlite3` on cygwin or modify `settings.py` to point to `sqlite3` local of repo
		![[Pasted image 20220428164550.png]]

	- Dev and run on localhost

	- Push master branch then received successful build
		![[Pasted image 20220428173253.png]]
		![[Pasted image 20220428173518.png]]
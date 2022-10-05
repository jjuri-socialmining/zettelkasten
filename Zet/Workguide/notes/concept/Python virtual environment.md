---
title: Python virtual environment
created: 2022-Sep-22
tags:
  - 'permanent/concept'
aliases:
  - virtual environment
---


# Creation of Python virtual environments

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. 
This is useful when we are working on an environment where we don't have right to install required python dependencies (DC5 chamber), a virtual environment allows us to install everything we need.
You can ignore this part if you are working on a personal environment like Cygwin as you have full permission in your own environment. 

## Create a virtual environment

```bash
mkdir ~/python2_venv
cd ~/python2_venv

virtualenv -p /tools/cad/python2.7/bin/python2.7 venv

```

## Activate 

Now after creating virtual environment, you need to activate it. Remember to activate the relevant virtual environment every time you work on the project. This can be done using the following command:

```bash
source ~/python2_venv/venv/bin/activate.csh
```

Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal. This will let you know that the virtual environment is currently active. In the image below, venv named virtual environment is active.
Now you can install dependencies related to the project in this virtual environment.




### Personal
- [ ] [[Setup python virtual environment in DC5]]
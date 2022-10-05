---
title: Indexing in Eclipse IDE
created: 2022-May-18
tags:
  - 'permanent/howto'
---

up:: [[Cygwin]], [[Eclipse IDE|Eclipse]]

1. Solution 1: Tell Eclipse to cygwin gcc tool chain

After installed Cygwin, Add cygwin path to windown PATH variable.
C:/cygwin/bin

Open eclipse then import project, [[Eclipse IDE]] will detect cygwin toolchain, select the `Cygwin GCC` toolchain -> Finish

![[Pasted image 20220518184116.png]]

After that, Eclipse will auto include path of that tool chain as below:

![[Pasted image 20220518184422.png]]

2. Solution 2: Workaround

Tell Eclipse the Include path of gcc cygwin by manual add include path + define.

![[Pasted image 20220518180315.png]]

Add some define for resolving `uintxx_t`
![[Pasted image 20220518180223.png]]

Can use this to include, define some specific macro for your project.

- Related:
	- [[Show all predefined macros of compiler]]
---
title: 'Advanced C Programming Course'
UID: 221020225233
tags:
  - 'created/2022/Oct/20'
  - 'source/video'
aliases:
  - Udemy - Advanced C Programming
publish: False
---
- metadata:
	- url:: https://marvell.udemy.com/course/advanced-c-programming-course/learn/lecture/17961842#overview
	- author:: [[Jason Fedin]]
	- category::


[[221021222506.excalidraw - Advanced C Programming Course]]

- [[221021225051 - Posix thread and C11 Threads]]
- [[221021225342 - Posix Thread is also called pthread]]
- [[221021225500 - C11 thread is in threads.h library]]
- [[221021230607 - C99 không được sử dụng phổ biến, nhiều compiler không hỗ trợ chuẩn C99]]
- [[221021230816 - C89 là chuẩn phổ biến trong ngôn ngữ C]]
- [[221021231044 - C99 hỗ trợ thêm comment in 1 line]]
- [[221021231204 - C99 hỗ trợ thêm inline function]]
- [[221021231451 - C99 cho phép khai báo biến idx trong vòng for]]
- [[221021231734 - C11 hỗ trợ multithreadings]]
- [[221021231856 - C11 focus on compatibility with C++]]
- [[Cygwin]] is environment install compiler

IDE recommend in this course
- [[Visual Studio Code]]
- [[xcode]]
- [[CodeLite]]
- 

- [[makefiles]]


- [[Storage Class]]
	- [[Auto Variable]]
		- [[221021235502 - Cú pháp khai báo biến nâng cao trong C]]
	- [[External Variable]]
	- [[Static Variable]]
		- [[221022000715 - Static Variable is alloacated on the heap]]
	- [[Register]]
	- [[221022200624 - Quiz of Storage Class]]
- Section 7: Type Qualifier
	- Const -> Just assign value when declare variable
	- [[221022202021 - Advanced usecases of const keyword in C]]
	- [[Volatile Type Qualifier]]
	- [[Restrict Type Qualifier]]

- Section 9: Advanced Control Flow
	- Program Counter?
	- setjmp/longjmp in setjmp.h

- Union
	- Union giống struct ngoại trừ đặc điểm là size của union là member có size lớn nhất trong union đó -> tiết kiệm memory.
	- Một lầ truy xuất chỉ truy xuất được 1 member tại 1 thời điểm
	- Sử dụng union như một dạng dữ liệu đa hình, có thể là int/float/...
- IPC
	- 2 types of process
		- Independent process: not affected/interact by/with another processes
		- Co-operating process: affected by other processes
	- IPC make processes work together
	- 2 communication types
		- Parent child
		- 2 different processes
		- [[221025230213 - 2 process có thể giao tiếp với nhau bằng nhiều cách thức]]
	- [[💥 How to send a signal to executed process from terminal]]

- Section 18: Useful library
	- assert.h
	- 


[[❔221022-2028 - Điều khác biệt lớn nhất giữa C11 và C99 là gì]]
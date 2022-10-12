[[Udemy]]

# Linux POSIX Threads ( Pthreads ), thread Synchronization, Operating System Concepts, C/C++ programming with Projects

## Section 1: 
- Process has atleast 1 thread, this is called main thread.
- Thread can create other threads

10. Resource sharing
![[Pasted image 20220414213041.png]]

11. Thread Stack
![[Pasted image 20220414213315.png]]


12. Schedulable

- Kernel OS do not schedule process, It schedules threads
- Thread segfault -> process terminate
- Signal send from OS per process, not per thread


## Section 2: Concurrency Vs Parallelism

Concurrency

- One at a time
- switching tasks

Parallelism


Singularism

- Doing two or more differen tasks
	- One task at a time
	- Do not pause until finish


![[Pasted image 20220414214711.png]]

-> Why we use Concurrency? It is worst than Singularism

- Concurrency do not provide speed, it provide progress
- Parrallelism provide speed, but require hardware resource.


Google: why process switching is slower than thread switching?


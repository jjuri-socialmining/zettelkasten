
source:: [[@ aosabook.org, The Architecture of Open Source Applications (Volume 2) GDB]]

> At the largest scale, GDB can be said to have two sides to it:

The "symbol side" is concerned with symbolic information about the program. Symbolic information includes function and variable names and types, line numbers, machine register usage, and so on. The symbol side extracts symbolic information from the program's executable file, parses expressions, finds the memory address of a given line number, lists source code, and in general works with the program as the programmer wrote it.
The "target side" is concerned with the manipulation of the target system. It has facilities to start and stop the program, to read memory and registers, to modify them, to catch signals, and so on. The specifics of how this is done can vary drastically between systems; most Unix-type systems provide a special system call named ptrace that gives one process the ability to read and write the state of a different process. Thus, GDB's target side is mostly about making ptrace calls and interpreting the results. For cross-debugging an embedded system, however, the target side constructs message packets to send over a wire, and waits for response packets in return.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) at [[2022-10-30]].

---

> Thus, GDB's target side is mostly about making ptrace calls and interpreting the results,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) at [[2022-10-30]].

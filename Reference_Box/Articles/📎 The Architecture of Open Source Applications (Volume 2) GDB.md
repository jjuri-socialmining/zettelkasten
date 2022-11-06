source:: [[@ aosabook.org, The Architecture of Open Source Applications (Volume 2) GDB]]

> At the largest scale, GDB can be said to have two sides to it:

The "symbol side" is concerned with symbolic information about the program. Symbolic information includes function and variable names and types, line numbers, machine register usage, and so on. The symbol side extracts symbolic information from the program's executable file, parses expressions, finds the memory address of a given line number, lists source code, and in general works with the program as the programmer wrote it.
The "target side" is concerned with the manipulation of the target system. It has facilities to start and stop the program, to read memory and registers, to modify them, to catch signals, and so on. The specifics of how this is done can vary drastically between systems; most Unix-type systems provide a special system call named ptrace that gives one process the ability to read and write the state of a different process. Thus, GDB's target side is mostly about making ptrace calls and interpreting the results. For cross-debugging an embedded system, however, the target side constructs message packets to send over a wire, and waits for response packets in return.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-10-30]].

---

> Thus, GDB's target side is mostly about making ptrace calls and interpreting the results,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-10-30]].

---

> GDB is designed to be a symbolic debugger for programs written in compiled imperative languages such as C, C++, Ada, and Fortran,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> GDB also needs to be able to debug programs compiled by different compilers (not just the GNU C compiler), to debug programs compiled years earlier by long-obsolete versions of compilers, and to debug programs whose symbolic info is missing, out of date, or simply incorrect; so, another design consideration is that GDB should continue to work and be useful even if data about the program is missing, or corrupted, or simply incomprehensible.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> GDB is an old program. It came into existence around 1985, written by Richard Stallman along with GCC, GNU Emacs, and other early components of GNU,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> today nearly all GNU tools and many (if not most) Unix programs use autoconf-generated configure scripts.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> "Host" definitions are for the machine that GDB itself runs on, and might include things like the sizes of the host's integer types.,

> "Target" definitions are specific to the machine running the program being debugged,

> If the target is the same as the host, then we are doing "native" debugging, otherwise it is "cross" debugging,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> As GDB is a C program, these are implemented as structs rather than as C++-style objects, but in most cases they are treated as objects, and here we follow GDBers' frequent practice in calling them objects.,

Thực tế GDB được tạo ra trên nền [[C Programming|Ngôn ngữ C]], nên dữ liệu nó được khai báo dưới dạng các `struct` chứ không phải là `object` như trong [[C++ Programming|C++]], tuy nhiên, các GDB guy thì vẫn gọi chúng là object.

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> GDB assigns a small positive integer to the breakpoint object, which the user subsequently uses to operate on the breakpoint.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> GDB assigns a small positive integer to the breakpoint object, which the user subsequently uses to operate on the breakpoint. Within GDB, the breakpoint is a C struct with a number of fields.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> Several kinds of breakpoint-like objects actually share the breakpoint struct, including watchpoints, catchpoints, and tracepoints.,

- [ ] [[$ 221106 - chức năng các point trong gdb như breakpoint, watchpoint, catchpoint, tracepoint là gì🔎]] #tasks/todo 

- [[gdb breakpoint]]
- [[gdb watchpoint]]
- [[gdb catchpoint]]
- [[gdb tracepoint]]

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> Symbol tables are a key data structure to GDB, and can be quite large, sometimes growing to occupy multiple gigabytes of RAM,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> Each local variable, each named type, each value of an enum—all of these are separate symbols.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> In addition to symbol tables that basically map character strings to address and type information, GDB builds line tables that support lookup in two directions; from source lines to addresses, and then from addresses back to source lines.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> The procedural languages for which GDB was designed share a common runtime architecture, in that function calls cause the program counter to be pushed on a stack, along with some combination of function arguments and local arguments. The assemblage is called a stack frame, or "frame" for short, and at any moment in a program's execution, the stack consists of a sequence of frames chained together.,

[[gdb stack frame]]

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> Originally GDB kept track of frames by using the literal value of a fixed-frame pointer register. ,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> Value structs have a number of fields recording various properties; important ones include an indication of whether the value is an r-value or l-value (l-values can be assigned to, as in C), and whether the value is to be constructed lazily.,

- [ ] [[$ 221106 - Khái niệm r-value, l-value trong gdb nghĩa là gì 🔎]] #tasks/todo 
- [[gdb l-value]]
- [[gdb r-value]]

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> The reading process starts with the BFD library. BFD is a sort of universal library for handling binary and object files; running on any host, it can read and write the original Unix a.out format, COFF (used on System V Unix and MS Windows), ELF (modern Unix, GNU/Linux, and most embedded systems), and some other file formats.,

- [[BFD Library]] đọc và ghi các file `a.out` (định dạng Unix nguyên bản), định dạng [[COFF]], định dạng [[ELF]] (Unix, GNU/Linux hiện đại)

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> GDB only uses BFD to read files, using it to pull blocks of data from the executable file into GDB's memory.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> information in the DWARF debug format is contained in specially named sections of an ELF file,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> Partial symbol tables allow GDB to start up in only a few seconds, even for large programs.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

![[Pasted image 20221106114634.png]]

> GDBserver doesn't do anything that native GDB can't do; if your target system can run GDBserver, then theoretically it can run GDB. However, GDBserver is 10 times smaller and doesn't need to manage symbol tables, so it is very convenient for embedded GNU/Linux usages and the like.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> The command-line interface uses the standard GNU library readline to handle the character-by-character interaction with the user.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> The command-line interface uses the standard GNU library readline to handle the character-by-character interaction with the user. Readline takes care of things like line editing and command completion; the user can do things like use cursor keys to go back in a line and fix a character.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> GDB then takes the command returned by readline and looks it up using a cascaded structure of command tables, where each successive word of the command selects an additional table,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

> Additional frontends include a tcl/tk-based version called GDBtk or Insight, and a curses-based interface called the TUI, originally contributed by Hewlett-Packard. GDBtk is a conventional multi-paned graphical interface built using the tk library, while the TUI is a split-screen interface.,

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

---

>  Machine Interface or MI for short. It is still fundamentally a command-line interface, but both commands and results have additional syntax that makes everything explicit—each argument is bounded by quotes, and complex output has delimiters for subgroups and parameter names for component pieces.,

[[GDB Machine Interface (MI)]]

source:: [The Architecture of Open Source Applications (Volume 2): GDB](http://www.aosabook.org/en/gdb.html) 
at [[2022-11-06]].

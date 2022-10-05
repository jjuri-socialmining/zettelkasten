# Cygwin error while loading shared librarires

error while loading shared libraries: ?: cannot open shared object file: No such file or directory

```
$ ./example
C:/Users/dutran/projects/hsc/lynx/api/examples/example.exe: error while loading shared libraries: ?: cannot open shared object file: No such file or directory

$ ldd example
        ntdll.dll => /cygdrive/c/WINDOWS/SYSTEM32/ntdll.dll (0x77cb0000)
        KERNEL32.DLL => /cygdrive/c/WINDOWS/System32/KERNEL32.DLL (0x77ba0000)
        KERNELBASE.dll => /cygdrive/c/WINDOWS/System32/KERNELBASE.dll (0x76ae0000)
        libolympus.so => /cygdrive/c/Users/dutran/projects/hsc/lynx/api/examples/libolympus.so (0x6e640000)
        cygwin1.dll => /usr/bin/cygwin1.dll (0x61000000)

$ ldd libolympus.so
        ntdll.dll => /cygdrive/c/WINDOWS/SYSTEM32/ntdll.dll (0x77cb0000)
        KERNEL32.DLL => /cygdrive/c/WINDOWS/System32/KERNEL32.DLL (0x77ba0000)
        KERNELBASE.dll => /cygdrive/c/WINDOWS/System32/KERNELBASE.dll (0x76ae0000)
        msvcrt.dll => /cygdrive/c/WINDOWS/System32/msvcrt.dll (0x77320000)
        QIPCAP.dll => /cygdrive/c/WINDOWS/System32/QIPCAP.dll (0x68000000)
        ADVAPI32.dll => /cygdrive/c/WINDOWS/System32/ADVAPI32.dll (0x77020000)
        sechost.dll => /cygdrive/c/WINDOWS/System32/sechost.dll (0x76d00000)
        RPCRT4.dll => /cygdrive/c/WINDOWS/System32/RPCRT4.dll (0x76d80000)
        SHELL32.dll => /cygdrive/c/WINDOWS/System32/SHELL32.dll (0x76170000)
        msvcp_win.dll => /cygdrive/c/WINDOWS/System32/msvcp_win.dll (0x76890000)
        ucrtbase.dll => /cygdrive/c/WINDOWS/System32/ucrtbase.dll (0x76910000)
        USER32.dll => /cygdrive/c/WINDOWS/System32/USER32.dll (0x75e30000)
        win32u.dll => /cygdrive/c/WINDOWS/System32/win32u.dll (0x76730000)
        GDI32.dll => /cygdrive/c/WINDOWS/System32/GDI32.dll (0x77a90000)
        gdi32full.dll => /cygdrive/c/WINDOWS/System32/gdi32full.dll (0x77ac0000)
        DNSAPI.dll => /cygdrive/c/WINDOWS/SYSTEM32/DNSAPI.dll (0x70590000)
        IMM32.DLL => /cygdrive/c/WINDOWS/System32/IMM32.DLL (0x76e40000)
        IPHLPAPI.DLL => /cygdrive/c/WINDOWS/SYSTEM32/IPHLPAPI.DLL (0x74c70000)
        NSI.dll => /cygdrive/c/WINDOWS/System32/NSI.dll (0x75b80000)
        PGHook.dll => /cygdrive/c/Program Files (x86)/Avecto/Privilege Guard Client/PGHook.dll (0x75a90000)
        CRYPTSP.dll => /cygdrive/c/WINDOWS/SYSTEM32/CRYPTSP.dll (0x75a70000)
        rsaenh.dll => /cygdrive/c/WINDOWS/system32/rsaenh.dll (0x75a40000)
        bcrypt.dll => /cygdrive/c/WINDOWS/System32/bcrypt.dll (0x76e70000)
        CRYPTBASE.dll => /cygdrive/c/WINDOWS/SYSTEM32/CRYPTBASE.dll (0x75a30000)
        bcryptPrimitives.dll => /cygdrive/c/WINDOWS/System32/bcryptPrimitives.dll (0x75dd0000)
        libolympus.so => /cygdrive/c/Users/dutran/projects/hsc/lynx/api/examples/libolympus.so (0x6e640000)
        cygwin1.dll => /usr/bin/cygwin1.dll (0x61000000)
        InphiOlympus.dll => not found

$ cygcheck InphiOlympus.dll
cygcheck: could not find 'InphiOlympus.dll'

```

## Reason:
When executing example file, it will load dynamic lib `libolympus.so` then load `InphiOlympus.dll`. But os can not find `InphiOlympus.dll` in `PATH` environment.

Add path that InphiOlympus.dll locate in to PATH, Assume .dll lib in `c:\your_dll_path`
```
$ export PATH=/cygdrive/c/your_dll_path:$PATH
```

Then recheck
```
$ cygcheck InphiOlympus.dll
Found: C:\Users\dutran\projects\hsc\lynx\api\examples\olympus\InphiOlympus.dll
C:\Users\dutran\projects\hsc\lynx\api\examples\olympus\InphiOlympus.dll
  C:\WINDOWS\system32\SETUPAPI.dll
    C:\WINDOWS\system32\msvcrt.dll
      C:\WINDOWS\system32\ntdll.dll
      C:\WINDOWS\system32\KERNELBASE.dll
    C:\WINDOWS\system32\RPCRT4.dll
    C:\WINDOWS\system32\KERNEL32.dll
    C:\WINDOWS\system32\CFGMGR32.dll
    C:\WINDOWS\system32\bcrypt.dll
  C:\WINDOWS\system32\USER32.dll
    C:\WINDOWS\system32\win32u.dll
    C:\WINDOWS\system32\GDI32.dll
  C:\WINDOWS\system32\ADVAPI32.dll
    C:\WINDOWS\system32\SECHOST.dll

$ ldd example
        ntdll.dll => /cygdrive/c/WINDOWS/SYSTEM32/ntdll.dll (0x77cb0000)
        KERNEL32.DLL => /cygdrive/c/WINDOWS/System32/KERNEL32.DLL (0x77ba0000)
        KERNELBASE.dll => /cygdrive/c/WINDOWS/System32/KERNELBASE.dll (0x76ae0000)
        libolympus.so => /cygdrive/c/Users/dutran/projects/hsc/lynx/api/examples/libolympus.so (0x6e640000)
        cygwin1.dll => /usr/bin/cygwin1.dll (0x61000000)
        InphiOlympus.dll => /cygdrive/c/Users/dutran/projects/hsc/lynx/api/examples/olympus/InphiOlympus.dll (0x6ab90000)
        SETUPAPI.dll => /cygdrive/c/WINDOWS/System32/SETUPAPI.dll (0x773e0000)
        msvcrt.dll => /cygdrive/c/WINDOWS/System32/msvcrt.dll (0x77320000)
        cfgmgr32.dll => /cygdrive/c/WINDOWS/System32/cfgmgr32.dll (0x76fe0000)
        ucrtbase.dll => /cygdrive/c/WINDOWS/System32/ucrtbase.dll (0x76910000)
        RPCRT4.dll => /cygdrive/c/WINDOWS/System32/RPCRT4.dll (0x76d80000)
        bcrypt.dll => /cygdrive/c/WINDOWS/System32/bcrypt.dll (0x76e70000)
        USER32.dll => /cygdrive/c/WINDOWS/System32/USER32.dll (0x75e30000)
        win32u.dll => /cygdrive/c/WINDOWS/System32/win32u.dll (0x76730000)
        GDI32.dll => /cygdrive/c/WINDOWS/System32/GDI32.dll (0x77a90000)
        gdi32full.dll => /cygdrive/c/WINDOWS/System32/gdi32full.dll (0x77ac0000)
        msvcp_win.dll => /cygdrive/c/WINDOWS/System32/msvcp_win.dll (0x76890000)
        ADVAPI32.dll => /cygdrive/c/WINDOWS/System32/ADVAPI32.dll (0x77020000)
        sechost.dll => /cygdrive/c/WINDOWS/System32/sechost.dll (0x76d00000)

$ ./example
This example program attempts to communicate
with the evaluation board GUI. To use it you
need to specify the IP address and port number
of the eval GUI or modify the example for your
environment
Usage: ./example ip_addr port_num test_name

```
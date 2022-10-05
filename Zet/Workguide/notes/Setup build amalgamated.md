# Setup build amalgamated

Clone 3rdparty, bin repo

![[Pasted image 20220331115153.png]]

Add PATH_PYTHON 2.7
![[Pasted image 20220331115306.png]]

Run env to show environment
```
env
```

or add `/cygdrive/c/Python27` to Cygwin PATH
```
export PATH="/cygdrive/c/Python27:/usr/local/bin:/usr/bin:/cygdrive/c/Program Files (x86)/Common Files/Oracle/Java/javapath:/cygdrive/c/WINDOWS/system32:/cygdrive/c/WINDOWS:/cygdrive/c/WINDOWS/System32/Wbem:/cygdrive/c/WINDOWS/System32/WindowsPowerShell/v1.0:/cygdrive/c/WINDOWS/System32/OpenSSH:/cygdrive/c/Program Files/Git/cmd:/cygdrive/c/Program Files/Microsoft SQL Server/110/Tools/Binn:/cygdrive/c/Program Files/VSCodium/bin:/cygdrive/c/Users/hcmswlab/AppData/Local/Microsoft/WindowsApps:/cygdrive/c/usr/tools/VSCodium:/cygdrive/c/Users/hcmswlab/AppData/Local/Programs/Microsoft VS Code/bin:/cygdrive/c/usr/build_api/3rdparty/win32"
```
In cygwin, remember install `make` tool
```
$ make amalgamated
/cygdrive/c/usr/dutran/example/hsc/lynx/api//../../../bin/make/os.inc:122: "Detected Cygwin or Msys"
```

##
Make api in cygwin but detect os is windows32 instead CYGWIN
```
C:/usr/dutran/example/hsc/lynx/api//../../../bin/make/os.inc:18: "Catch windows32"
C:/usr/dutran/example/hsc/lynx/api//../../../bin/make/os.inc:152: "Detected Windows"
C:/usr/dutran/example/hsc/lynx/api//../../../bin/make/os.inc:172: "Using MSVC in vs12/14"
C:/usr/dutran/example/hsc/lynx/api//../../../bin/make/os.inc:198: "Don't know where perl should come from, so using whatever is found in PATH"
C:/usr/dutran/example/hsc/lynx/api//../../../bin/make/os.inc:215: "Please specify path to shorte scripts in var PATH_SHORTE"
```

Solve: `which make`
-> Cygwin may not install make yet

## Releate:
[[Cygwin setup for building hsc_api]]
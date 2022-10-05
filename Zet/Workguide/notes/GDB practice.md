```
$ gdb

gdb $
gdb $ file <file_name>
gdb $ run <option to run with file>

# set breakpoint to function
gdb $ b <function name>

# print variable
gdb $ p <variable name>

# next line
gdb $ n

# continue
gdb $ c


```

gdb --arg
```
gdb --arg build-output/tests/tests.exe --ip 127.0.0.1 --port 60008 --product spicap --suite query_init
```

## Relate
- [[Run GDB to debug API example]]
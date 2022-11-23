---
title: GUI Development with Python and Tkinter
UID: 221122230348
created: 22-Nov-2022
tags:
  - 'created/2022/Nov/22'
  - 'daily/journal'
---
## Notes:
url:: https://marvell.udemy.com/course/desktop-gui-python-tkinter/learn/lecture/16430628#overview
source_code:: https://github.com/tecladocode/gui-development-tkinter-course, 
https://github.com/omegakid1902/gui-development-tkinter-course

### Introduction
- Nên dùng python version 3.5+ để dev Tkinter, vì python sau version này có nhiều tính năng giúp Tkinter trông đẹp hơn
-  Dùng [Repl.it](https://repl.it) (web base editor) giúp code python và cả Tkinter. Show kết quả
- Hoặc dùng [[PyCharm IDE]]

### Python refresher
Giới thiệu python basic

### Tkinter intro
Tkinter need Tcl/tk

#### simplest program
```python
import tkinter as tk

root = tk.Tk()
root.mainloop()
```

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

ttk.Label(root, text="Hello, World!", padding=(30, 10)).pack()

root.mainloop()
```
#### Button
```python
import tkinter as tk
from tkinter import ttk

def greet():
	print("hello world!")

root = tk.Tk()

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(side="left")

quit_btn = ttk.Button(root, text="Quit", command=root.destroy)
quit_btn.pack(side="left")

root.mainloop()
```

- Default `greet_btn.pack()` sẽ tạo đối tượng button ngay chính giữa, phía dưới đối tượng cuối cùng được tạo trước đó

`greet_btn.pack(side="left", fill="x", expand=True)`

#### Greeting app
```python
import tkinter as tk
from tkinter import ttk

def greet():
	print(f"hello, {user_name.get() or 'World'}!")

root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(side="left")

quit_btn = ttk.Button(root, text="Quit", command=root.destroy)
quit_btn.pack(side="right")

root.mainloop()
```

#### Packing component
```python
import tkinter as tk
from tkinter import ttk

def greet():
	print(f"hello, {user_name.get() or 'World'}!")

root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(side="left")

quit_btn = ttk.Button(root, text="Quit", command=root.destroy)
quit_btn.pack(side="right")

root.mainloop()
```
#### Frame
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

tk.Label(main, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(main, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")

root.mainloop()
```

#### Geometry
[[grid và pack trong tkinter khác nhau ở điểm nào❓]]

#### High DPI
```python
# For window setting with nicer view
def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
```
### Tkinter Widget reference
Cần  `Pillow` lib để attach image vào [[Tkinter]]

![[Pasted image 20221123001204.png]]

### Milestone project
### OOP with Tkinter
### Tkinter styling
### Build Chat App
### Snake game
### Packaging and Distributing




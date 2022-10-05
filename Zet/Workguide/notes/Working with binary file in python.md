---
title: Working with binary file in python
created: 2022-Jul-14
tags:
  - 'permanent/howto'
---

## Read/write

- String style
```python
# Open a file handler to create a binary file
file_handler = open("string.bin", "wb")  

# Add two lines of text in the binary file  
file_handler.write(b"Welcome to LinuxHint.\nLearn Python Programming.")  

# Close the file handler  
file_handler.close()
```




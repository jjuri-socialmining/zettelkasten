Source: http://www.swig.org/Doc1.3/Python.html#Python_nn46

## Pointer
With the C code

```c
void add(int x, int y, int *result) {
   *result = x + y;
}
```

or

```c
int sub(int *x, int *y) {
   return *x-*y;
}
```

### 1. The simple way to handle this is using `typemap.i`
```swig
%module example
%include "typemaps.i"

void add(int, int, int *OUTPUT);
int  sub(int *INPUT, int *INPUT);
```

### 2. Use `%apply`
```swig
%module example
%include "typemaps.i"

%apply int *OUTPUT { int *result };
%apply int *INPUT  { int *x, int *y};

void add(int x, int y, int *result);
int  sub(int *x, int *y);
```

### Result:
After that, python will handle
```python
>>> a = add(3,4)
>>> print a
7
>>> b = sub(7,4)
>>> print b
3
>>>
```

## Unbound Array
Constants, as declared by the preprocessor `#define` macro or SWIG %constant directive, are included in SWIGs parse tree
when it can be determined that they are, or could be reduced to, a literal value. Such values are translated into defconstant forms
in the generated lisp wrapper when the −nocwrap command−line options is used. Else, wrapper functions are generated as in the
case of variable access (see section below).
Here are examples of simple preprocessor constants when using −nocwrap.
```
#define A 1 => (swig−defconstant "A" 1)
#define B 'c' => (swig−defconstant "B" #\c)
#define C B => (swig−defconstant "C" #\c)
#define D 1.0e2 => (swig−defconstant "D" 1.0d2)
#define E 2222 => (swig−defconstant "E" 2222)
#define F (unsigned int)2222 => no code generated
#define G 1.02e2f => (swig−defconstant "G" 1.02f2)
#define H foo => no code generated
```
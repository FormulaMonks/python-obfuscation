# Python code Protection Mechanisms - Code Scrambling

This mechanism will make use of Python [Abstract Syntax Trees](https://docs.python.org/2/library/ast.html)
and an [import hook](https://www.python.org/dev/peps/pep-0302/) in order to
scramble code and unscramble it on import time.


## Description

Python [Abstract Syntax Trees](https://docs.python.org/2/library/ast.html) is
a tool to process of Python abstract syntax grammar, which can be modified on
any way before the code is evaluated by the interpreter.

In this case the code will be scrambled and written back to the file system.
Later the application will configure an import hook to detect scrambled code
and unscramble it on import time.

The scrambling algorithm is fair simple, but good enough for this example.

## Pros

1. Simple to implement, scrambling algorithms can vary to make them more
   complicated to crack.

## Cons

1. The unscrambling code must be available in the server in order to run the
   application (the module can be compiled with Cython or implemented as python
   extension).

2. The decrypted code in memory can be inspected and dumped and decompiled from
   byte-code back to python.

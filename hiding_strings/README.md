# Python code Protection Mechanisms - Hidding Strings

Process an python application and encode strings by processing the walking
through the Abstract Syntax Trees.


## Description

In this example, we will be customizing the processing a python application by
walking the Abstract Syntax Trees and replacing strings occurrences with
encoded versions that automatically decode on runtime. This comes handy when
using [Cython](http://cython.org/) to compile the application code to Python
extensions, that way a simple ``strings`` command won't be very useful to
extract strings in the lib.

This example uses [unparse.py](http://svn.python.org/view/python/trunk/Demo/parser/unparse.py?view=markup).

## Pros

1. Walking the AST is a very powerful transformation tool, this example just
   do string replacement, but more advanced transformations are possible.

## Cons

1. This just encodes strings (the example uses ``rot13``, but a custom encoder
   or translation table can be implemented). This is just a hiding technique.

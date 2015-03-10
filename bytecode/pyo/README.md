# Python code Protection Mechanisms - Optimized Byte-code distribution

Compile ``.py`` into ``.pyo`` to distribute, there's not much gain compared
with the usual ``.pyc`` files since optimized byte-code mostly disables
``assert`` calls and removes docstrings.

## Description

In this example, we will be using [compileall](https://docs.python.org/2/library/compileall.html)
to compile the different ``.py`` files into ``.pyo``, then remove the ``.py``
keeping the application functionality.

## Pros

1. Simple to implement (just a command call is needed).

## Cons

1. Optimized byte-code is easily converted back to python code,
   [uncompyle2](https://pypi.python.org/pypi/uncompyle2) does the work to build
   back the ``.py`` files very well.

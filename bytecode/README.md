# Python code Protection Mechanisms - Byte-code distribution

Compile ``.py`` into ``.pyc`` to distribute.

## Description

In this example, we will be using [compileall](https://docs.python.org/2/library/compileall.html)
to compile the different ``.py`` files into ``.pyc``, then remove the ``.py``
keeping the application functionality.

## Pros

1. Simple to implement (just a command call is needed)

## Cons

1. Byte-code is easilly converted back to python code, [uncompyle2](https://pypi.python.org/pypi/uncompyle2)
   does the work to build back the ``.py`` files very well.

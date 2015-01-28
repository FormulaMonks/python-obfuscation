# Python code Protection Mechanisms - Cython

Cython mechanism to protect a python codebase.

## Description

In this example, we will be using [Cython](http://cython.org/) to
compile the different ``.py`` files into ``.so`` libs without loosing
import capabilities or code functionality.

Cython will compile the given python module into a ``.c`` source code,
which is then compiled by ``gcc`` as a shared library (``.so``). Finally,
the ``.py`` files can be removed, leaving just the ``.so``.

**Note**: The ``__init__.py`` files **must** be kept in the tree, otherwise
	      ``import`` won't work.

## Pros

## Cons

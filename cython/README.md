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

1. Code speedup: since the code is translated to C, it's going to run
   faster compared to the python version.

2. Assembler ananlysis is needed in order to rebuild the code, which
   is compiled with ``O2`` flag (optimization) making the task even
   harder to achieve.

3. Code compilation can be applied just to key components of the
   application if necessary.

4. [UPX](http://upx.sourceforge.net/) compressor can applied in the
   generated libraries (avoids ``objdump`` assembler dumping, but it's
   possible to decompress it)

## Cons

1. Cython is not 100% python compatible [yet](http://docs.cython.org/src/userguide/limitations.html)

2. Cross-compilation is needed to properly build the binaries for the
   supported environments (docker can be used to achieve this)

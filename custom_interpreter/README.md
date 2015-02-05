# Python code Protection Mechanisms - Custom Interpreter

Customize python interpreter to protect a python codebase.

## Description

In this example, we will be customizing the CPython interpreter in order to
introduce protection measures to avoid the reverse engineering of the codebase.

So far the following protections were introduced:

    1. Opcode scrambling to protect against tools like [uncompyle2](https://pypi.python.org/pypi/uncompyle2)

The following protections will be investigated too:

    1. Dynamic ``opcode`` tables (use a different ``opcode`` table for each
       ``.py`` file to make decompiling technics even harder)
    2. Removal of properties that leak code (``co_code``, etc)
    3. Removal of functions that allow code injection (``PyRun_SimpleString``,
       ``compile``, etc)
    4. Built-in encryption support

## Pros

1. Customizing the python interpreter opens the door to several protection
   mechanisms available for C applications (like anti-debugging techniques)

2. Conventional tools to reverse-engineer python application won't work,
   [pyREtic](https://github.com/MyNameIsMeerkat/pyREtic) might still work for
   if scrambled-opcodes is the only technique used.

## Cons

1. The whole python platform needs to be distributed when deployed to the
   servers (cross-compilation is needed for this)

2. Only ``.pyc`` files must be deployed (check [bytecode](../bytecode) example)

3. The application **must** be run with this interpreter, ``pyenv`` comes handy
   when deploying the application.

4. Demands a very good knowledge of the python interpreter internals

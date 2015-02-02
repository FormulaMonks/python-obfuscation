# Python code Protection Mechanisms - Import Hook

This mechanism will use an [import hook](https://www.python.org/dev/peps/pep-0302/)
in order to detect encrypted modules on import time.


## Description

In this example we will be using an [import hook](https://www.python.org/dev/peps/pep-0302/)
to detect encrypted modules when they are being imported, the detection is done
by verifying a signature in the encrypted files (in this case the signature is
a simple string ``AESENC:``.

The encrypted modules follow a simple format: ``AESENC:<encrypted src code>``,
the signature is stripped, the code is decrypted and "evaluated" in the context
of a in-memory created module.

## Pros

1. Simple to implement (just a command call is needed).
2. Strong encryption algorithms supported.

## Cons

1. The encryption key *must* be available in the server in order to run the
   application (unless it's possible to run it on demand by accessing the
   server over ssh and input the password in the command line, but still it's
   going to live in a in-memory object which can be inspected).

2. The decrypted code in memory can be inspected and dumped and decompiled from
   byte-code back to python.

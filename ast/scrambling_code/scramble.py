import os
import sys
import ast

from scrambler import Scrambler
from unparse import Unparser


for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        if file.endswith('.py'):
            with open('{0}/{1}'.format(root, file), 'r') as f:
                code = ''.join(f.readlines())
            if code:
                with open('{0}/{1}'.format(root, file), 'w') as f:
                    node = ast.parse(code)
                    encoded = Scrambler(scramble=True).visit(node)
                    f.write('{0}\n'.format(Scrambler.HEADER))
                    Unparser(encoded, f)
                    f.write('\n')

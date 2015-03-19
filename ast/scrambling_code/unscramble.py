import os
import sys
import ast

from scrambler import Scrambler
from unparse import Unparser


for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        if file.endswith('.py'):
            with open('{0}/{1}'.format(root, file), 'r') as f:
                lines = f.readlines()
                if lines[0].strip() != Scrambler.HEADER:
                    continue
                code = ''.join(lines[1:])
            with open('{0}/{1}'.format(root, file), 'w') as f:
                node = ast.parse(code)
                decoded = Scrambler(scramble=False).visit(node)
                Unparser(decoded, f)
                f.write('\n')

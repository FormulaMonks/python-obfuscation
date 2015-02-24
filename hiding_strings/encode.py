import os
import sys
import ast

from tree_parser import EncodeStrings
from unparse import Unparser


for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        if file.endswith('.py'):
            with open('{0}/{1}'.format(root, file), 'r') as f:
                code = ''.join(f.readlines())
            with open('{0}/{1}'.format(root, file), 'w') as f:
                node = ast.parse(code)
                encoded = EncodeStrings().visit(node)
                Unparser(encoded, f)
                f.write('\n')

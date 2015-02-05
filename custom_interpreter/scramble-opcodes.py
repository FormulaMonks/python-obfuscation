# Scramble python opcodes table to avoid byte-code to python decompilation
import os
import re
import random
import argparse


OPCODE_H = 'Include/opcode.h'
OPCODE_RE = re.compile(
    r'^#define\s+(?P<name>[A-Z_]+)\s+(?P<code>\d+)(?P<extra>.*)'
)


def fix_offests(opcodes, ignore_names, value, offs):
    if not isinstance(ignore_names, (list, tuple)):
        ignore_names = [ignore_names]

    new_opcodes = {}
    for key, val in opcodes.items():
        if key not in ignore_names and val >= value:
            val += offs
        new_opcodes[key] = val
    return new_opcodes


def slice_opcodes(opcodes):
    for name in ['SLICE', 'STORE_SLICE', 'DELETE_SLICE']:
        if name in opcodes:
            opcodes = fix_offests(opcodes, name, opcodes[name], 4)
    return opcodes


def call_function_opcodes(opcodes):
    if 'CALL_FUNCTION' in opcodes:
        opcodes['CALL_FUNCTION_VAR'] = opcodes['CALL_FUNCTION'] + 9
        opcodes['CALL_FUNCTION_KW'] = opcodes['CALL_FUNCTION_VAR'] + 1
        opcodes['CALL_FUNCTION_VAR_KW'] = opcodes['CALL_FUNCTION_VAR'] + 2
        opcodes = fix_offests(opcodes, [
            'CALL_FUNCTION_VAR',
            'CALL_FUNCTION_KW',
            'CALL_FUNCTION_VAR_KW'
        ], opcodes['CALL_FUNCTION_VAR'], 3)
    return opcodes


def is_opcode(line):
    return OPCODE_RE.match(line)


def fix_opcodes_offsets(opcodes):
    opcodes = slice_opcodes(opcodes)
    opcodes = call_function_opcodes(opcodes)
    return opcodes


def opcode(line):
    match = is_opcode(line)
    if match:
        return (match.group('name'),
                int(match.group('code')),
                match.group('extra'))


def scramble_subset(opcodes):
    names = [name for name, code, extra in opcodes]
    opcodes = [code for name, code, extra in opcodes]
    random.shuffle(opcodes)
    return dict(zip(names, opcodes))


def scramble_opcodes(src):
    path = os.path.join(src, OPCODE_H)
    lines = []
    dont_have_arg = []
    have_arg = []

    with open(path, 'r') as file:
        file_lines = file.readlines()
        opcodes = filter(None, map(opcode, file_lines))

        have = False
        for name, code, extra in opcodes:
            if name == 'HAVE_ARGUMENT':
                have = True
                continue
            opcodes_set = have_arg if have else dont_have_arg
            opcodes_set.append((name, code, extra))

        dont_have_arg = scramble_subset(dont_have_arg)
        have_arg = scramble_subset(have_arg)
        have_arg['HAVE_ARGUMENT'] = min(have_arg.values())
        opcodes = dict(dont_have_arg)
        opcodes.update(have_arg)
        opcodes = fix_opcodes_offsets(opcodes)

        for line in file_lines:
            match = is_opcode(line)
            if match:
                name = match.group('name')
                line = '#define {0} {1}{2}\n'.format(name, opcodes[name],
                                                     match.group('extra'))
            lines.append(line)

    with open(path, 'w') as file:
        file.write(''.join(lines))


parser = argparse.ArgumentParser(description='Scramble python opcodes table')
parser.add_argument('--python-source', dest='src', type=str,
                    help='Python source code', required=True)


if __name__ == '__main__':
    args = parser.parse_args()
    scramble_opcodes(args.src)

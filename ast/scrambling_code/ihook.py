import os
import sys
import imp
import ast

from scrambler import Scrambler


class BaseLoader(object):
    def modinfo(self, name, path):
        try:
            modinfo = imp.find_module(name.rsplit('.', 1)[-1], path)
        except ImportError:
            if '.' not in name:
                raise
            clean_path, clean_name = name.rsplit('.', 1)
            clean_path = [clean_path.replace('.', '/')]
            modinfo = imp.find_module(clean_name, clean_path)

        file, pathname, (suffix, mode, type_) = modinfo
        if type_ == imp.PY_SOURCE:
            filename = pathname
        elif type_ == imp.PY_COMPILED:
            filename = pathname[:-1]
        elif type_ == imp.PKG_DIRECTORY:
            filename = os.path.join(pathname, '__init__.py')
        else:
            return (None, None)
        return (filename, modinfo)


class Loader(BaseLoader):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def is_package(self, val):
        """Flask requirement"""
        return None

    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        filename, modinfo = self.modinfo(self.name, self.path)
        if filename is None and modinfo is None:
            return None

        file = modinfo[0] or open(filename, 'r')
        src = ''.join(file.readlines())
        src = self.unscramble(src)
        src = ast.fix_missing_locations(src)

        module = imp.new_module(name)
        module.__file__ = filename
        module.__path__ = [os.path.dirname(os.path.abspath(file.name))]
        module.__loader__ = self
        sys.modules[name] = module
        codeobj = compile(src, name, 'exec')
        eval(codeobj, module.__dict__, module.__dict__)
        print 'scrambled module loaded: {0}'.format(name)
        return module

    def unscramble(self, code):
        node = ast.parse(code)
        code = Scrambler(scramble=False).visit(node)
        return code


class Finder(BaseLoader):
    def find_module(self, name, path=None):
        filename, modinfo = self.modinfo(name, path)
        if filename is None and modinfo is None:
            return None

        file = modinfo[0] or open(filename, 'r')
        if file.read(len(Scrambler.HEADER)) == Scrambler.HEADER:
            print 'scrambled module found: {0} (at {1})'.format(name, path)
            file.seek(0)
            return Loader(name, path)


def install_hook():
    sys.meta_path.insert(0, Finder())

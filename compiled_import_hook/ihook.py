import os
import sys
import imp
import base64

from Crypto.Cipher import AES


SECRET = 'abcdefghijklmnop'
SIGNATURE = 'AESENC:'


class AESCypher(object):
    def __init__(self, secret=None, block_size=16, padding='$'):
        # block_size = 16 -> 128bits
        self.block_size = block_size
        self.padding = padding
        self.secret = secret or os.urandom(self.block_size)

    def add_padding(self, val):
        bsize, padding = self.block_size, self.padding
        return val + (bsize - len(val) % bsize) * padding

    def encode_aes(self, cipher, value):
        return base64.b64encode(cipher.encrypt(self.add_padding(value)))

    def decode_aes(self, chipher, value):
        return chipher.decrypt(base64.b64decode(value)).rstrip(self.padding)

    def encrypt(self, private_info):
        return self.encode_aes(AES.new(self.secret), private_info)

    def decrypt(self, value):
        return self.decode_aes(AES.new(self.secret), value)


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
        src = self.decrypt_to(src[len(SIGNATURE):])

        module = imp.new_module(name)
        module.__file__ = filename
        module.__path__ = [os.path.dirname(os.path.abspath(file.name))]
        module.__loader__ = self
        sys.modules[name] = module
        exec(src,  module.__dict__)
        print "encrypted module loaded: {0}".format(name)
        return module

    def decrypt_to(self, input):
        return AESCypher(SECRET).decrypt(input)


class Finder(BaseLoader):
    def find_module(self, name, path=None):
        filename, modinfo = self.modinfo(name, path)
        if filename is None and modinfo is None:
            return None

        file = modinfo[0] or open(filename, 'r')
        if file.read(len(SIGNATURE)) == SIGNATURE:
            print "encrypted module found: {0} (at {1})".format(name, path)
            file.seek(0)
            return Loader(name, path)


def install_hook():
    sys.meta_path.insert(0, Finder())


def encrypt_all(location):
    cipher = AESCypher(SECRET)

    for root, dirs, files in os.walk(location):
        files = (f for f in files if f.endswith('.py'))
        for name in files:
            enc_name = '{0}/{1}-enc'.format(root, name)
            orig_name = '{0}/{1}'.format(root, name)

            with open(orig_name, 'r') as input:
                with open(enc_name, 'wb') as output:
                    content = cipher.encrypt(''.join(input.readlines()))
                    content = '{0}{1}'.format(SIGNATURE, content)
                    output.write(content)
            os.rename(enc_name, orig_name)


if __name__ == '__main__':
    encrypt_all(sys.argv[1])

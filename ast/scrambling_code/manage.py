#!/usr/bin/env python

# Install import hook
import ihook
ihook.install_hook()

from flask_script import Server, Manager, Shell

from app import app


manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=lambda: {
    'app': app,
}))


if __name__ == '__main__':
    manager.run()

#!/usr/bin/env python3

"""This file is named to immitate the principle of django over the debugger system and reloader manager"""

#set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from tumblelog import app

manager = Manager(app)

#Turn on debugger by default and reloader
manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
    )

if __name__ == '__main__':
    manager.run()

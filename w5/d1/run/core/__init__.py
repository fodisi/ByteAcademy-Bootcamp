
#!/usr/bin/env python3

import os

from flask import Flask

from core.controllers.featured import controller as featured


def key_maker(omnibus, filename='secretkey'):
    pathname = os.path.join(omnibus.instance_path, filename)
    try:
        print('Im trying to find a directory labelled instance')
        print('Im trying to find a file labelled secret_key')
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()
        print('I found a directory labelled instance')
        print('I found a file labelled secret_key')
    except IOError:
        parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(parent_directory):
            print('i cant find a directory labeled instance...')
            print('im making a directory labelled instance')
            os.system('mkdir -p {}'.format(parent_directory))
        print('Im writing to a file labelled secret_key')
        os.system('head -c 24 /dev/urandom > {}'.format(pathname))
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()


omnibus = Flask(__name__)

# Enterpise Service Bus concept: register multiple controllers
omnibus.register_blueprint(featured)

# TODO write the following function
key_maker(omnibus)


#!/usr/bin/env python3

import os

from flask import Flask

from core.controllers.login import controller as login


omnibus = Flask(__name__)

omnibus.register_blueprint(login)

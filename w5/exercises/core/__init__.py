
#!/usr/bin/env python3

import os

from flask import Flask

from core.controllers.index import controller as index
from core.controllers.grandpa import controller as grandpa


omnibus = Flask(__name__)

omnibus.register_blueprint(index)
omnibus.register_blueprint(grandpa)

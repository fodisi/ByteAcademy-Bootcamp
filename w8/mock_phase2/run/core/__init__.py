#!usr/bin/env python3

from flask import Flask

from core.controllers.featured import controller as featured
from core.controllers.generic import controller as generic

omnibus = Flask(__name__)

omnibus.register_blueprint(featured)
omnibus.register_blueprint(generic)
